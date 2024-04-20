from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ChromaSettings(BaseModel):
    host: str
    port: int


class Settings(BaseSettings):
    host: str
    port: int
    debug_mode: bool
<<<<<<< HEAD
<<<<<<< HEAD
    openai_api_key: str
=======
>>>>>>> 741159d (Setup chromadb)
=======
    openai_api_key: str
>>>>>>> ed700fa (Setup whisper speech to text)
    chroma: ChromaSettings

    model_config = SettingsConfigDict(
        env_file=(".env",), env_nested_delimiter="__"
    )


settings = Settings()
