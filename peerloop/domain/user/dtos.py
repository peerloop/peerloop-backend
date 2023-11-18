from email_validator import EmailNotValidError, validate_email
from pydantic import BaseModel, Field, validator

from peerloop.domain.user.exceptions import (
    InvalidEmailError,
    InvalidPasswordFormatError,
)


class RegisterRequest(BaseModel):
    email: str = Field(default=..., examples=["changjin9792@gmail.com"])
    password: str = Field(default=..., examples=["Asdfk123*"], min_length=6, max_length=50)

    @validator("email")
    def email_must_be_valid(cls, v: str) -> str:
        try:
            validation = validate_email(v)
            email = validation.email
        except EmailNotValidError:
            raise InvalidEmailError(f"Invalid Email Error: {v} is not a valid email address.")
        return email

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


class RegisterResponse(BaseModel):
    email: str = Field(default=..., examples=["changjin9792@gmail.com"])


class LoginRequest(BaseModel):
    email: str = Field(default=..., examples=["changjin9792@gmail.com"])
    password: str = Field(default=..., examples=["Asdfk123*"])

    @validator("email")
    def email_must_be_valid(cls, v: str) -> str:
        try:
            validation = validate_email(v)
            email = validation.email
        except EmailNotValidError:
            raise InvalidEmailError(f"Invalid Email Error: {v} is not a valid email address.")
        return email


class LoginResponse(BaseModel):
    access_token: str = Field(default=...)
    refresh_token: str = Field(default=...)
    token_type: str = Field(default="bearer")


class VerifyEmailRequest(BaseModel):
    email: str = Field(default=...)
    verification_code: str = Field(default=...)

    @validator("email")
    def email_must_be_valid(cls, v: str) -> str:
        try:
            validation = validate_email(v)
            email = validation.email
        except EmailNotValidError:
            raise InvalidEmailError(detail=v)
        return email
