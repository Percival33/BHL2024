from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.domain.exceptions import DomainException
from src.infrastructure.api.error_handlers import application_error_handler
from src.infrastructure.api.routes import router
from src.infrastructure.containers import Container
origins = [
    "http://localhost",
    "http://localhost:3000",
]

container = Container()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.container = container

app.include_router(router)

app.add_exception_handler(DomainException, application_error_handler)
