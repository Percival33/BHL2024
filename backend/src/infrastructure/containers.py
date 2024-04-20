<<<<<<< HEAD
from openai import OpenAI

from src.application.speech_to_text import OpenAISpeechToText
from src.application.summarizer import OpenAISummarizer
from src.infrastructure.chroma.client import get_chroma_client

from dependency_injector import containers, providers

from src.infrastructure.settings import settings

=======
from dependency_injector import containers, providers

>>>>>>> 99a700f (setup dependency injector framework)

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.infrastructure.api.routes",
        ]
    )

<<<<<<< HEAD
    chroma_client = providers.Singleton(get_chroma_client)

    openai_client = providers.Singleton(lambda: OpenAI(api_key=settings.openai_api_key))

    speech_to_text = providers.Factory(OpenAISpeechToText, openai_client)

    summarizer = providers.Factory(OpenAISummarizer, openai_client)

=======
    int_provider = providers.Factory(lambda: 1)
>>>>>>> 99a700f (setup dependency injector framework)
