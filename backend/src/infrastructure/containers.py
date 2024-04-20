from openai import OpenAI

from src.application.meeting_audio_analyzer import MeetingAudioAnalyzer
from src.application.note_repository import JsonFileNoteRepository
from src.application.speech_to_text import OpenAISpeechToText
from src.application.summarizer import OpenAISummarizer
from src.infrastructure.chroma.chroma_embedding_repository import ChromaEmbeddingRepository

from src.infrastructure.chroma.client import get_chroma_client
from src.infrastructure.settings import settings

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.infrastructure.api.routes",
        ]
    )

    chroma_client = providers.Singleton(get_chroma_client)

    openai_client = providers.Singleton(lambda: OpenAI(api_key=settings.openai_api_key))

    speech_to_text = providers.Factory(OpenAISpeechToText, openai_client)

    summarizer = providers.Factory(OpenAISummarizer, openai_client)

    note_repository = providers.Factory(JsonFileNoteRepository)

    embedding_repository = providers.Factory(ChromaEmbeddingRepository, chroma_client)

    meeting_audio_analyzer = providers.Factory(
        MeetingAudioAnalyzer,
        speech_to_text,
        summarizer,
        note_repository,
        embedding_repository
    )
