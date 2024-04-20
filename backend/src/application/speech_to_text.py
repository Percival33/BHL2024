import abc
import typing

<<<<<<< HEAD
<<<<<<< HEAD
=======
import openai
>>>>>>> ed700fa (Setup whisper speech to text)
=======
>>>>>>> ecb70db (Audio processing pipeline)
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
