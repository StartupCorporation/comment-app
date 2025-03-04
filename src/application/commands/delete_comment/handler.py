from dw_shared_kernel import CommandHandler

from application.commands.delete_comment.command import DeleteCommentCommand
from domain.comment.repository import CommentRepository


class DeleteCommentCommandHandler(CommandHandler[DeleteCommentCommand]):
    def __init__(
        self,
        comment_repository: CommentRepository,
    ):
        self._comment_repository = comment_repository

    async def __call__(
        self,
        command: DeleteCommentCommand,
    ) -> None:
        await self._comment_repository.delete(
            id_=command.id,
        )
