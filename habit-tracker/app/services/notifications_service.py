from datetime import (
    datetime, 
    timedelta
)
from fastapi import (
    HTTPException, 
    status
)
from beanie import BeanieObjectId

from app.schemas import (
    ScheduleCreate,
    ScheduleOut
)
from app.models import (
    Habit, 
    Notification
)
from app.config import logger




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

