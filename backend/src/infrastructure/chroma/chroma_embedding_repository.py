import logging

import chromadb
import chromadb.utils.embedding_functions as embedding_functions

from src.application.embedding_repository import EmbeddingRepository, SimilarNote
from src.domain.note import Note
from src.domain.meeting_id import MeetingId
from src.infrastructure.settings import settings

logger = logging.getLogger(__name__)


class ChromaEmbeddingRepository(EmbeddingRepository):
    _COLLECTION_NAME = "notes"

    def __init__(
        self,
        chroma_client: chromadb.ClientAPI,
        model_name: str = "text-embedding-3-large",
    ) -> None:
        self._client = chroma_client
        self._collection = self._client.get_or_create_collection(
            self._COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )

    def save(self, note: Note) -> None:
        logger.info("Saving embeddings for meeting %s", note.id)

        self._collection.upsert(
            documents=note.text,
            ids=note.id.value,
        )

    def find_similar(self, note: Note, n_results: int = 4) -> list[SimilarNote]:
        logger.info("Retrieving similar notes for meeting %s", note.id)

        results = self._collection.query(
            query_texts=note.text,
            n_results=n_results
        )

        normalized_results = [
            SimilarNote(
                meeting_id=MeetingId(meeting_id),
                similarity=self._normalize_cosine_similarity(cos_distance)
            ) for meeting_id, cos_distance in zip(results["ids"][0], results["distances"][0])
        ]

        logger.info("Meeting %s, similar notes: %s", note.id, normalized_results)
        return normalized_results

    @staticmethod
    def _normalize_cosine_similarity(cos_distance: float) -> float:
        return (2 - cos_distance) / 2
