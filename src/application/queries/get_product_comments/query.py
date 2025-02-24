from uuid import UUID

from infrastructure.bus.query.message import Query


class GetProductCommentsQuery(Query):
    product_id: UUID
