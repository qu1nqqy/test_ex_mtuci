from fastapi import APIRouter
from . import checknote
from . import crud
from . import UserLoggin, UserRegistration

router = APIRouter(
    prefix='/auth',
    tags=['Authentification']
)


@router.post('/{actual_user}/check_note_{note_id}')
def check_note(note_id: int):
    return checknote.check_note(note_id=note_id)


@router.post('/log')
def loggin(user: UserLoggin):
    return crud.loggin(user=user)


@router.post('/reg')
def registration(new_user: UserRegistration):
    return crud.registration(new_user=new_user)
