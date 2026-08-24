from typing import (
    Any, 
    List
)
import datetime 
from beanie import BeanieObjectId
from pydantic import (
    BaseModel,
    ConfigDict, 
    Field,
    field_validator
)
from app.utils.enum import HabitStatus



class TrackCreate(BaseModel):
    
    habit_id: BeanieObjectId = Field(
        ..., 
        description = "ID of the habit to track"
    )
    
    note: str | None = Field(
        default = None, 
        max_length = 500,
        description = "Optional note for the tracking entry"
    )
    
    value: int = Field(
        default = 1, 
        ge = 0,
        description = "Value or progress amount for the habit"
    )
    
    date: datetime.date = Field(
        default_factory = lambda: datetime.datetime.now().date(),
        description = "Date of the tracking entry"
    )
    
    timestamp: int = Field(
        default_factory = lambda: int(datetime.datetime.now().timestamp()),
        description = "Unix timestamp of the tracking entry"
    )
    
    status: HabitStatus = Field(
        default = HabitStatus.completed,
        description = "Status of the habit for this tracking entry"
    )



class TrackOut(BaseModel):

    id:         str = Field(
        ..., 
        alias = "_id",
        description = "Unique identifier for the tracking entry"
    )
    
    habit_id:   BeanieObjectId = Field(
        ...,
        description = "ID of the tracked habit"
    )
    
    note:       str | None = Field(
        ...,
        description = "Optional note for the tracking entry"
    )
    
    value:      int = Field(
        ...,
        description = "Value or progress amount for the habit"
    )
    
    date:       datetime.date = Field(
        ...,
        description = "Date of the tracking entry"
    )
    
    timestamp:  int = Field(
        ...,
        description = "Unix timestamp of the tracking entry"
    )
    
    status:     HabitStatus = Field(
        ...,
        description = "Status of the habit for this tracking entry"
    )
    
    created_at: datetime.datetime = Field(
        ...,
        description = "Timestamp when the tracking entry was created"
    )
    
    updated_at: datetime.datetime = Field(
        ...,
        description = "Timestamp when the tracking entry was last updated"
    )

    model_config = ConfigDict(
        from_attributes = True, 
        populate_by_name = True
    )

    
    @field_validator("id", mode = "before")
    @classmethod
    def convert_objectid(cls, v: Any) -> str:
        return str(v) 
    



class TrackUpdate(BaseModel):

    note:       str | None = Field(
        default = None, 
        max_length = 500,
        description = "Updated note for the tracking entry"
    )
    
    value:      int | None = Field(
        default = None, 
        ge = 0,
        description = "Updated value or progress amount"
    )
    
    status:     HabitStatus | None = Field(
        default = None,
        description = "Updated status of the habit"
    )





class MissedDaysResponse(BaseModel):
    
    missed_days:    List[datetime.date] = Field(
        ...,
        description = "List of dates where the habit was missed"
    )
    
    habit_id:       BeanieObjectId | None = Field(
        default = None,
        description = "ID of the habit (optional)"
    )