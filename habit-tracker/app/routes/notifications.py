from typing import Annotated
from fastapi import (
    APIRouter, 
    Depends,
    Body
)

from app.dependencies import get_current_user
from app.schemas import (
    ScheduleCreate,
    ScheduleOut,
    TokenData
)
from app.services.notifications_service import (
    create_schedule_service
)


router: APIRouter = APIRouter(
    prefix = '/api/notifications',
    tags = ["Notifications"],
    dependencies = [
        Depends(get_current_user)
    ]
)


@router.post(
    '/schedule',
    response_model = ScheduleOut,
    status_code = 201
)
async def create_schedule_route(
    current_user:       Annotated[TokenData, Depends(get_current_user)],
    schedule_in:        Annotated[ScheduleCreate, Body(...)]
) -> ScheduleOut:
    return await create_schedule_service(current_user.id, schedule_in)
