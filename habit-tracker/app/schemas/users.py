from beanie import BeanieObjectId
from pydantic import (
    BaseModel, 
    EmailStr, 
    ConfigDict, 
    Field, 
    field_validator
)
from datetime import datetime

from app.utils.enum import (
    UserStatus, 
    UserRole
)



class UserBase(BaseModel):
    
    name:       str = Field(
        min_length = 3, 
        max_length = 50,
        description = "Full name of the user"
    )
    
    username:   str = Field(
        min_length = 3, 
        max_length = 30,
        description = "Unique username for the user"
    )
    
    email:      EmailStr = Field(
        ...,
        description = "Email address of the user"
    )
    
    avatar:     str | None = Field(
        default = None,
        description = "URL or path to the user's avatar image"
    )



class UserCreate(UserBase):
    
    password: str = Field(
        min_length = 8,
        description = "Password for the user account (minimum 8 characters)"
    )



class UserPrivateOut(UserBase):
    
    id:     BeanieObjectId | None = Field(
        default = None, 
        alias = "_id",
        description = "Unique identifier for the user"
    )
    
    role:   UserRole = Field(
        ...,
        description = "Role of the user (e.g., admin, user)"
    )
    
    status: UserStatus = Field(
        ...,
        description = "Current status of the user (e.g., active, inactive)"
    )

    
    model_config = ConfigDict(
        from_attributes = True, 
        populate_by_name = True
    )

    
    @field_validator("id", mode = "before")
    @classmethod
    def convert_objectid(cls, v: BeanieObjectId):
        return str(v)



class UserAdminOut(UserBase):
    
    id:         BeanieObjectId = Field(
        alias = "_id",
        description = "Unique identifier for the user"
    )
    
    status:     UserStatus = Field(
        ...,
        description = "Current status of the user (e.g., active, inactive)"
    )
    
    role:       UserRole = Field(
        ...,
        description = "Role of the user (e.g., admin, user)"
    )
    
    created_at: datetime = Field(
        ...,
        description = "Timestamp when the user was created"
    )
    
    updated_at: datetime = Field(
        ...,
        description = "Timestamp when the user was last updated"
    )
    
    
    model_config = ConfigDict(
        from_attributes = True, 
        populate_by_name = True
    )

    
    @field_validator("id", mode = "before")
    @classmethod
    def convert_objectid(cls, v: BeanieObjectId):
        return str(v) 
    


class UserUpdate(BaseModel):
    
    name:       str | None = Field(
        default = None,
        min_length = 3,
        max_length = 50,
        description = "Updated full name of the user"
    )
    
    username:   str | None = Field(
        default = None,
        min_length = 3,
        max_length = 30,
        description = "Updated username for the user"
    )
    
    email:      EmailStr | None = Field(
        default = None,
        description = "Updated email address of the user"
    )
    
    password:   str | None = Field(
        default = None,
        min_length = 8,
        description = "Updated password for the user account"
    )
    
    avatar:     str | None = Field(
        default = None,
        description = "Updated URL or path to the user's avatar"
    )
    
    status:     str | None = Field(
        default = None,
        description = "Updated status of the user"
    )