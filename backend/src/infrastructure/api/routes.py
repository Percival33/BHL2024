from collections import defaultdict
from typing import Annotated

import chromadb
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Header, UploadFile

from src.application.session_id_provider import create_session_id
from src.application.speech_to_text import SpeechToText
from src.infrastructure.containers import Container

router = APIRouter()

chunk_counter = defaultdict(int)


@router.post("/upload_audio")
@inject
async def process_audio_chunk(
        session_id: Annotated[str, Header(default_factory=create_session_id)],
        audio_file: UploadFile,
) -> None:
    chunk_counter[session_id] += 1

    content = await audio_file.read()

    with open(f"recordings/{session_id}/chunk-{chunk_counter[session_id]}.mp3", "wb") as f:
        f.write(content)


@router.get("/suggestions")
@inject
async def get_suggestions(
        chroma_client: chromadb.ClientAPI = Depends(Provide[Container.chroma_client])
) -> None:
    print(chroma_client.heartbeat())


@router.get("/transcription")
@inject
async def get_transcription(
        speech_to_text: SpeechToText = Depends(Provide[Container.speech_to_text])
) -> str:
    with open("audio.mp3", "rb") as f:
        return speech_to_text.create_transcription(f)
