import uuid
import os

from src.application.embedding_repository import EmbeddingRepository
from src.application.note_repository import NoteRepository
from src.application.speech_to_text import SpeechToText
from src.application.summarizer import Summarizer
from src.domain.meeting_id import MeetingId
import time

class MeetingAudioAnalyzer:
    _RECORDINGS_DIR = "recordings"

    def __init__(
            self,
            speech_to_text: SpeechToText,
            summarizer: Summarizer,
            note_repository: NoteRepository,
            embedding_repository: EmbeddingRepository,
    ) -> None:
        self._speech_to_text = speech_to_text
        self._summarizer = summarizer
        self._note_repository = note_repository
        self._embedding_repository = embedding_repository

        self._create_temporary_recordings_directory()

    def process_meeting_audio(self, meeting_id: MeetingId, audio: bytes) -> None:
        s = time.time()
        temp_file = os.path.join(self._RECORDINGS_DIR, f"{str(uuid.uuid4())}.mp3")

        with open(temp_file, "wb+") as f_handle:
            f_handle.write(audio)
            f_handle.seek(0)
            transcript = self._speech_to_text.create_transcription(f_handle)

        print(time.time() - s)

        self._process_audio_transcript(meeting_id, transcript)
        self._cleanup_temporary_files(temp_file)

        e = time.time()

        print(e-s)

    def _create_temporary_recordings_directory(self) -> None:
        if not os.path.exists(self._RECORDINGS_DIR):
            os.makedirs(self._RECORDINGS_DIR)

    def _process_audio_transcript(self, meeting_id: MeetingId, transcript: str) -> None:
        note = self._summarizer.summarize(meeting_id, transcript)

        self._note_repository.save(note)
        self._embedding_repository.save(note)

    @staticmethod
    def _cleanup_temporary_files(file_path: str) -> None:
        if os.path.exists(file_path):
            os.remove(file_path)
