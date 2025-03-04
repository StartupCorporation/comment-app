from dw_shared_kernel import CommandHandler

from application.commands.delete_product_comments.command import DeleteProductCommentsCommand
from domain.comment.repository import CommentRepository


class DeleteProductCommentsCommandHandler(CommandHandler[DeleteProductCommentsCommand]):
    def __init__(
        self,
        comment_repository: CommentRepository,
    ):
        self._comment_repository = comment_repository

    async def __call__(
        self,
        command: DeleteProductCommentsCommand,
    ) -> None:
        await self._comment_repository.delete_comments_by_product_ids(
            product_ids=command.product_ids,
        )
