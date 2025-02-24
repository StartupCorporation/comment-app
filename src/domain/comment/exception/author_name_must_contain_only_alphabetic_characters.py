from domain.shared.exception.base import DomainException


class AuthorNameMustContainOnlyAlphaCharacters(DomainException):

    def __init__(
        self,
        detail: str = "Author name must contain only alphabetic characters",
    ):
        super().__init__(
            detail=detail,
        )
