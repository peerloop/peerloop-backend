from peerloop.core.exceptions.base import BaseValidationException


class InvalidEmailError(BaseValidationException):
    def __init__(self, detail: str) -> None:
        super().__init__(detail)


# Domain exceptions
class InvalidPasswordFormatError(BaseValidationException):
    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)
