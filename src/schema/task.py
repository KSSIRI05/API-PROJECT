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
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    due_date: Optional[datetime] = None
    status: Optional[bool] = None