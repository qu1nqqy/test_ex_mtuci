from fastapi import HTTPException, status

from src.storage import session
from src.core import User, Note
from src.authdata import actual_user


def filter_notes_by_checked():
    if actual_user.__int__() == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need log in or register to check '
                                                                             'notes')
    try:
        user = session.query(User).filter(User.id == actual_user.__int__()).first()
        u = user.id
        checked_notes = session.query(Note).filter(Note.Author == u,
                                                   Note.Checked == True).all()
        return {'List of sorted notes': checked_notes}
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need to log in or register to '
                                                                             'filter your notes')


def filter_notes_by_not_checked():
    if actual_user.__int__() == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need log in or register to check '
                                                                             'notes')
    try:
        user = session.query(User).filter(User.id == actual_user.__int__()).first()
        u = user.id
        not_checked_notes = session.query(Note).filter(Note.Author == u,
                                                       Note.Checked == False).all()
        return {'List of sorted notes': not_checked_notes}
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need to log in or register to '
                                                                             'filter your notes')
