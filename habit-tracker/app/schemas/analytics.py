from typing import Dict
from pydantic import (
    BaseModel, 
    Field
)




class BestHabitOut(BaseModel):
    title:      str = Field(..., description = "Habit title")
    streak:     int = Field(..., ge = 0, description = "Current streak count")




class DashboardOut(BaseModel):
    total_habits:       int                 = Field(..., ge = 0, description = "Total number of habits")
    active_habits:      int                 = Field(..., ge = 0, description = "Number of active habits")
    completion_rate:    float               = Field(..., ge = 0.0, le = 1.0, description = "Overall completion rate")
    best_habit:         BestHabitOut | None = Field(default = None, description = "Best performing habit")
    total_days_tracked: int                 = Field(..., ge = 0, description = "Total days tracked across all habits")




class HeatmapOut(BaseModel):
    heatmap:    Dict[int, int]  = Field(
        default_factory = dict,
        description = "Dictionary with day as key and count as value"
    )
    year:       int             = Field(..., description = "Year of the heatmap")
    month:      int | None      = Field(default = None, description = "Month of the heatmap if applicable")