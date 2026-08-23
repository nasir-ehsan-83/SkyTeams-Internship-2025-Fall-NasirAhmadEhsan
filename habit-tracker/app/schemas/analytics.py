from pydantic import (
    BaseModel, 
    Field
)




class BestHabitOut(BaseModel):
    title:      str = Field(..., description = "Habit title")
    streak:     int = Field(..., ge = 0, description = "Current streak count")