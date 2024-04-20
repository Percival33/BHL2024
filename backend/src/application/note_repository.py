import abc

from src.domain.note import Note
from src.domain.session_id import SessionId


class NoteRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, note: Note) -> None:
        pass

    @abc.abstractmethod
    def find(self) -> list[Note]:
        pass

    @abc.abstractmethod
    def find_one(self, id_: SessionId) -> Note | None:
        pass


class InMemoryNoteRepository(NoteRepository):
    _db: dict[str, Note] = {}

    def save(self, note: Note) -> None:
        self._db[note.id.value] = note

    def find(self) -> list[Note]:
        return list(self._db.values())

    def find_one(self, id_: SessionId) -> Note | None:
        return self._db.get(id_.value)
