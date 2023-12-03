import asyncio
from datetime import datetime

from peerloop.core.authentication.token_manager import TokenManager
from peerloop.core.email.email_manager import EmailManager
from peerloop.core.utils.auth import (
    check_password,
    generate_email_verification_code,
    hash_password,
)
from peerloop.domain.user.exceptions import (
    IncorrectPasswordError,
    InvalidVerificationCodeError,
    UserAlreadyRegisteredError,
    UserNotRegisteredError,
    UserNotVerifiedError,
    VerificationCodeExpiredError,
)
from peerloop.domain.user.models import User
from peerloop.domain.user.repository import EmailVerificationRepository, UserRepository


class UserService:
    def __init__(
        self,
        user_repository: UserRepository,
        email_verification_repository: EmailVerificationRepository,
        token_manager: TokenManager,
        email_manager: EmailManager,
    ) -> None:
        self.user_repo = user_repository
        self.email_verification_repo = email_verification_repository
        self.token_manager = token_manager
        self.email_manager = email_manager

    async def create_user(self, email: str, password: str) -> None:
        # Check duplicated email
        existing_user = await self.user_repo.get_user_or_none_by_email(email=email)
        if existing_user:
            if existing_user.is_verified:
                raise UserAlreadyRegisteredError(f"User already registered: {email}.")
            else:  # If unverified user exists, delete it and create new user.
                await self.user_repo.delete_by_id(id=existing_user.id)

        # Create a new unverified user
        hashed_password = hash_password(password)
        new_user = await self.user_repo.create_user(email=email, hashed_password=hashed_password)

        # Send verification email
        verification_code = generate_email_verification_code()
        content = self.email_manager.read_and_format_html(replacements={"__VERIFICATION_CODE__": verification_code})
        asyncio.create_task(
            self.email_manager.send_email(
                recipient=new_user.email, subject="Please verify your email address.", content=content
            )
        )

        # Create EmailVerification table entry
        await self.email_verification_repo.create_email_verification(
            user_id=new_user.id, verification_code=verification_code
        )

    async def login(
        self,
        email: str,
        password: str,
    ) -> dict[str, str]:
        # Check whether the user exists
        user = await self.user_repo.get_user_or_none_by_email(email=email)
        if not user:
            raise UserNotRegisteredError(email=email)

        # Check whether the user is verified
        if not user.is_verified:
            raise UserNotVerifiedError(f"User Not Verified: {email} is not verified.")

        # Check whether the password is correct
        if not check_password(raw_password=password, hashed_password=user.password):
            raise IncorrectPasswordError()

        access_token, refresh_token = self.token_manager.create_tokens(sub=user.id)
        return {"access_token": access_token, "refresh_token": refresh_token}

    async def verify_email(self, email: str, verification_code: str) -> None:
        # Check if user exists
        user = await self.user_repo.get_user_or_none_by_email(email=email)
        if user is None:
            raise UserNotRegisteredError(f"User not registered: {email} does not exist.")

        # Check if user is already verified
        if user.is_verified:
            raise UserAlreadyRegisteredError(f"User already registered: {email} is already registered.")

        # Check if verification code is expired
        email_verification = await self.email_verification_repo.get_email_verification_by_user_id(user_id=user.id)
        if email_verification.expiration_time < datetime.utcnow():
            raise VerificationCodeExpiredError()

        # Check if verification code is correct
        if verification_code != email_verification.verification_code:
            raise InvalidVerificationCodeError()

        # Update is_verified to True
        await self.user_repo.update_by_id(id=user.id, params={"is_verified": True})

    async def get_user_by_id(self, user_id: int) -> User:
        # Check whether the user exists
        user = await self.user_repo.get_by_id(id=user_id)
        if user is None:
            raise UserNotRegisteredError(f"User is not registered: {user_id} does not exist.")

        return user
