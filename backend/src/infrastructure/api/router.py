import uvicorn
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/suggestions")
async def get_suggestions() -> None:
    pass


@app.post("/summarize_chunk")
async def summarize_audio_chunk() -> None:
    pass
