from fastapi import status

from peerloop.core.exceptions.base import BaseCustomException


# Persistence exceptions
class UserNotExistError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


class EmailVerificationNotExistError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


# Domain exceptions
class InvalidPasswordFormatError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


class UserAlreadyRegisteredError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


class UserNotRegisteredError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, email: str) -> None:
        super().__init__(self.status_code, detail=f"User not registered: {email}")


class UserNotVerifiedError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


class IncorrectPasswordError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Incorrect password"

    def __init__(self) -> None:
        super().__init__(self.status_code, self.detail)


class VerificationCodeExpiredError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Verification code has expired"

    def __init__(self) -> None:
        super().__init__(self.status_code, self.detail)


class VerificationCodeDoesNotExistError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Verification code does not exist"

    def __init__(self) -> None:
        super().__init__(self.status_code, self.detail)


class InvalidVerificationCodeError(BaseCustomException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid verification code"

    def __init__(self) -> None:
        super().__init__(self.status_code, self.detail)
