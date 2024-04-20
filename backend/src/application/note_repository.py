import abc
import os
import datetime
import json

from src.domain.note import Note
from src.domain.meeting_id import MeetingId


class NoteRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, note: Note) -> None:
        pass

    @abc.abstractmethod
    def find(self, ids: list[MeetingId] | None = None) -> list[Note]:
        pass

    @abc.abstractmethod
    def find_one(self, id_: MeetingId) -> Note | None:
        pass


class JsonFileNoteRepository(NoteRepository):
    _db: dict[str, Note] = {}
    _db_file = "db.json"

    def __init__(self) -> None:
        if not os.path.exists(self._db_file):
            self._create_db_file()

        if not self._db:
            self._load_db_dump()

    def _create_db_file(self) -> None:
        with open(self._db_file, "w"):
            pass

    def _load_db_dump(self) -> None:
        with open(self._db_file, "r") as f:
            try:
                for row in json.load(f):
                    self._db[row["id"]] = Note(
                        meeting_id=MeetingId(row["id"]),
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

    def find(self, ids: list[MeetingId] | None = None) -> list[Note]:
        if ids is None:
            return list(self._db.values())

        return [self._db[id_.value] for id_ in ids]

    def find_one(self, id_: MeetingId) -> Note | None:
        return self._db.get(id_.value)
