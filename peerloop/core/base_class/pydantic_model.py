from pydantic import Field, validator

from peerloop.core.exceptions.validation import (
    InvalidEmailError,
    InvalidPasswordFormatError,
)
from peerloop.core.utils.validation import is_valid_email_format


class EmailMixin:
    email: str = Field(default=..., examples=["changjin9792@gmail.com"])

    @validator("email")
    def email_must_be_valid(cls, v: str) -> str:
        if not is_valid_email_format(v):
            raise InvalidEmailError(f"Invalid Email Error: {v} is not a valid email address.")
        return v


class PasswordMixin:
    password: str = Field(default=..., examples=["Asdfk123*"], min_length=6, max_length=50)

    @validator("password")
    def password_must_be_valid(cls, v: str) -> str:
        """
        Rules
        1) Must be 6 <= len(pwd) <= 50
        2) Must contain at least one capital letter
        3) Must contain at least one lower-case letter
        4) Must contain at least one special character. One of (@, #, $, %, *, !)
        """
        if len(v) < 6 or len(v) > 50:
            raise InvalidPasswordFormatError("Password must be 6 <= len(pwd) <= 50")
        if not any(char.isupper() for char in v):
            raise InvalidPasswordFormatError("Password must contain at least one capital letter")
        if not any(char.islower() for char in v):
            raise InvalidPasswordFormatError("Password must contain at least one lower-case letter")
        if not any(char in ["@", "#", "$", "%", "*", "!"] for char in v):
            raise InvalidPasswordFormatError(
                "Password must contain at least one special character. One of (@, #, $, %, *, !)"
            )
        return v
