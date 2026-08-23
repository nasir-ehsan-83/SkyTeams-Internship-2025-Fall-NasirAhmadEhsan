from datetime import datetime
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
    



class ScheduleOut(BaseModel):

    schedule_id:    BeanieObjectId  = Field(..., description = "Schedule ID")
    habit_id:       BeanieObjectId  = Field(..., description = "Habit ID")
    time:           str             = Field(..., description = "Reminder time")
    days:           List[int]       = Field(..., description = "Days of week")
    type:           str             = Field(..., description = "Notification type")
    next_trigger:   datetime        = Field(..., description = "Next trigger time")
    is_active:      bool            = Field(default = True, description = "Whether schedule is active")
    created_at:     datetime        = Field(..., description = "Creation timestamp")




class ScheduleUpdate(BaseModel):
    time:       str | None          = Field(default = None, description = "New reminder time", pattern = r"^([01]\d|2[0-3]):([0-5]\d)$")
    days:       List[int] | None    = Field(default = None, description = "New days of week")
    is_active:  bool | None         = Field(default = None, description = "Activate or deactivate schedule")
    
    @field_validator('days')
    @classmethod
    def validate_days(cls, v: List[int] | None) -> List[int] | None:
        
        if v is not None:
            for day in v:
                
                if not 0 <= day <= 6:
                    raise ValueError('Days must be between 0 (Monday) and 6 (Sunday)')
            
            return sorted(set(v))
        
        return v
    



class SettingsOut(BaseModel):

    push_enabled:       bool                = Field(default = True, description = "Push notifications enabled")
    email_enabled:      bool                = Field(default = False, description = "Email notifications enabled")
    reminder_time:      str | None          = Field(default = None, description = "Default reminder time", pattern = r"^([01]\d|2[0-3]):([0-5]\d)$")
    reminder_days:      List[int] | None    = Field(default = None, description = "Default reminder days")
    



class SettingsUpdate(BaseModel):
    push_enabled:       bool | None         = Field(default = None, description = "Enable push notifications")
    email_enabled:      bool | None         = Field(default = None, description = "Enable email notifications")
    reminder_time:      str | None          = Field(default = None, description = "Default reminder time", pattern = r"^([01]\d|2[0-3]):([0-5]\d)$")
    reminder_days:      List[int] | None    = Field(default = None, description = "Default reminder days")
    
    @field_validator('reminder_days')
    @classmethod
    def validate_days(cls, v: List[int] | None) -> List[int] | None:
        
        if v is not None:
            for day in v:
        
                if not 0 <= day <= 6:
                    raise ValueError('Days must be between 0 (Monday) and 6 (Sunday)')
        
            return sorted(set(v))
        
        return v
    



class TestNotificationIn(BaseModel):
    type:       str = Field(..., description = "Notification type (push/email)")
    message:    str = Field(..., description = "Test message", min_length = 1)




class TestNotificationOut(BaseModel):
    message:    str         = Field(..., description = "Status message")
    sent_at:    datetime    = Field(..., description = "Sent timestamp")




class NotificationItemOut(BaseModel):
    id:         BeanieObjectId  = Field(..., description = "Notification ID")
    type:       str             = Field(..., description = "Notification type")
    title:      str | None      = Field(default = None, description = "Notification title")
    message:    str             = Field(..., description = "Notification message")
    sent_at:    datetime        = Field(..., description = "Sent timestamp")
    status:     str             = Field(..., description = "Delivery status (delivered/failed/pending)")




class NotificationHistoryOut(BaseModel):
    notifications: List[NotificationItemOut] = Field(default_factory = list, description = "List of notifications")
    total:      int = Field(..., description = "Total count")
    limit:      int = Field(..., description = "Requested limit")