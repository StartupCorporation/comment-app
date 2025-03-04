from pydantic import UUID4
from dw_shared_kernel import Command


class CreateCommentCommand(Command):
    product_id: UUID4
    author: str
    content: str
