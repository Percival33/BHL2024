import datetime

from pydantic import BaseModel, computed_field

from src.domain.note import Note
from src.domain.meeting_id import MeetingId
from src.infrastructure.settings import settings


class NoteResponse(BaseModel):
    meeting_id: str
    title: str
    content: str
    created_at: datetime.datetime

    @computed_field
    @property
    def uri(self) -> str:
        return f"{settings.frontend_base_url}/note/{self.meeting_id}"

    @classmethod
    def from_note(cls, note: Note) -> "NoteResponse":
        return cls(
            meeting_id=note.id.value,
            title=note.title,
            content=note.text,
            created_at=note.created_at
        )


class UploadAudioResponse(BaseModel):
    meeting_id: str
