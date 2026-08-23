from collections import defaultdict
from datetime import (
    date, 
    timedelta
)
from beanie import BeanieObjectId
from fastapi import (
    HTTPException, 
    status
)

from app.schemas import (
    DashboardOut,
    BestHabitOut,
)
from app.models import(
    Habit, 
    Track, 
    Streak
)
from app.schemas import (
    HeatmapOut,
    DistributionOut, 
    ProgressChartOut
)
from app.schemas.analytics import InsightsOut
from app.utils.enum import Timeframe
from app.config import logger




async def get_dashboard_service(
    timeframe:  Timeframe | None = None
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




async def get_heatmap_service(
    year:   int,
    month:  int | None = None
) -> HeatmapOut:
    
    try:
        start_date = date(year, month, 1) if month else date(year, 1, 1)
        end_date = date(year, month + 1, 1) - timedelta(days = 1) if month else date(year, 12, 31)
        
        tracks = await Track.find(
            Track.date >= start_date,
            Track.date <= end_date
        ).to_list()
        
        heatmap = defaultdict(int)

        for track in tracks:
            day = track.date.day
            heatmap[day] += 1
        
        return HeatmapOut(
            heatmap = dict(heatmap),
            year = year,
            month = month
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in get_heatmap_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )




async def get_progress_chart_service(
    habit_id:   BeanieObjectId,
    period:     int = 90
) -> ProgressChartOut:
    
    try:
        habit = await Habit.get(habit_id)
        
        if not habit:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Habit not found"
            )
        
        start_date = date.today() - timedelta(days = period)
        
        tracks = await Track.find(
            Track.habit_id == habit_id,
            Track.date >= start_date
        ).sort("date").to_list()
        
        labels = []
        values = []
        track_dict = {track.date: 1 for track in tracks}
        
        current_date = start_date
        while current_date <= date.today():
            labels.append(current_date)
            values.append(track_dict.get(current_date, 0))
            current_date += timedelta(days = 1)
        
        return ProgressChartOut(
            labels = labels,
            values = values,
            target_line = habit.target_count if hasattr(habit, 'target_count') else None,
            habit_title = habit.title
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in get_progress_chart_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )




async def get_distribution_service(
    habit_id:   BeanieObjectId
) -> DistributionOut:
    
    try:
        habit = await Habit.get(habit_id)
        
        if not habit:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Habit not found"
            )
        
        tracks = await Track.find(Track.habit_id == habit_id).to_list()
        
        distribution = defaultdict(int)
        time_slots = [
            ("6-9", 6, 9),
            ("9-12", 9, 12),
            ("12-15", 12, 15),
            ("15-18", 15, 18),
            ("18-21", 18, 21)
        ]
        
        for track in tracks:
            
            if track.created_at:
                hour = track.created_at.hour
            
                for slot_name, start, end in time_slots:
            
                    if start <= hour < end:
                        distribution[slot_name] += 1
                        break
        
        return DistributionOut(
            distribution = dict(distribution),
            habit_title = habit.title
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in get_distribution_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )
    



async def get_insights_service() -> InsightsOut:
    
    try:
        insights = []
        
        habits = await Habit.find().to_list()
        total_habits = len(habits)
        
        if total_habits > 0:
            insights.append(f"You have {total_habits} active habits")
        
        top_streak = await Streak.find().sort("-current_streak").limit(1).to_list()
        
        if top_streak:
            habit = await Habit.get(top_streak[0].habit_id)
        
            if habit:
                insights.append(f"Best streak: {top_streak[0].current_streak} days for {habit.title}")
        
        tracks_today = await Track.find(Track.date == date.today()).count()
        
        if tracks_today == 0:
            insights.append("You haven't tracked any habit today. Start now!")
        
        else:
            insights.append(f"You've tracked {tracks_today} habits today")
        
        weekday_tracks = defaultdict(int)
        tracks = await Track.find().to_list()
        
        for track in tracks:
            weekday = track.date.weekday()
            weekday_tracks[weekday] += 1
        
        if weekday_tracks:
            
            best_day = max(weekday_tracks.items(), key=lambda x: x[1])[0]
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            insights.append(f"Your most productive day is {days[best_day]}")
        
        return InsightsOut(
            insights=insights
        )
        
    except HTTPException:
        raise
        
    except Exception as error:
        logger.error(f"Unexpected error in get_insights_service: {error}", exc_info = True)
        
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Internal server error"
        )
