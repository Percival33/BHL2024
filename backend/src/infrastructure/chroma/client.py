import chromadb

from src.infrastructure.settings import settings


def get_chroma_client() -> chromadb.ClientAPI:
    client = chromadb.HttpClient(
        host=settings.chroma.host,
        port=settings.chroma.port,
        settings=chromadb.Settings(allow_reset=True, anonymized_telemetry=False),
    )

    return client
