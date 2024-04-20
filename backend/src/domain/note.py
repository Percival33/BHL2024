import datetime

from src.domain.meeting_id import MeetingId


class Note:
    def __init__(
        self,
        meeting_id: MeetingId,
        title: str,
        content: str,
        created_at: datetime.datetime = datetime.datetime.now(),
    ) -> None:
        self._meeting_id = meeting_id
        self._title = title
        self._content = content
        self._created_at = created_at

    @property
    def id(self) -> MeetingId:
        return self._meeting_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def text(self) -> str:
        return self._content

    @property
    def created_at(self) -> datetime.datetime:
        return self._created_at

    def __dict__(self) -> dict:
        return {
            "id": self._meeting_id.value,
            "title": self._title,
            "content": self._content,
            "created_at": self._created_at,
        }

    def __str__(self) -> str:
        return f"{self.title}: {self.text}"
