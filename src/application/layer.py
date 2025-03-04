from dw_shared_kernel import (
    CommandBus,
    QueryBus,
    Container,
    Layer,
)

from application.commands.create_comment.command import CreateCommentCommand
from application.commands.create_comment.handler import CreateCommentCommandHandler
from application.commands.delete_comment.command import DeleteCommentCommand
from application.commands.delete_comment.handler import DeleteCommentCommandHandler
from application.commands.delete_product_comments.command import DeleteProductCommentsCommand
from application.commands.delete_product_comments.handler import DeleteProductCommentsCommandHandler
from application.queries.get_product_comments.handler import GetProductCommentsQueryHandler
from application.queries.get_product_comments.query import GetProductCommentsQuery
from domain.comment.repository import CommentRepository


class ApplicationLayer(Layer):
    def setup(
        self,
        container: Container,
    ) -> None:
        container[CommandBus].register(
            command=DeleteCommentCommand,
            handler=DeleteCommentCommandHandler(
                comment_repository=container[CommentRepository],
            ),
        )
        container[CommandBus].register(
            command=CreateCommentCommand,
            handler=CreateCommentCommandHandler(
                comment_repository=container[CommentRepository],
            ),
        )
        container[CommandBus].register(
            command=DeleteProductCommentsCommand,
            handler=DeleteProductCommentsCommandHandler(
                comment_repository=container[CommentRepository],
            ),
        )

        container[QueryBus].register(
            query=GetProductCommentsQuery,
            handler=GetProductCommentsQueryHandler(
                comment_repository=container[CommentRepository],
            ),
        )
