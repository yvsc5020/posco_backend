from fastapi import APIRouter
from . import image
from pydantic import BaseModel

router = APIRouter(
    prefix="/image"
)


class Item(BaseModel):
    img: str


@router.post("/caption")
async def work(item: Item):
    request_image = item.dict()['img']
    result = image.caption(request_image)
    return result
