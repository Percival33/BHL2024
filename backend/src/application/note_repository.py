import abc
import os
import datetime
import json

from src.domain.note import Note
from src.domain.session_id import SessionId


class NoteRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, note: Note) -> None:
        pass

    @abc.abstractmethod
    def find(self, ids: list[SessionId] | None = None) -> list[Note]:
        pass

    @abc.abstractmethod
    def find_one(self, id_: SessionId) -> Note | None:
        pass


class InMemoryNoteRepository(NoteRepository):
    _db: dict[str, Note] = {}
    _db_file = "db.json"

    def __init__(self) -> None:
        if not self._db and os.path.exists(self._db_file):
            self._load_db_dump()

    def _load_db_dump(self) -> None:
        with open(self._db_file, "r") as f:
            try:
                for row in json.load(f):
                    self._db[row["id"]] = Note(
                        session_id=SessionId(row["id"]),
                        title=row["title"],
                        content=row["content"],
                        created_at=datetime.datetime.fromisoformat(row["created_at"]),
                    )
            except json.decoder.JSONDecodeError:  # silent
                pass

    def save(self, note: Note) -> None:
        self._db[note.id.value] = note
        self._dump_db()

    def _dump_db(self) -> None:
        dump = [note.__dict__() for note in self._db.values()]

        with open(self._db_file, "w") as f:
            json.dump(dump, f, default=str)

    def find(self, ids: list[SessionId] | None = None) -> list[Note]:
        if ids is None:
            return list(self._db.values())

        ids_map = set(id_.value for id_ in ids)

        results = []
        for id_, note in self._db.items():
            if id_ in ids_map:
                results.append(note)

        return list(self._db.values())

    def find_one(self, id_: SessionId) -> Note | None:
        return self._db.get(id_.value)
