from functools import cached_property
from uuid import UUID

from sqlalchemy import select

from infrastructure.database.relational.repository.base import CRUDSQLAlchemyRepository
from domain.comment.entity import Comment
from domain.comment.repository import CommentRepository


class SQLAlchemyCommentRepository(
    CRUDSQLAlchemyRepository[UUID, Comment],
    CommentRepository,
):
    async def get_comments_by_product_id(
        self,
        product_id: UUID,
    ) -> list[Comment]:
        stmt = select(self.entity_class).where(self.entity_class.product_id == product_id)  # type: ignore
        return await self._scalars(stmt)

    @cached_property
    def entity_class(self) -> type[Comment]:
        return Comment
