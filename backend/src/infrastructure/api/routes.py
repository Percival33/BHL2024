<<<<<<< HEAD
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
=======
from collections import defaultdict
from typing import Annotated

import chromadb
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Header, UploadFile

from src.application.speech_to_text import SpeechToText
<<<<<<< HEAD
>>>>>>> ed700fa (Setup whisper speech to text)
=======
from src.application.summarizer import Summarizer
from src.domain.session_id import SessionId
>>>>>>> ecb70db (Audio processing pipeline)
from src.infrastructure.containers import Container

router = APIRouter()

<<<<<<< HEAD
<<<<<<< HEAD
chunk_counter = defaultdict(int)


@router.post("/upload_audio")
@inject
async def process_audio_chunk(
        session_id: Annotated[str, Header(default_factory=SessionId.generate)],
<<<<<<< HEAD
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
=======
chunk_counter = defaultdict(int)
>>>>>>> ed700fa (Setup whisper speech to text)


@router.post("/upload_audio")
@inject
async def process_audio_chunk(
        session_id: Annotated[str, Header(default_factory=create_session_id)],
=======
>>>>>>> ecb70db (Audio processing pipeline)
        audio_file: UploadFile,
) -> None:
    chunk_counter[session_id] += 1

    content = await audio_file.read()

    with open(f"recordings/{session_id}/chunk-{chunk_counter[session_id]}.mp3", "wb") as f:
        f.write(content)


@router.get("/suggestions/{fname}")
@inject
<<<<<<< HEAD
async def get_suggestions(aa: int = Depends(Provide[Container.int_provider])) -> None:
    print(aa)
>>>>>>> 99a700f (setup dependency injector framework)
=======
async def get_suggestions(
        fname: str,
        speech_to_text: SpeechToText = Depends(Provide[Container.speech_to_text]),
        summarizer: Summarizer = Depends(Provide[Container.summarizer]),
) -> None:
<<<<<<< HEAD
    print(chroma_client.heartbeat())
<<<<<<< HEAD
>>>>>>> 741159d (Setup chromadb)
=======


@router.get("/transcription")
@inject
async def get_transcription(
        speech_to_text: SpeechToText = Depends(Provide[Container.speech_to_text])
) -> str:
    with open("audio.mp3", "rb") as f:
        return speech_to_text.create_transcription(f)
>>>>>>> ed700fa (Setup whisper speech to text)
=======
    print(fname)
    with open(fname, "rb") as f:
        transcript = speech_to_text.create_transcription(f)

    note = summarizer.summarize(transcript)
    print(note)
>>>>>>> ecb70db (Audio processing pipeline)
