from pydantic import BaseModel


class TodoBase(BaseModel):
    name: str
    
    
class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    owner_id: int
    
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    todos: list[Todo] = []

    class Config:
        from_attributes = True
