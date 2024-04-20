import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="src.infrastructure.api.app:app",
        host="localhost",
        port=8000,
        reload=True,
    )
