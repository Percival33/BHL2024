from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, UploadFile, Depends, status, HTTPException

from src.application.note_repository import NoteRepository
from src.application.speech_to_text import SpeechToText
from src.application.summarizer import Summarizer
from src.domain.session_id import SessionId
from src.infrastructure.api.dependencies import provide_session_id
from src.infrastructure.api.responses import NoteResponse
from src.infrastructure.containers import Container

router = APIRouter()


@router.post("/upload_audio")
@inject
async def process_audio_chunk(
        audio_file: UploadFile,
        session_id: Annotated[SessionId, Depends(provide_session_id)],
        speech_to_text: SpeechToText = Depends(Provide[Container.speech_to_text]),
        summarizer: Summarizer = Depends(Provide[Container.summarizer]),
        note_repository: NoteRepository = Depends(Provide[Container.note_repository])
) -> None:
    content = await audio_file.read()

    file_name = f"recordings/chunk-{session_id.value}-{str(uuid.uuid4())}.mp3"

    with open(file_name, "wb") as f:
        f.write(content)

    with open(file_name, "rb") as f:
        transcript = speech_to_text.create_transcription(f)

    note = summarizer.summarize(session_id, transcript)

    note_repository.save(note)


@router.get("/suggestions/{fname}")
@inject
async def get_suggestions() -> None:
    pass


@router.get("/note")
@inject
async def find_notes(
        note_repository: NoteRepository = Depends(Provide[Container.note_repository])
) -> list[NoteResponse]:
    return list(map(lambda note: NoteResponse.from_note(note), note_repository.find()))


@router.get("/note/{session_id}")
@inject
async def get_note(
        session_id: str,
        note_repository: NoteRepository = Depends(Provide[Container.note_repository])
) -> NoteResponse:
    note = note_repository.find_one(SessionId(session_id))

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note doesn't exist")

    return NoteResponse.from_note(note)
