from uuid import UUID

from dw_shared_kernel import Query


class GetProductCommentsQuery(Query):
    product_id: UUID
