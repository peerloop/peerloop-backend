from peerloop.core.exceptions.base import BaseCustomException


class InvalidEmailError(BaseCustomException):
    status_code = 400

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


class InvalidPasswordFormatError(BaseCustomException):
    status_code = 400

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


class DuplicateEmailError(BaseCustomException):
    status_code = 400

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


class UserDoesNotExistError(BaseCustomException):
    status_code = 400

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


class UserAlreadyExistsError(BaseCustomException):
    status_code = 400

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail)


class IncorrectPasswordError(BaseCustomException):
    status_code = 400
    detail = "Incorrect password"

    def __init__(self) -> None:
        super().__init__(self.status_code, self.detail)


class VerificationCodeExpiredError(BaseCustomException):
    status_code = 400
    detail = "Verification code has expired"

    def __init__(self) -> None:
        super().__init__(self.status_code, self.detail)


class VerificationCodeDoesNotExistError(BaseCustomException):
    status_code = 400
    detail = "Verification code does not exist"

    def __init__(self) -> None:
        super().__init__(self.status_code, self.detail)


class InvalidVerificationCodeError(BaseCustomException):
    status_code = 400
    detail = "Invalid verification code"

    def __init__(self) -> None:
        super().__init__(self.status_code, self.detail)
