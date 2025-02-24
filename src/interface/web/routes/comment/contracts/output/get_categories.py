from datetime import datetime
from typing import Annotated

from pydantic import Field

from interface.web.contracts import OutputContract


class CommentOutputContract(OutputContract):
    author_name: Annotated[
        str,
        Field(
            examples=["John"],
            description="Person who has written the comment.",
        ),
    ]
    content: Annotated[
        str,
        Field(
            examples=["I like this!"],
            description="The comment's content.",
        ),
    ]
    created_at: Annotated[
        datetime,
        Field(
            examples=[datetime.now()],
            description="When the comment was written.",
        ),
    ]
