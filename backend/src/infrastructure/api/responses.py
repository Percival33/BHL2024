import datetime

from pydantic import BaseModel

from src.domain.note import Note
from src.domain.session_id import SessionId


class NoteResponse(BaseModel):
    session_id: str
    title: str
    content: str
    created_at: datetime.datetime

    @classmethod
    def from_note(cls, note: Note) -> "NoteResponse":
        return cls(
            session_id=note.id,
            title=note.title,
            content=note.text,
            created_at=note.created_at
        )
