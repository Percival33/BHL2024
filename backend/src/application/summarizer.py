import abc

from openai import OpenAI

from src.domain.note import Note
from src.domain.meeting_id import MeetingId


class Summarizer(abc.ABC):
    @abc.abstractmethod
    def summarize(self, meeting_id: MeetingId, text: str) -> Note:
        pass


class OpenAISummarizer(Summarizer):
    _TITLE_SYS_PROMPT = """You are a highly skilled AI trained in creating titles for text. 
    I would like you to read the following text and create a title, which matches what the text is about
    as accurately as possible. Use no more than 5 words."""

    _ABSTRACT_SYS_PROMPT = """You are a highly skilled AI trained in language comprehension and summarization. 
    I would like you to read the following text and summarize it into a concise abstract paragraph. 
    Aim to retain the most important points, providing a coherent and readable summary that could help a person 
    understand the main points of the discussion without needing to read the entire text. 
    Please avoid unnecessary details or tangential points."""

    def __init__(self, client: OpenAI, model_name: str = "gpt-4"):
        self._client = client
        self._model_name = model_name

    def summarize(self, meeting_id: MeetingId, text: str) -> Note:
        title = self._get_title(text)
        abstract = self._get_abstract(text)

        return Note(meeting_id, title, abstract)

    def _get_title(self, text: str) -> str:
        return self._client.chat.completions.create(
            model=self._model_name,
            temperature=0,
            messages=[
                {"role": "system", "content": self._TITLE_SYS_PROMPT},
                {"role": "user", "content": text}
            ]
        ).choices[0].message.content

    def _get_abstract(self, text: str) -> str:
        return self._client.chat.completions.create(
            model=self._model_name,
            temperature=0,
            messages=[
                {"role": "system", "content": self._ABSTRACT_SYS_PROMPT},
                {"role": "user", "content": text}
            ]
        ).choices[0].message.content
