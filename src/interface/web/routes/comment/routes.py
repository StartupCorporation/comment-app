from typing import Annotated

from fastapi import APIRouter, Query, status, Depends
from pydantic import UUID4

from infrastructure.bus.query.bus import QueryBus
from infrastructure.di.container import Container
from interface.web.dependencies.container import get_di_container
from interface.web.routes.comment.contracts.output.get_categories import CommentOutputContract
from interface.web.routes.comment.docs.get_product_comments import GET_PRODUCT_COMMENTS
from application.queries.get_product_comments.query import GetProductCommentsQuery


router = APIRouter(
    prefix="/comment",
    tags=["Comment"],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    responses=GET_PRODUCT_COMMENTS,  # type: ignore
)
async def get_product_comments(
    container: Annotated[Container, Depends(get_di_container)],
    product_id: Annotated[UUID4, Query(description="Product's `id` whose comments must be returned.")],
) -> list[CommentOutputContract]:
    """
    Returns all comments for the specified product.
    """
    return await container[QueryBus].handle(
        query=GetProductCommentsQuery(
            product_id=product_id,
        ),
    )
