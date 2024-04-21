from pymongo import MongoClient


from src.application.note_repository import NoteRepository
from src.domain.meeting_id import MeetingId
from src.domain.note import Note


class MongoNoteRepository(NoteRepository):
    def __init__(self) -> None:
        pass

    def save(self, note: Note) -> None:
        pass

    def find(self, ids: list[MeetingId] | None = None) -> list[Note]:
        pass

    def find_one(self, id_: MeetingId) -> Note | None:
        pass
