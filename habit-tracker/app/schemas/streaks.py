from datetime import (
    datetime,
    date
)
from beanie import BeanieObjectId
from pydantic import (
    BaseModel,
    Field,
    field_validator
)




class StreakResponse(BaseModel):
    
    owner_id:   BeanieObjectId = Field(
        ...,
        description = "ID of the user who owns this streak"
    )
    
    habit_id:   BeanieObjectId = Field(
        ...,
        description = "ID of the habit associated with this streak"
    )
    
    status:     str = Field(
        ...,
        min_length = 1,
        max_length = 20,
        description = "Current status of the streak (e.g., active, broken, completed)"
    )
    
    created_at: datetime = Field(
        ...,
        description = "Timestamp when the streak was created"
    )
    
    updated_at: datetime = Field(
        ...,
        description = "Timestamp when the streak was last updated"
    )

    @field_validator("status")
    @classmethod
    def validate_status(cls, v: str) -> str:
        
        if not v or len(v.strip()) == 0:
            raise ValueError("Status cannot be empty")
        
        return v.strip()




class CurrentStreakOut(StreakResponse):
    
    current_streak: int = Field(
        ...,
        ge = 0,
        description = "Current consecutive days of tracking the habit"
    )
    
    start_date:     date | None = Field(
        default = None,
        description = "Date when the current streak started"
    )
    
    last_tracked:   date | None = Field(
        default = None,
        description = "Date when the habit was last tracked"
    )

    @field_validator("current_streak")
    @classmethod
    def validate_current_streak(cls, v: int) -> int:

        if v < 0:
            raise ValueError("Current streak must be non-negative")
       
        return v

    @field_validator("start_date", "last_tracked")
    @classmethod
    def validate_dates(cls, v: date | None) -> date | None:
        
        if v is not None and v > date.today():
            raise ValueError("Date cannot be in the future")
       
        return v




class BestStreakOut(StreakResponse):
    
    best_streak: int = Field(
        ...,
        ge = 0,
        description = "Highest consecutive days achieved for this habit"
    )

    @field_validator("best_streak")
    @classmethod
    def validate_best_streak(cls, v: int) -> int:
        
        if v < 0:
            raise ValueError("Best streak must be non-negative")
        
        return v