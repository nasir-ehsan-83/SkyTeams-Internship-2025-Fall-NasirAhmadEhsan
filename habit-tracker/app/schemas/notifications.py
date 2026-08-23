from typing import List
from pydantic import (
    BaseModel, 
    Field, 
    field_validator
)
from beanie import BeanieObjectId




class ScheduleCreate(BaseModel):
    habit_id:   BeanieObjectId  = Field(..., description = "Habit ID to set reminder for")
    time:       str             = Field(..., description = "Reminder time in HH:MM format", pattern = r"^([01]\d|2[0-3]):([0-5]\d)$")
    days:       List[int]       = Field(..., description = "Days of week (0=Monday to 6=Sunday)", min_length = 1, max_length = 7)
    type:       str             = Field(default = "reminder", description = "Notification type")
    
    @field_validator('days')
    @classmethod
    def validate_days(cls, v: List[int]) -> List[int]:
        for day in v:
            if not 0 <= day <= 6:
                raise ValueError('Days must be between 0 (Monday) and 6 (Sunday)')
        
        return sorted(set(v))