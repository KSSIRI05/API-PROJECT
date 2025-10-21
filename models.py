from datetime import datetime
from beanie import Document
class task(Document):
    title: str
    description: str
    priority: int
    due_date: datetime
    status:bool