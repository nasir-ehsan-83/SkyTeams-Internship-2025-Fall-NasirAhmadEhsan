from pydantic import BaseModel, Field, field_validator

class AppStatsOut(BaseModel):
    total_users:    int = Field(..., description = "Total number of registered users", ge = 0)
    active_users:   int = Field(..., description = "Number of active users (logged in within last 7 days)", ge = 0)
    total_habits:   int = Field(..., description = "Total number of habits created by all users", ge = 0)
    total_streaks:  int = Field(..., description = "Total number of active streaks across all users", ge = 0)

    @field_validator("total_users", "active_users", "total_habits", "total_streaks")
    @classmethod
    def validate_non_negative(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Value must be non-negative")
        return v