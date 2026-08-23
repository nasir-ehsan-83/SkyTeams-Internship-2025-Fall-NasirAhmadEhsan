from typing import Annotated
from datetime import date
from beanie import BeanieObjectId
from fastapi import (
    APIRouter, 
    Depends, 
    Query
)

from app.dependencies import get_current_user
from app.utils.enum import Timeframe
from app.schemas import (
    HeatmapOut, 
    ProgressChartOut,
    DashboardOut,
    DistributionOut,
    ExportOut, 
    InsightsOut
)
from app.services.analytics_service import (
    get_dashboard_service,
    get_distribution_service,
    export_data_service,
    get_heatmap_service,
    get_progress_chart_service,
    get_insights_service
)




router: APIRouter = APIRouter(
    prefix = '/api/analytics',
    tags = ["Analytics"],
    dependencies = [
        Depends(get_current_user)
    ]
)


@router.get(
    '/dashboard',
    response_model = DashboardOut
)
async def get_dashboard_route(
    timeframe:      Annotated[Timeframe | None, Query(default = None)]
) -> DashboardOut:
    
    return await get_dashboard_service(timeframe)




@router.get(
    '/heatmap',
    response_model = HeatmapOut
)
async def get_heatmap_route(
    year:       Annotated[int, Query(ge = 2020, le = 2100)],
    month:      Annotated[int | None, Query(default = None, ge = 1, le = 12)]
) -> HeatmapOut:
    
    return await get_heatmap_service(year, month)




@router.get(
    '/progress-chart',
    response_model = ProgressChartOut
)
async def get_progress_chart_route(
    habit_id:   Annotated[BeanieObjectId, Query()],
    period:     Annotated[int, Query(default = 90, ge = 1, le = 365)]
) -> ProgressChartOut:
    
    return await get_progress_chart_service(habit_id, period)




@router.get(
    '/distribution',
    response_model = DistributionOut
)
async def get_distribution_route(
    habit_id:   Annotated[BeanieObjectId, Query()]
) -> DistributionOut:
    
    return await get_distribution_service(habit_id)




@router.get(
    '/insights',
    response_model = InsightsOut
)
async def get_insights_route() -> InsightsOut:
    return await get_insights_service()




@router.get(
    '/export',
    response_model = ExportOut
)
async def export_data_route(
    format:         Annotated[str, Query(default = "json", pattern = "^(json|csv)$")],
    from_date:      Annotated[date | None, Query(default = None)],
    to_date:        Annotated[date | None, Query(default = None)]
) -> ExportOut:
    
    return await export_data_service(format, from_date, to_date)