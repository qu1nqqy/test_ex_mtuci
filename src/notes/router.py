from fastapi import APIRouter
from . import crud
from . import view
from . import NewNote, UpdateNote

router = APIRouter(
    prefix='/notes',
    tags=['Notes']
)


@router.get('/{actual_user}/get_note_{note_id}')
def get_note(note_id: int):
    return crud.get_note(note_id=note_id)


@router.post('/{actual_user}/create_note')
def create_note(new_note: NewNote):
    return crud.create_note(new_note=new_note)


@router.put('/{actual_user}/update_note_{note_id}')
def update_note(updated_note: UpdateNote):
    return crud.update_note(updated_note=updated_note)


@router.delete('/{actual_user}/delete_note_{note_id}')
def delete_note(note_id: int):
    return crud.delete_note(note_id=note_id)


@router.get('/{actual_user}/filtered_by_checked')
def filtered_by_checked():
    return view.filter_notes_by_checked()


@router.get('/{actual_user}/filtered_by_not_checked')
def filtered_by_not_checked():
    return view.filter_notes_by_not_checked()
