from typing import Any
from datetime import datetime
from pydantic import (
    BaseModel,
    ConfigDict, 
    Field,
    field_validator
)


class PreferenceOut(BaseModel):

    id: str = Field(
        ..., 
        alias = "_id",
        description = "Unique identifier for the user preferences (MongoDB ObjectId)"
    )
    
    theme: str = Field(
        ..., 
        max_length = 20,
        description = "UI theme preference (e.g., light, dark, system)"
    )
    
    language: str = Field(
        ..., 
        max_length = 10,
        description = "User's preferred language code (e.g., en, fa, fr)"
    )
    
    timezone: str = Field(
        ..., 
        max_length = 50,
        description = "User's timezone (e.g., Asia/Tehran, UTC, America/New_York)"
    )
    
    start_of_week: str = Field(
        ..., 
        max_length = 20,
        description = "First day of the week (e.g., monday, sunday)"
    )
    
    notifications_enabled: bool = Field(
        ..., 
        description = "Whether notifications are enabled for the user"
    )
    
    reminder_time: str | None = Field(
        default = None,
        max_length = 5,
        description = "Default reminder time in HH:MM format (24-hour)"
    )
     
    default_view: str = Field(
        ..., 
        max_length = 20,
        description = "Default view for the dashboard (e.g., daily, weekly, monthly)"
    )
    
    created_at: datetime = Field(
        ..., 
        description = "Timestamp when the preferences were created"
    )
    
    updated_at: datetime = Field(
        ..., 
        description = "Timestamp when the preferences were last updated"
    )

    model_config = ConfigDict(
        from_attributes = True, 
        populate_by_name = True
    )

    @field_validator("id", mode = "before")
    @classmethod
    def convert_objectid(cls, v: Any) -> str:
        return str(v)


class PreferenceUpdate(BaseModel):

    theme: str | None = Field(
        default = None,
        max_length = 20,
        description = "UI theme preference (e.g., light, dark, system)"
    )
    
    language: str | None = Field(
        default = None,
        max_length = 10,
        description = "User's preferred language code (e.g., en, fa, fr)"
    )
    
    timezone: str | None = Field(
        default = None,
        max_length = 50,
        description = "User's timezone (e.g., Asia/Tehran, UTC, America/New_York)"
    )
    
    start_of_week: str | None = Field(
        default = None,
        max_length = 20,
        description = "First day of the week (e.g., monday, sunday)"
    )
    
    notifications_enabled: bool | None = Field(
        default = None,
        description = "Whether notifications are enabled for the user"
    )
    
    reminder_time: str | None = Field(
        default = None,
        max_length = 5,
        description = "Default reminder time in HH:MM format (24-hour)"
    )
    
    default_view: str | None = Field(
        default = None,
        max_length = 20,
        description = "Default view for the dashboard (e.g., daily, weekly, monthly)"
    )

    @field_validator("reminder_time")
    @classmethod
    def validate_reminder_time(cls, v: str | None) -> str | None:

        if v is not None:
            import re
            pattern = r"^([01]\d|2[0-3]):([0-5]\d)$"
           
            if not re.match(pattern, v):
                raise ValueError("reminder_time must be in HH:MM format (e.g., 14:30)")
        return v

    @field_validator("theme", "language", "timezone", "start_of_week", "default_vie")
    @classmethod
    def validate_not_empty(cls, v: str | None) -> str | None:

        if v is not None and len(v.strip()) == 0:
            raise ValueError('Field cannot be empty string')
        return v