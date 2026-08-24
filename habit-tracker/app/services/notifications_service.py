from datetime import (
    datetime, 
    timedelta
)
from fastapi import (
    HTTPException, 
    status
)
from beanie import BeanieObjectId

from app.models.notifications import NotificationSettings
from app.schemas import (
    ScheduleCreate,
    ScheduleOut,
    MessageOut, 
    ScheduleUpdate
)
from app.models import (
    Habit, 
    Notification
)
from app.config import logger
from app.schemas.notifications import SettingsOut, SettingsUpdate




async def create_schedule_service(
    owner_id:       BeanieObjectId,
    schedule_in:    ScheduleCreate
) -> ScheduleOut:
    
    try:
        habit = await Habit.get(schedule_in.habit_id)
       
        if not habit:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Habit not found"
            )
        
        now = datetime.now()
        trigger_time = datetime.combine(now.date(), datetime.strptime(schedule_in.time, "%H:%M").time())
        
        if trigger_time <= now:
            trigger_time += timedelta(days=1)
        
        notification = Notification(
            owner_id = owner_id,
            habit_id = schedule_in.habit_id,
            time = schedule_in.time,
            days = schedule_in.days,
            type = schedule_in.type,
            next_trigger = trigger_time,
            is_active = True
        )
        
        await notification.insert() # type: ignore
        
        return ScheduleOut(
            schedule_id = notification.id, # type: ignore
            habit_id = notification.habit_id,
            time = notification.time,
            days = notification.days,
            type = notification.type,
            next_trigger = notification.next_trigger,
            is_active = notification.is_active,
            created_at = notification.created_at
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in create_schedule_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )




async def update_schedule_service(
    owner_id:       BeanieObjectId,
    schedule_id:    BeanieObjectId,
    schedule_in:    ScheduleUpdate
) -> MessageOut:
    
    try:
        notification = await Notification.find_one({
            "_id": schedule_id,
            "owner_id": owner_id
        })
        
        if not notification:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Schedule not found"
            )
        
        if schedule_in.time is not None:
            notification.time = schedule_in.time
            
            now = datetime.now()
            trigger_time = datetime.combine(now.date(), datetime.strptime(schedule_in.time, "%H:%M").time())
            
            if trigger_time <= now:
                trigger_time += timedelta(days=1)
            
            notification.next_trigger = trigger_time
        
        if schedule_in.days is not None:
            notification.days = schedule_in.days
        
        if schedule_in.is_active is not None:
            notification.is_active = schedule_in.is_active
        
        await notification.save() # type: ignore
        
        return MessageOut(
            message = "Schedule updated successfully"
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in update_schedule_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )




async def delete_schedule_service(
    owner_id:       BeanieObjectId,
    schedule_id:    BeanieObjectId
) -> MessageOut:
    
    try:
        
        notification = await Notification.find_one({
            "_id": schedule_id,
            "owner_id": owner_id
        })
        
        if not notification:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Schedule not found"
            )
        
        await notification.delete() # type: ignore
        
        return MessageOut(
            message = "Schedule deleted successfully"
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in delete_schedule_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )




async def get_settings_service(
    owner_id:   BeanieObjectId
) -> SettingsOut:
    
    try:
        settings = await NotificationSettings.find_one({"owner_id": owner_id})
        
        if not settings:
            return SettingsOut(
                push_enabled = True,
                email_enabled = False,
                reminder_time = None,
                reminder_days = None
            )
        
        return SettingsOut(
            push_enabled = settings.push_enabled,
            email_enabled = settings.email_enabled,
            reminder_time = settings.reminder_time,
            reminder_days = settings.reminder_days
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in get_settings_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )




async def update_settings_service(
    owner_id:       BeanieObjectId,
    settings_in:    SettingsUpdate
) -> MessageOut:
    
    try:
        settings = await NotificationSettings.find_one({"owner_id": owner_id})
        
        if not settings:
            settings = NotificationSettings(owner_id = owner_id)
        
        if settings_in.push_enabled is not None:
            settings.push_enabled = settings_in.push_enabled
        
        if settings_in.email_enabled is not None:
            settings.email_enabled = settings_in.email_enabled
        
        if settings_in.reminder_time is not None:
            settings.reminder_time = settings_in.reminder_time
        
        if settings_in.reminder_days is not None:
            settings.reminder_days = settings_in.reminder_days
        
        await settings.save() # type: ignore
        
        return MessageOut(
            message = "Settings updated successfully"
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in update_settings_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )
