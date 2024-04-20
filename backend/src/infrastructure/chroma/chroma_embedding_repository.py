import chromadb

from src.application.embedding_repository import EmbeddingRepository
from src.domain.note import Note
from src.domain.session_id import SessionId


class ChromaEmbeddingRepository(EmbeddingRepository):
    _COLLECTION_NAME = "notes"

    def __init__(self, chroma_client: chromadb.ClientAPI) -> None:
        self._client = chroma_client
        self._collection = self._client.get_or_create_collection(self._COLLECTION_NAME)

    def save(self, note: Note) -> None:
        self._collection.add(
            documents=note.text,
            ids=note.id.value,
        )

    def find_similar(self, note: Note, n_results: int = 3) -> list[SessionId]:
        results = self._collection.query(
            query_texts=note.text,
            n_results=n_results
        )
        print(results)
        return [SessionId(result) for result in results["ids"][0]]
