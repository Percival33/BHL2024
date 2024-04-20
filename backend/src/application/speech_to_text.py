import abc
import typing

import openai
from openai import OpenAI


class SpeechToText(abc.ABC):
    @abc.abstractmethod
    def create_transcription(self, f_handle: typing.BinaryIO) -> str:
        pass


class OpenAISpeechToText(SpeechToText):
    def __init__(self, client: OpenAI, model_name: str = "whisper-1"):
        self._client = client
        self._model_name = model_name

    def create_transcription(self, f_handle: typing.BinaryIO) -> str:
        transcription = self._client.audio.transcriptions.create(
            model=self._model_name,
            file=f_handle
        )

        return transcription.text
