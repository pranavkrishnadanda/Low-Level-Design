from pydantic import BaseModel
from typing import Optional


class AddTodo(BaseModel):
    title : str
    description : Optional[str] = None
    status: Optional[str] = None
    todo_id : Optional[str] = None
