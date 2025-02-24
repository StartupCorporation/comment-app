from abc import ABC, abstractmethod
from uuid import UUID

from domain.comment.entity import Comment
from domain.shared.repository.base import CRUDRepository


class CommentRepository(CRUDRepository[UUID, Comment], ABC):

    @abstractmethod
    async def get_comments_by_product_id(self, product_id: UUID) -> list[Comment]: ...
