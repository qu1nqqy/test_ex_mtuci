from fastapi import APIRouter
from src.notes import service
from src.notes import utils
from src.notes import NewNote, UpdateNote

router = APIRouter(
    prefix='/notes',
    tags=['Notes']
)


@router.get('/{actual_user}/get_note_{note_id}')
def get_note(note_id: int):
    return service.get_note(note_id=note_id)


@router.post('/{actual_user}/create_note')
def create_note(new_note: NewNote):
    return service.create_note(new_note=new_note)


@router.put('/{actual_user}/update_note_{note_id}')
def update_note(updated_note: UpdateNote):
    return service.update_note(updated_note=updated_note)


@router.delete('/{actual_user}/delete_note_{note_id}')
def delete_note(note_id: int):
    return service.delete_note(note_id=note_id)


@router.post('/{actual_user}/check_note_{note_id}')
def check_note(note_id: int):
    return service.check_note(note_id=note_id)


@router.get('/{actual_user}/filtered_by_checked')
def filtered_by_checked():
    return utils.filter_notes_by_checked()


@router.get('/{actual_user}/filtered_by_not_checked')
def filtered_by_not_checked():
    return utils.filter_notes_by_not_checked()
