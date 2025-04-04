from abc import ABC, abstractmethod
from uuid import UUID

from dw_shared_kernel import CRUDRepository

from domain.comment.entity import Comment


class CommentRepository(CRUDRepository[UUID, Comment], ABC):
    @abstractmethod
    async def get_comments_by_product_id(self, product_id: UUID) -> list[Comment]: ...

    @abstractmethod
    async def delete_comments_by_product_ids(self, product_ids: list[UUID]) -> None: ...
