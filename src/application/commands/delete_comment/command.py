from pydantic import UUID4

from infrastructure.bus.command.message import Command


class DeleteCommentCommand(Command):
    id: UUID4
