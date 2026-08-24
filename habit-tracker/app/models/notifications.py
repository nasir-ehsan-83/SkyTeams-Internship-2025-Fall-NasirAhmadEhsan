from typing import List
from datetime import (
    datetime, 
    timezone
)
from pymongo import (
    ASCENDING, 
    IndexModel
)
from beanie import (
    Document, 
    BeanieObjectId, 
    before_event, 
    Replace, 
    Update
)
from pydantic import Field




class Notification(Document):
    
    owner_id:       BeanieObjectId  = Field(..., description = "User ID")
    habit_id:       BeanieObjectId  = Field(..., description = "Habit ID")
    time:           str             = Field(..., description = "Reminder time in HH:MM format")
    days:           List[int]       = Field(default = [0, 1, 2, 3, 4], description = "Days of week (0=Monday to 6=Sunday)")
    type:           str             = Field(default = "reminder", description = "Notification type")
    next_trigger:   datetime        = Field(..., description = "Next trigger time")
    is_active:      bool            = Field(default = True, description = "Whether schedule is active")
    title:          str | None      = Field(default = None, description = "Notification title")
    message:        str | None      = Field(default = None, description = "Notification message")
    sent_at:        datetime | None = Field(default = None, description = "Sent timestamp")
    status:         str             = Field(default = "pending", description = "Delivery status (pending/delivered/failed)")
    
    created_at:     datetime        = Field(default_factory = lambda: datetime.now(timezone.utc))
    updated_at:     datetime        = Field(default_factory = lambda: datetime.now(timezone.utc))
    
    @before_event([Replace, Update])
    async def update_timestamp(self) -> None:
        self.updated_at = datetime.now(timezone.utc)
    
    class Settings:
        name = "notifications"
        indexes = [
            IndexModel([("owner_id", ASCENDING), ("habit_id", ASCENDING)]),
            IndexModel([("next_trigger", ASCENDING)]),
            IndexModel([("is_active", ASCENDING)]),
            IndexModel([("owner_id", ASCENDING), ("is_active", ASCENDING)])
        ]



