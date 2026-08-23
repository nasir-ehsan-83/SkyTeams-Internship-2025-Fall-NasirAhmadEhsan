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
    
    habit_id:   BeanieObjectId
    note:       str | None = Field(default = None, max_length = 500)
    value:      int = Field(default = 1, ge = 0)
    date:       datetime.date = Field(default_factory = lambda: datetime.datetime.now().date())
    timestamp:  int = Field(default_factory = lambda: int(datetime.datetime.now().timestamp()))
    status:     HabitStatus = Field(default = HabitStatus.completed)



class TrackOut(BaseModel):

    id:         str = Field(alias = "_id")
    habit_id:   BeanieObjectId
    note:       str | None
    value:      int
    date:       datetime.date
    timestamp:  int
    status:     HabitStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = ConfigDict(
        from_attributes = True, 
        populate_by_name = True
    )

    
    @field_validator("id", mode = "before")
    @classmethod
    def convert_objectid(cls, v: Any) -> str:
        return str(v) 
    



class TrackUpdate(BaseModel):

    note:       str | None = Field(default = None, max_length = 500)
    value:      int | None = Field(default = None, ge = 0)
    status:     HabitStatus | None = Field(default = None)





class MissedDaysResponse(BaseModel):
    missed_days:    List[datetime.date]
    habit_id:       BeanieObjectId | None = None