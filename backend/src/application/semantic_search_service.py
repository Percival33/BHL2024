import abc

from src.domain.note import Note


class SemanticSearchService(abc.ABC):
    @abc.abstractmethod
    def save(self, note: Note) -> None:
        pass

    def find_simmilar(self, note: Note):
        pass
