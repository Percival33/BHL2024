from fastapi import FastAPI

from src.infrastructure.api.routes import router
from src.infrastructure.containers import Container

container = Container()

app = FastAPI()

app.container = container

app.include_router(router)
