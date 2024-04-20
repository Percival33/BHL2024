import uvicorn
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.infrastructure.containers import Container

router = APIRouter()


@router.post("/summarize_chunk")
@inject
async def summarize_audio_chunk() -> None:
    pass


@router.get("/suggestions")
@inject
async def get_suggestions(aa: int = Depends(Provide[Container.int_provider])) -> None:
    print(aa)
