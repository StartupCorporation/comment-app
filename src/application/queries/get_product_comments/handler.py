from application.queries.get_product_comments.query import GetProductCommentsQuery
from application.queries.get_product_comments.result import ProductComment
from domain.comment.repository import CommentRepository
from infrastructure.bus.query.handler import QueryHandler


class GetProductCommentsQueryHandler(QueryHandler[GetProductCommentsQuery, list[ProductComment]]):
    def __init__(
        self,
        comment_repository: CommentRepository,
    ):
        self._comment_repository = comment_repository

    async def __call__(
        self,
        query: GetProductCommentsQuery,
    ) -> list[ProductComment]:
        comments = await self._comment_repository.get_comments_by_product_id(
            product_id=query.product_id,
        )

        return [ProductComment.model_validate(comment, from_attributes=True) for comment in comments]
