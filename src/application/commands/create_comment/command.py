from pydantic import UUID4

from infrastructure.bus.command.message import Command


class CreateCommentCommand(Command):
    product_id: UUID4
    author: str
    content: str
