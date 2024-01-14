from pydantic import BaseModel, Field

from peerloop.core.base_class.pydantic_model import EmailMixin, PasswordMixin
from peerloop.domain.user.constants import ExternalLinkName


# Create User DTOs
class ExternalLink(BaseModel):
    name: ExternalLinkName = Field(default=..., examples=["github"])
    url: str = Field(default=..., examples=["github.com/noisrucer"])


class RegisterRequest(BaseModel, EmailMixin, PasswordMixin):
    email: str = Field(default=..., examples=["changjin9792@gmail.com"])
    password: str = Field(default=..., examples=["Asdfk123*"], min_length=6, max_length=50)
    username: str = Field(default=..., examples=["noisrucer"], min_length=1, max_length=50)
    job_title: str = Field(default=None, examples=["Backend Engineer"], min_length=1, max_length=50)
    organization: str = Field(default=None, examples=["peerloop"], min_length=1, max_length=50)
    bio: str = Field(default=None, examples=["I am a backend engineer at peerloop"], min_length=5, max_length=500)
    country: str = Field(default=None, examples=["South Korea"], min_length=1, max_length=50)
    img_url: str = Field(default=None, examples=["https://peerloop.io/img/profile.png"], min_length=1, max_length=500)
    external_links: list[ExternalLink] = Field(
        default=None,
        examples=[
            [{"name": "github", "url": "github.com/noisrucer"}, {"name": "linkedin", "url": "linkedin.com/noisrucer"}]
        ],
    )


class RegisterResponse(BaseModel):
    email: str = Field(default=..., examples=["changjin9792@gmail.com"])


# Login DTOs
class LoginResponse(BaseModel):
    access_token: str = Field(default=...)
    refresh_token: str = Field(default=...)
    token_type: str = Field(default="bearer")


# Verify Email DTOs
class VerifyEmailRequest(BaseModel, EmailMixin):
    email: str = Field(default=..., examples=["changjin9792@gmail.com"])
    verification_code: str = Field(default=...)


class UserResponse(BaseModel):
    id: int = Field(default=...)
    email: str = Field(default=...)
    is_verified: bool = Field(default=...)
