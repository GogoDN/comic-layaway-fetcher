from fastapi import APIRouter, Depends

from datetime import datetime

from pydantic import BaseModel

from ..dependencies import AuthHeaders, SortParams
from ..services.layaway import LayawayService


router = APIRouter(
    prefix="/getLayawayList",
    tags=["get_layaway_list"],
    responses={404: {"description": "Not Found"}},
)


class Comic(BaseModel):
    title: str
    onSaleDate: datetime
    characters: list[str]


class LayawayOut(BaseModel):
    comics: list[Comic]


@router.get("/", response_model=LayawayOut)
def get_list(
    headers: AuthHeaders = Depends(AuthHeaders),
    params: SortParams = Depends(SortParams),
    service: LayawayService = Depends(LayawayService),
):
    params.validate_params()
    return service.get_comic_list(headers, params)
