from fastapi import HTTPException, status

from .schemas import UserLoggin, UserRegistration
from src.authdata import actual_user
from src.storage import session
from src.core import User


def loggin(user: UserLoggin):
    try:
        user_loggin = session.query(User).filter(User.Username == user.Username,
                                                 User.Password == user.Password).first()
        actual_user(user_loggin.id)
        return {'User': user_loggin, 'User ID': actual_user.__int__()}
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Wrong username or password')


def registration(new_user: UserRegistration):
    try:
        user = User(Name=new_user.Name,
                    Surname=new_user.Surname,
                    Patronymic=new_user.Patronymic,
                    Number=new_user.Number,
                    Role=new_user.Role,
                    Username=new_user.Username,
                    Password=new_user.Password)
        session.add(user)
        session.commit()
        actual_user(user.id)
        return {'Your profile': user, 'Your ID': actual_user.__int__()}
    except Exception:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='This username is already used')
