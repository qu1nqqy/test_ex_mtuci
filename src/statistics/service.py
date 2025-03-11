from fastapi import HTTPException, status

from src.authdata import actual_user
from src.notes import Note
from src.database import session


def stat_all():
    if actual_user.__int__() == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need log in or register to check '
                                                                             'notes')
    try:
        count_of_notes = session.query(Note).count()
        return {'Count of all notes': count_of_notes}
    except Exception as e:
        print({'ErrorMessage': str(e)})
        return 'Error'


def stat_one(user_id: int):
    if actual_user.__int__() == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need log in or register to check '
                                                                             'notes')
    try:
        count_of_notes = session.query(Note).filter(Note.Author == user_id).count()
        count_of_checked_notes = session.query(Note).filter(Note.Author == user_id,
                                                            Note.Checked == True).count()
        return {'Count of notes': count_of_notes,'Count of checked notes': count_of_checked_notes}
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User with this id does not exist')
