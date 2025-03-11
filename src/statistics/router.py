from fastapi import APIRouter
from src.statistics import service

router = APIRouter(
    prefix='/stat',
    tags=['Statistic']
)


@router.get('/all')
def stat_all():
    return service.stat_all()


@router.get('/{user_id}')
def stat_one(user_id: int):
    return service.stat_one(user_id=user_id)
