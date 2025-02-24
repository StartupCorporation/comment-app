from datetime import datetime

from pydantic import BaseModel


class ProductComment(BaseModel):
    author_name: str
    created_at: datetime
    content: str
