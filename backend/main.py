import uvicorn

<<<<<<< HEAD
<<<<<<< HEAD
from src.infrastructure.settings import settings


if __name__ == "__main__":
    uvicorn.run(
        app="src.infrastructure.api.app:app",
        host=settings.host,
        port=settings.port,
=======
if __name__ == "__main__":
    uvicorn.run(
        app="src.infrastructure.api.app:app",
        host="localhost",
        port=8000,
>>>>>>> 99a700f (setup dependency injector framework)
=======
from src.infrastructure.settings import settings


if __name__ == "__main__":
    uvicorn.run(
        app="src.infrastructure.api.app:app",
        host=settings.host,
        port=settings.port,
>>>>>>> 741159d (Setup chromadb)
        reload=True,
    )
