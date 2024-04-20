import abc

from src.domain.note import Note
from src.domain.meeting_id import MeetingId


class EmbeddingRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, note: Note) -> None:
        pass

    @abc.abstractmethod
    def find_similar(self, note: Note) -> list[MeetingId]:
        pass
