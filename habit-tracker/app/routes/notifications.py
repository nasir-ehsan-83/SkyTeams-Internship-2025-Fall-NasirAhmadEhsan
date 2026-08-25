from typing import Annotated
from beanie import BeanieObjectId
from fastapi import (
    APIRouter, 
    Depends,
    Body,
    Path,
    Query
)

from app.dependencies import get_current_user
from app.schemas import (
    ScheduleCreate,
    ScheduleOut,
    TokenData,
    MessageOut,
    ScheduleUpdate,
    SettingsOut,
    SettingsUpdate,
    TestNotificationIn, 
    TestNotificationOut,
    NotificationHistoryOut
)
from app.services.notifications_service import (
    create_schedule_service,
    update_schedule_service,
    delete_schedule_service,
    get_settings_service,
    update_settings_service,
    send_test_notification_service,
    get_notification_history_service
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




@router.get(
    '/settings',
    response_model = SettingsOut
)
async def get_settings_route(
    current_user:   Annotated[TokenData, Depends(get_current_user)]
) -> SettingsOut:
    
    return await get_settings_service(current_user.id)




@router.put(
    '/settings',
    response_model = MessageOut
)
async def update_settings_route(
    current_user:   Annotated[TokenData, Depends(get_current_user)],
    settings_in:    Annotated[SettingsUpdate, Body(...)]
) -> MessageOut:
    
    return await update_settings_service(current_user.id, settings_in)




@router.post(
    '/test',
    response_model = TestNotificationOut
)
async def send_test_notification_route(
    current_user:   Annotated[TokenData, Depends(get_current_user)],
    test_in:        Annotated[TestNotificationIn, Body(...)]
) -> TestNotificationOut:
    
    return await send_test_notification_service(current_user.id, test_in)




@router.get(
    '/history',
    response_model = NotificationHistoryOut
)
async def get_notification_history_route(
    current_user:   Annotated[TokenData, Depends(get_current_user)],
    limit:          Annotated[int, Query(ge = 1, le = 100)] = 20
) -> NotificationHistoryOut:
    
    return await get_notification_history_service(current_user.id, limit)