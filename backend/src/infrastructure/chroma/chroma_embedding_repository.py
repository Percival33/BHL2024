import chromadb

from src.application.embedding_repository import EmbeddingRepository, SimilarNote
from src.domain.note import Note
from src.domain.meeting_id import MeetingId


class ChromaEmbeddingRepository(EmbeddingRepository):
    _COLLECTION_NAME = "notes"

    def __init__(self, chroma_client: chromadb.ClientAPI) -> None:
        self._client = chroma_client
        self._collection = self._client.get_or_create_collection(
            self._COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )

    def save(self, note: Note) -> None:
        self._collection.upsert(
            documents=note.text,
            ids=note.id.value,
        )

    def find_similar(self, note: Note, n_results: int = 4) -> list[SimilarNote]:
        results = self._collection.query(
            query_texts=note.text,
            n_results=n_results
        )

        return [
            SimilarNote(
                meeting_id=MeetingId(meeting_id),
                similarity=self._normalize_cosine_similarity(cos_distance)
            ) for meeting_id, cos_distance in zip(results["ids"][0], results["distances"][0])
        ]

    @staticmethod
    def _normalize_cosine_similarity(cos_distance: float) -> float:
        return (2 - cos_distance) / 2
