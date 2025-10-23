from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CreateTask(BaseModel):
    title: str
    description: str
    priority: int
    due_date: datetime
    status:bool

class UpdateTask(BaseModel):
    title: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    due_date: Optional[datetime]
    status:Optional[bool]    