from uuid import UUID

from infrastructure.bus.command.message import Command


class DeleteCommentCommand(Command):
    id: UUID
