from beanie import BeanieObjectId
from pydantic import (
    BaseModel, 
    ConfigDict, 
    Field,
    field_validator
)
from datetime import (
    date, 
    time
)
from typing import Optional

from app.utils.enum import (
    HabitStatus, 
    HabitCategory
)


class HabitBase(BaseModel):
    
    name: str = Field(
        ..., 
        min_length=3, 
        max_length=50,
        description="Habit name (3-50 characters)"
    )
    
    category: HabitCategory = Field(
        ..., 
        description="Category of the habit (e.g., Health, Education, Fitness)"
    )
    
    status: HabitStatus = Field(
        ..., 
        description="Current status of the habit (Active, Paused, Completed, Archived)"
    )
    
    remind_time: time = Field(
        ..., 
        description="Time of day to send reminder (HH:MM:SS format)"
    )
    
    start_date: date = Field(
        ..., 
        description="Date when the habit starts"
    )
    
    end_date: date = Field(
        ..., 
        description="Date when the habit ends (must be after start_date)"
    )

    @field_validator('end_date')
    @classmethod
    def validate_dates(cls, v: date, info) -> date:
        """Ensure end_date is after start_date"""
        if 'start_date' in info.data:
            start = info.data['start_date']
            if v <= start:
                raise ValueError('End date must be after start date')
        return v


class HabitCreate(HabitBase):
    """Model for creating a new habit - inherits all fields from HabitBase"""
    pass


class HabitPrivateOut(HabitBase):
    """Model for returning habit data to the owner (private view)"""
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )


class HabitAdminOut(HabitBase):
    """Model for returning habit data to admin (includes system fields)"""

    _id: BeanieObjectId = Field(
        ..., 
        description="Unique identifier for the habit (MongoDB ObjectId)"
    )
    
    owner_id: BeanieObjectId = Field(
        ..., 
        description="ID of the user who owns this habit"
    )
    
    created_at: date = Field(
        ..., 
        description="Date when the habit was created"
    )
    
    updated_at: date = Field(
        ..., 
        description="Date when the habit was last updated"
    )

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )


class HabitUpdate(BaseModel):
    """Model for updating an existing habit - all fields are optional"""
    
    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=50,
        description="Habit name (3-50 characters)"
    )
    
    status: Optional[HabitStatus] = Field(
        default=None,
        description="Current status of the habit"
    )
    
    remind_time: Optional[time] = Field(
        default=None,
        description="Time of day to send reminder"
    )
    
    start_date: Optional[date] = Field(
        default=None,
        description="Date when the habit starts"
    )
    
    end_date: Optional[date] = Field(
        default=None,
        description="Date when the habit ends"
    )

    @field_validator('end_date')
    @classmethod
    def validate_dates(cls, v: Optional[date], info) -> Optional[date]:
        
        if v is not None and 'start_date' in info.data:
            start = info.data['start_date']
            if start is not None and v <= start:
                raise ValueError('End date must be after start date')
        return v