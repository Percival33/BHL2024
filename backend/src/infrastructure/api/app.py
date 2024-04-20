from fastapi import FastAPI

from src.domain.exceptions import DomainException
from src.infrastructure.api.error_handlers import application_error_handler
from src.infrastructure.api.routes import router
from src.infrastructure.containers import Container

container = Container()

app = FastAPI()

app.container = container

app.include_router(router)

app.add_exception_handler(DomainException, application_error_handler)
