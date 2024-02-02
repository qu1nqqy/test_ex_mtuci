from src.storage import session
from src.core import Note, User
from src.authdata import actual_user
from fastapi import HTTPException, status


def check_note(note_id: int):
    if actual_user.__int__() == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need log in or register to check '
                                                                             'notes')
    user = session.query(User).filter(User.id == actual_user.__int__()).first()

    try:
        note = session.query(Note).filter(Note.id == note_id).first()
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Note with this ID does not exist')

    if user.Role == 'Teacher' and note.Checked == False:
        note.Checked = True
        session.commit()
        return {'message': 'Note successfully checked!'}
    elif user.Role == 'Teacher' and note.Checked == True: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='This note already checked')
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not allowed to do so')
