from typing import Annotated

from dependency_injector.wiring import Provide, inject
from email_validator import EmailNotValidError, validate_email
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from peerloop.domain.user.dtos import (
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
    VerifyEmailRequest,
)
from peerloop.domain.user.exceptions import InvalidEmailError
from peerloop.domain.user.service import UserService

router = APIRouter(tags=["user"])


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterResponse)
@inject
async def register(
    request: RegisterRequest, user_service: UserService = Depends(Provide["user_container.user_service"])
) -> RegisterResponse:
    await user_service.create_user(email=request.email, password=request.password)
    return RegisterResponse(email=request.email)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginResponse)
@inject
async def login(
    request: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: UserService = Depends(Provide["user_container.user_service"]),
) -> LoginResponse:
    try:
        validation = validate_email(request.username)
        email = validation.email
    except EmailNotValidError:
        raise InvalidEmailError(f"Invalid Email Error: {request.username} is not a valid email address.")
    resp = await user_service.login(email=email, password=request.password)
    access_token = resp["access_token"]
    refresh_token = resp["refresh_token"]
    return LoginResponse(access_token=access_token, refresh_token=refresh_token, token_type="bearer")


@router.post(
    "/verifications",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def verify_email(
    request: VerifyEmailRequest, user_service: UserService = Depends(Provide["user_container.user_service"])
) -> None:
    await user_service.verify_email(email=request.email, verification_code=request.verification_code)
