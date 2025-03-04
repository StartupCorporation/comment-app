from pydantic import UUID4
from dw_shared_kernel import Command


class DeleteProductCommentsCommand(Command):
    product_ids: list[UUID4]
