from typing import Annotated
from fastapi import (
    APIRouter, 
    Depends, 
    Query
)

from app.dependencies import get_current_user
from app.schemas import (
    DashboardOut
)
from app.schemas import HeatmapOut
from app.services.analytics_service import (
    get_dashboard_service,
    get_heatmap_service
)
from app.utils.enum import Timeframe




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