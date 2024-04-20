import uuid


class SessionId:
    def __init__(self, value: str) -> None:
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    @classmethod
    def generate(cls) -> "SessionId":
        return cls(str(uuid.uuid4()))
