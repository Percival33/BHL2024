import uuid

from src.domain.exceptions import DomainException


class InvalidMeetingId(DomainException):
    def __init__(self, value: str) -> None:
        super().__init__(f"'{value}' is not a valid meeting id")


class MeetingId:
    def __init__(self, value: str) -> None:
        try:
            uuid.UUID(value)
        except ValueError:
            raise InvalidMeetingId(value)

        self._value = value

    @property
    def value(self) -> str:
        return self._value

    @classmethod
    def generate(cls) -> "MeetingId":
        return cls(str(uuid.uuid4()))

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return self._value
