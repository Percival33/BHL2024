from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ChromaSettings(BaseModel):
    host: str
    port: int


class MongoSettings(BaseModel):
    host: str
    port: int
    db_name: str


class Settings(BaseSettings):
    host: str
    port: int
    debug_mode: bool
    openai_api_key: str
    openai_api_key: str
    frontend_base_url: str
    chroma: ChromaSettings
    mongo: MongoSettings

    model_config = SettingsConfigDict(
        env_file=(".env",), env_nested_delimiter="__"
    )


settings = Settings()
