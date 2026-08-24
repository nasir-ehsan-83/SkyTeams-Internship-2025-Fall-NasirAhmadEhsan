from typing import Annotated
from beanie import BeanieObjectId
from fastapi import (
    APIRouter, 
    Depends,
    Body,
    Path
)

from app.dependencies import get_current_user
from app.schemas import (
    ScheduleCreate,
    ScheduleOut,
    TokenData,
    MessageOut,
    ScheduleUpdate
)
from app.services.notifications_service import (
    create_schedule_service,
    update_schedule_service,
    delete_schedule_service
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




@router.put(
    '/schedule/{schedule_id}',
    response_model = MessageOut
)
async def update_schedule_route(
    current_user:       Annotated[TokenData, Depends(get_current_user)],
    schedule_id:        Annotated[BeanieObjectId, Path(...)],
    schedule_in:        Annotated[ScheduleUpdate, Body(...)]
) -> MessageOut:
    
    return await update_schedule_service(current_user.id, schedule_id, schedule_in)




@router.delete(
    '/schedule/{schedule_id}',
    response_model = MessageOut
)
async def delete_schedule_route(
    current_user:   Annotated[TokenData, Depends(get_current_user)],
    schedule_id:    Annotated[BeanieObjectId, Path(...)]
) -> MessageOut:
    
    return await delete_schedule_service(current_user.id, schedule_id)
