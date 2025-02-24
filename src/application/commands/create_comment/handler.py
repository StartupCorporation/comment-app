from application.commands.create_comment.command import CreateCommentCommand
from domain.comment.entity import Comment
from domain.comment.repository import CommentRepository
from infrastructure.bus.command.handler import CommandHandler


class CreateCommentCommandHandler(CommandHandler[CreateCommentCommand]):

    def __init__(
        self,
        comment_repository: CommentRepository,
    ):
        self._comment_repository = comment_repository

    async def __call__(
        self,
        command: CreateCommentCommand,
    ) -> None:
        comment = Comment.new(
            product_id=command.product_id,
            author_name=command.author_name,
            content=command.content,
        )
        await self._comment_repository.save(
            entity=comment,
        )
