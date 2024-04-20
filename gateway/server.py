import random
import uvicorn
from fastapi import FastAPI, UploadFile, Header
from fastapi.responses import JSONResponse
import uuid

app = FastAPI()

recording_cnt = {}


@app.get("/matching_notes")
async def process_audio_chunk() -> list[str]:
    results = [f"Note suggestion {random.randint(1, 1000)}" for _ in range(10)]

    return results


@app.post("/upload_audio")
async def upload_audio_chunk(file: UploadFile, sessionId: str = Header(None)) -> JSONResponse:
    if sessionId is None:
        print("new user connected")
        sessionId = uuid.uuid1()
    print(f"Uploaded: {file.filename}")
    recording_cnt[sessionId] = recording_cnt.get(sessionId, 0) + 1
    content = await file.read()
    with open(f"recordings/chunk-{recording_cnt.get(sessionId)}-{sessionId}.mp3", "wb") as f:
        f.write(content)

    return JSONResponse(headers={'sessionId': str(sessionId)}, status_code=200, content="OK")


if __name__ == "__main__":
    uvicorn.run(
        app="server:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
