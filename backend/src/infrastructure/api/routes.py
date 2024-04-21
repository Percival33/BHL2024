from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, UploadFile, Depends, status, HTTPException, BackgroundTasks

from src.application.embedding_repository import EmbeddingRepository
from src.application.meeting_audio_analyzer import MeetingAudioAnalyzer
from src.application.note_repository import NoteRepository
from src.domain.meeting_id import MeetingId
from src.infrastructure.api.dependencies import provide_meeting_id
from src.infrastructure.api.responses import NoteResponse, UploadAudioResponse, SimilarNoteResponse
from src.infrastructure.containers import Container

router = APIRouter()


@router.post("/upload_audio", response_model=UploadAudioResponse)
@inject
async def process_audio_chunk(
        background_tasks: BackgroundTasks,
        audio_file: UploadFile,
        meeting_id: Annotated[MeetingId, Depends(provide_meeting_id)],
        meeting_audio_analyzer: MeetingAudioAnalyzer = Depends(Provide[Container.meeting_audio_analyzer]),
) -> UploadAudioResponse:
    audio_content = await audio_file.read()
    background_tasks.add_task(meeting_audio_analyzer.process_meeting_audio, meeting_id, audio_content)

    return UploadAudioResponse(meeting_id=meeting_id.value)


@router.get("/suggestions/{meeting_id}", response_model=list[SimilarNoteResponse])
@inject
async def get_suggestions(
        meeting_id: str,
        note_repository: NoteRepository = Depends(Provide[Container.note_repository]),
        embedding_repository: EmbeddingRepository = Depends(Provide[Container.embedding_repository]),
) -> list[SimilarNoteResponse]:
    meeting_id = MeetingId(meeting_id)

    note = note_repository.find_one(meeting_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note doesn't exist")

    similar_notes = [
        similar_note for similar_note in embedding_repository.find_similar(note)
        if similar_note.meeting_id.value != meeting_id.value
    ]

    similarities = {match.meeting_id.value: match.similarity for match in similar_notes}

    similar_notes = note_repository.find(ids=[note.meeting_id for note in similar_notes])

    return sorted(
        [SimilarNoteResponse.from_note(note, similarities[note.id.value]) for note in similar_notes],
        key=lambda x: x.similarity,
        reverse=True,
    )


@router.get("/note")
@inject
async def find_notes(
        note_repository: NoteRepository = Depends(Provide[Container.note_repository])
) -> list[NoteResponse]:
    return list(map(lambda note: NoteResponse.from_note(note), note_repository.find()))


@router.get("/note/{meeting_id}")
@inject
async def get_note(
        meeting_id: str,
        note_repository: NoteRepository = Depends(Provide[Container.note_repository])
) -> NoteResponse:
    note = note_repository.find_one(MeetingId(meeting_id))
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note doesn't exist")

    return NoteResponse.from_note(note)
