import abc
from dataclasses import dataclass

from pydantic import BaseModel

from src.domain.note import Note
from src.domain.meeting_id import MeetingId


@dataclass
class SimilarNote:
    meeting_id: MeetingId
    similarity: float


class EmbeddingRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, note: Note) -> None:
        pass

    @abc.abstractmethod
    def find_similar(self, note: Note) -> list[SimilarNote]:
        pass
