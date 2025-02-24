from uuid import UUID

from infrastructure.bus.command.message import Command


class CreateCommentCommand(Command):
    product_id: UUID
    author_name: str
    content: str
