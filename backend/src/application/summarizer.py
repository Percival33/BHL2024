import abc
import concurrent.futures

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
    as accurately as possible. Use no more than 5 words. Use English language."""

    _ABSTRACT_SYS_PROMPT = """You are a highly skilled AI trained in language comprehension and summarization. 
    I would like you to read the following text and summarize it into a concise abstract paragraph. 
    Aim to retain the most important points, providing a coherent and readable summary that could help a person 
    understand the main points of the discussion without needing to read the entire text. 
    Please avoid unnecessary details or tangential points."""

    _MARKDOWN_SYS_PROMPT = """You are a highly skilled AI trained in converting texts to a markdown format.
    Convert the following text to a valid markdown. Extract headers, paragraphs, bullet points and format them accordingly.
    Keep all of the original content."""

    def __init__(self, client: OpenAI, model_name: str = "gpt-4"):
        self._client = client
        self._model_name = model_name

    def summarize(self, meeting_id: MeetingId, text: str) -> Note:
        with concurrent.futures.ThreadPoolExecutor() as exe:
            title_future = exe.submit(self._get_title, text)
            abstract_future = exe.submit(self._get_abstract, text)

            title = title_future.result()
            abstract = abstract_future.result()

        markdown = self._get_markdown_abstract(abstract)

        return Note(meeting_id, title, abstract, markdown)

    def _get_title(self, text: str) -> str:
        title = self._client.chat.completions.create(
            model=self._model_name,
            temperature=0,
            messages=[
                {"role": "system", "content": self._TITLE_SYS_PROMPT},
                {"role": "user", "content": text}
            ]
        ).choices[0].message.content

        return title.replace("\"", "")

    def _get_abstract(self, text: str) -> str:
        return self._client.chat.completions.create(
            model=self._model_name,
            temperature=0,
            messages=[
                {"role": "system", "content": self._ABSTRACT_SYS_PROMPT},
                {"role": "user", "content": text}
            ]
        ).choices[0].message.content

    def _get_markdown_abstract(self, text: str) -> str:
        return self._client.chat.completions.create(
            model=self._model_name,
            temperature=0,
            messages=[
                {"role": "system", "content": self._MARKDOWN_SYS_PROMPT},
                {"role": "user", "content": text}
            ]
        ).choices[0].message.content
