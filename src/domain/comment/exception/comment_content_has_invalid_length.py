from dw_shared_kernel import DomainException


class CommentContentHasInvalidLength(DomainException):
    def __init__(
        self,
        detail: str = "Comment content has invalid length",
    ):
        super().__init__(
            detail=detail,
        )
