from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

class CreateTask(BaseModel):
    title: str = Field(..., min_length=1)
    description: str
    priority: int = Field(..., ge=0)
    due_date: datetime
    status: bool

    @field_validator('title')
    @classmethod
    def title_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Title cannot be empty')
        return v

class UpdateTask(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
    priority: Optional[int] = Field(None, ge=0)
    due_date: Optional[datetime] = None
    status: Optional[bool] = None

    @field_validator('title', mode='before')
    @classmethod
    def title_validation(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('Title cannot be empty')
        return v