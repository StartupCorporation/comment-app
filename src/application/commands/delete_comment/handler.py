from application.commands.delete_comment.command import DeleteCommentCommand
from domain.comment.repository import CommentRepository
from infrastructure.bus.command.handler import CommandHandler


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
