from pydantic import BaseModel


class UserRegistration(BaseModel):
    Name: str
    Surname: str
    Patronymic: str
    Number: int
    Role: str
    Username: str
    Password: str
    
    
class UserLoggin(BaseModel):
    Username: str
    Password: str
