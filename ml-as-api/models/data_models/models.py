from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr

class UserConstruct(User):
    last_name: str
    first_name: str 
    password: str 

class TodoOnCreate(BaseModel):
    text: str 
    completed: bool

class TodoonUpdate(TodoOnCreate):
    id: int
