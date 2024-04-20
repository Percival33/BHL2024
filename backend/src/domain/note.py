class Note:
    def __init__(self, title: str, content: str) -> None:
        self._title = title
        self._content = content

    @property
    def title(self) -> str:
        return self._title

    @property
    def text(self) -> str:
        return self._content

    def __str__(self) -> str:
        return f"{self.title}: {self.text}"
