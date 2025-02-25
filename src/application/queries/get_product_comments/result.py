from datetime import datetime

from pydantic import UUID4, BaseModel


class ProductComment(BaseModel):
    id: UUID4
    author: str
    created_at: datetime
    content: str
