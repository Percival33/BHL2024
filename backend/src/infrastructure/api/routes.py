<<<<<<< HEAD
<<<<<<< HEAD
from collections import defaultdict
from typing import Annotated

import chromadb
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Header, UploadFile

from src.application.speech_to_text import SpeechToText
from src.application.summarizer import Summarizer
from src.domain.session_id import SessionId
=======
=======
import chromadb
>>>>>>> 741159d (Setup chromadb)
import uvicorn
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

>>>>>>> 99a700f (setup dependency injector framework)
from src.infrastructure.containers import Container

router = APIRouter()

<<<<<<< HEAD
chunk_counter = defaultdict(int)


@router.post("/upload_audio")
@inject
async def process_audio_chunk(
        session_id: Annotated[str, Header(default_factory=SessionId.generate)],
        audio_file: UploadFile,
) -> None:
    chunk_counter[session_id] += 1

    content = await audio_file.read()

    with open(f"recordings/{session_id}/chunk-{chunk_counter[session_id]}.mp3", "wb") as f:
        f.write(content)


@router.get("/suggestions/{fname}")
@inject
async def get_suggestions(
        fname: str,
        speech_to_text: SpeechToText = Depends(Provide[Container.speech_to_text]),
        summarizer: Summarizer = Depends(Provide[Container.summarizer]),
) -> None:
    print(fname)
    with open(fname, "rb") as f:
        transcript = speech_to_text.create_transcription(f)

    note = summarizer.summarize(transcript)
    print(note)
=======

@router.post("/summarize_chunk")
@inject
async def summarize_audio_chunk() -> None:
    pass


@router.get("/suggestions")
@inject
<<<<<<< HEAD
async def get_suggestions(aa: int = Depends(Provide[Container.int_provider])) -> None:
    print(aa)
>>>>>>> 99a700f (setup dependency injector framework)
=======
async def get_suggestions(
        chroma_client: chromadb.ClientAPI = Depends(Provide[Container.chroma_client])
) -> None:
    print(chroma_client.heartbeat())
>>>>>>> 741159d (Setup chromadb)
