from fastapi import APIRouter
from src.users import service
from src.users.schemas import UserLoggin, UserRegistration

router = APIRouter(
    prefix='/auth',
    tags=['Authentification']
)


@router.post('/log')
def loggin(user: UserLoggin):
    return service.loggin(user=user)


@router.post('/reg')
def registration(new_user: UserRegistration):
    return service.registration(new_user=new_user)
