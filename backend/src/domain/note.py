import datetime

from src.domain.session_id import SessionId


class Note:
    def __init__(
        self,
        session_id: SessionId,
        title: str,
        content: str,
        created_at: datetime.datetime = datetime.datetime.now(),
    ) -> None:
        self._session_id = session_id
        self._title = title
        self._content = content
        self._created_at = created_at

    @property
    def id(self) -> SessionId:
        return self._session_id

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
            "id": self._session_id.value,
            "title": self._title,
            "content": self._content,
            "created_at": self._created_at,
        }

    def __str__(self) -> str:
        return f"{self.title}: {self.text}"
