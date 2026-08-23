from fastapi import (
    HTTPException, 
    status
)

from app.schemas import (
    DashboardOut,
    BestHabitOut,
)
from app.models import Habit, Track, Streak
from app.utils.enum import Timeframe
from app.config.logging_handler import logger


async def get_dashboard_service(
    timeframe:      Timeframe | None = None
) -> DashboardOut:
    try:
        total_habits = await Habit.count()
        
        active_habits = await Habit.find(Habit.status == "active").count()
        
        total_tracks = await Track.count()
        total_habits_count = await Habit.count()
        
        completion_rate = total_tracks / (total_habits_count * 30) if total_habits_count > 0 else 0.0
        completion_rate = min(completion_rate, 1.0)
        
        streaks = await Streak.find().sort("-current_streak").limit(1).to_list()
        best_habit = None
        
        if streaks:
            streak = streaks[0]
            habit = await Habit.get(streak.habit_id)
            
            if habit:
                best_habit = BestHabitOut(
                    title = habit.title,
                    streak = streak.current_streak
                )
        
        total_days_tracked = await Track.count()
        
        return DashboardOut(
            total_habits = total_habits,
            active_habits = active_habits,
            completion_rate = round(completion_rate, 2),
            best_habit = best_habit,
            total_days_tracked = total_days_tracked
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in get_dashboard_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )

