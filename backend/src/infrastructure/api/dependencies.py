from typing import Annotated

from fastapi import Header

from src.domain.session_id import SessionId


def provide_session_id(session_id: Annotated[str | None, Header()] = None) -> SessionId:
    return SessionId(session_id) if session_id else SessionId.generate()
