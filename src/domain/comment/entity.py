from datetime import datetime
from dataclasses import dataclass
from uuid import UUID, uuid4

from domain.shared.entity.base import Entity
from domain.comment.exception.author_name_must_contain_only_alphabetic_characters import (
    AuthorNameMustContainOnlyAlphaCharacters,
)
from domain.comment.exception.comment_content_has_invalid_length import CommentContentHasInvalidLength


@dataclass(kw_only=True)
class Comment(Entity):
    product_id: UUID
    author: str
    content: str
    created_at: datetime

    @classmethod
    def new(
        cls,
        product_id: UUID,
        author: str,
        content: str,
    ) -> "Comment":
        cls._check_author_name(
            author=author,
        )
        cls._check_content(
            content=content,
        )
        return cls(
            id=uuid4(),
            product_id=product_id,
            author=author,
            content=content,
            created_at=datetime.now(),
        )

    @staticmethod
    def _check_author_name(author: str) -> None:
        if any(map(lambda v: not v.isalpha(), author.split())):
            raise AuthorNameMustContainOnlyAlphaCharacters()

    @staticmethod
    def _check_content(content: str) -> None:
        if not 0 <= len(content) < 512:
            raise CommentContentHasInvalidLength()
