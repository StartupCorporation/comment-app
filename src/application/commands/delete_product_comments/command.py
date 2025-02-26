from pydantic import UUID4

from infrastructure.bus.command.message import Command


class DeleteProductCommentsCommand(Command):
    product_ids: list[UUID4]
