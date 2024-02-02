from fastapi import HTTPException, status

from src.storage import session
from src.core import User, Note
from . import NewNote, UpdateNote
from datetime import datetime
from src.authdata import actual_user


def get_note(note_id: int):
    if actual_user.__int__() == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='You need log in or register to check notes')
    user = session.get(User, actual_user.__int__())
    if user.Role == 'Teacher':
        try:
            note = session.get(Note, note_id)
        except Exception:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Note with this ID does not exist')
    else:
        try:
            note = session.query(Note).filter(Note.Author == user.id,
                                              Note.id == note_id).all()
        except Exception:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Note with this ID does not exist')
    if note == []:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not allowed to do so')
    return {'Note': note}


def create_note(new_note: NewNote):
    try:
        user = session.query(User).filter(User.id == actual_user.__int__()).first()
        note = Note(
            Author=user.id,
            Title=new_note.Title,
            Text=new_note.Text,
            Checked=False,
            Create_date=datetime.now()
        )
        session.add(note)
        session.commit()

        return {'message': 'Note successfully created!', 'NoteID': note.id}
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need to log in or register to '
                                                                             'create new notes')


def update_note(updated_note: UpdateNote):
    if actual_user.__int__() == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need log in or register to check '
                                                                             'notes')
    try:
        note = session.query(Note).filter(Note.id == updated_note.OldNoteID,
                                          Note.Author == actual_user.__int__()).first()
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='You do not have any note with this id')
    if note == [] or note == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='You do not have any note with this id')
    note.Title = updated_note.NewTitle
    note.Text = updated_note.NewText
    note.Create_date = datetime.now()
    session.commit()
    return {'Updated note': session.get(Note, updated_note.OldNoteID)}



def delete_note(note_id: int):
    if actual_user.__int__() == 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You need log in or register to check '
                                                                             'notes')
    try:
        note = session.get(Note, note_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Note with this ID does not exist')
    session.delete(note)
    session.commit()
    return {'message': 'Note successfully deleted!'}
