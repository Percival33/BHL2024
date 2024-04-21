from typing import Mapping, Any

from pymongo import MongoClient

from src.application.note_repository import NoteRepository
from src.domain.meeting_id import MeetingId
from src.domain.note import Note
from src.infrastructure.settings import settings


class MongoNoteRepository(NoteRepository):
    _COLLECTION_NAME = "notes"

    def __init__(self, mongo_client: MongoClient) -> None:
        self._mongo_client = mongo_client
        self._db = self._mongo_client[settings.mongo.db_name]
        self._notes = self._db[self._COLLECTION_NAME]

    def save(self, note: Note) -> None:
        self._notes.update_one(
            {"meeting_id": note.id.value},
            {"$set": note.__dict__()},
            upsert=True,
        )

    def find(self, ids: list[MeetingId] | None = None) -> list[Note]:
        query = {"meeting_name": {"$in": [id_.value for id_ in ids]}} if ids else {}
        notes = self._notes.find(query)

        return [self._map_collection_to_note(note) for note in notes]

    def find_one(self, id_: MeetingId) -> Note | None:
        note = self._notes.find_one({"meeting_id": id_.value})
        if not note:
            return None

        return self._map_collection_to_note(note)

    @staticmethod
    def _map_collection_to_note(collection: Mapping[str, Any]) -> Note:
        return Note(
            meeting_id=MeetingId(collection["meeting_id"]),
            title=collection["title"],
            content=collection["content"],
            created_at=collection["created_at"]
        )
