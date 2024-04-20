from fastapi import Request, Response, status
from fastapi.responses import JSONResponse


def application_error_handler(request: Request, err: Exception) -> Response:
    return JSONResponse(
        content={"detail": str(err)},
        status_code=status.HTTP_400_BAD_REQUEST,
    )
