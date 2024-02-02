from pydantic import BaseModel


class NewNote(BaseModel):
    Title: str
    Text: str


class UpdateNote(BaseModel):
    OldNoteID: int
    NewTitle: str
    NewText: str
