from fastapi import APIRouter
from . import separate

router = APIRouter(
    prefix="/jamo"
)


@router.get('/change')
def separate_text(text):
    data = separate.split_text(text)

    return {'status': data}
