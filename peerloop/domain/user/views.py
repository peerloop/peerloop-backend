from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from peerloop.domain.user.dtos import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
    VerifyEmailRequest,
)
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
    request: LoginRequest,
    user_service: UserService = Depends(Provide["user_container.user_service"]),
) -> LoginResponse:
    resp = await user_service.login(email=request.email, password=request.password)
    access_token = resp["access_token"]
    refresh_token = resp["refresh_token"]
    return LoginResponse(access_token=access_token, refresh_token=refresh_token)


@router.post(
    "/verifications",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def verify_email(
    request: VerifyEmailRequest, user_service: UserService = Depends(Provide["user_container.user_service"])
) -> None:
    await user_service.verify_email(email=request.email, verification_code=request.verification_code)
