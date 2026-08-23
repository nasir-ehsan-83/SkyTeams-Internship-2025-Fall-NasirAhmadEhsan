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
from app.services.analytics_service import (
    get_dashboard_service
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

