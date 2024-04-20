<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from openai import OpenAI

from src.application.speech_to_text import OpenAISpeechToText
from src.application.summarizer import OpenAISummarizer
=======
import chromadb

>>>>>>> 741159d (Setup chromadb)
=======
from openai import OpenAI

from src.application.speech_to_text import OpenAISpeechToText
>>>>>>> ed700fa (Setup whisper speech to text)
from src.infrastructure.chroma.client import get_chroma_client

from dependency_injector import containers, providers

from src.infrastructure.settings import settings

<<<<<<< HEAD
=======
from dependency_injector import containers, providers

>>>>>>> 99a700f (setup dependency injector framework)
=======
>>>>>>> ed700fa (Setup whisper speech to text)

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.infrastructure.api.routes",
        ]
    )

<<<<<<< HEAD
<<<<<<< HEAD
    chroma_client = providers.Singleton(get_chroma_client)

    openai_client = providers.Singleton(lambda: OpenAI(api_key=settings.openai_api_key))

    speech_to_text = providers.Factory(OpenAISpeechToText, openai_client)

<<<<<<< HEAD
    summarizer = providers.Factory(OpenAISummarizer, openai_client)

=======
    int_provider = providers.Factory(lambda: 1)
>>>>>>> 99a700f (setup dependency injector framework)
=======
    chroma_client = providers.Singleton(get_chroma_client)
>>>>>>> 741159d (Setup chromadb)
=======
>>>>>>> ed700fa (Setup whisper speech to text)
