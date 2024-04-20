from typing import Annotated

from fastapi import Header

from src.domain.meeting_id import MeetingId


def provide_meeting_id(meeting_id: Annotated[str | None, Header()] = None) -> MeetingId:
    return MeetingId(meeting_id) if meeting_id else MeetingId.generate()
