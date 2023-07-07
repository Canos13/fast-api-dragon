
from pydantic import BaseModel
from typing import Optional

class News(BaseModel):
    id: Optional[int]
    title: str
    description: str
    date: str
    content: str
    author: str
    image: str
    source: str

    class Config:
        orm_mode = True