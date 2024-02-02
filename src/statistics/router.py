from fastapi import APIRouter
from . import getstat

router = APIRouter(
    prefix='/stat',
    tags=['Statistic']
)


@router.get('/all')
def stat_all():
    return getstat.stat_all()


@router.get('/{user_id}')
def stat_one(user_id: int):
    return getstat.stat_one(user_id=user_id)
