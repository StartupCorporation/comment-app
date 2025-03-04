from pydantic import UUID4
from dw_shared_kernel import Command


class DeleteCommentCommand(Command):
    id: UUID4
