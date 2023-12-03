from dependency_injector.wiring import Provide
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_scoped_session

from peerloop.core.base_class.base_repository import BaseSQLAlchemyRepository
from peerloop.core.db.transactional import Transactional
from peerloop.domain.user.exceptions import (
    EmailVerificationNotExistError,
    UserNotExistError,
)
from peerloop.domain.user.models import EmailVerification, User

session: async_scoped_session = Provide["session"]


class UserRepository(BaseSQLAlchemyRepository[User]):
    model: type[User]

    def __init__(self, model: type[User]) -> None:
        super().__init__(model)

    @Transactional()
    async def get_user_by_email(self, email: str) -> User:
        query = select(self.model).filter(self.model.email == email)
        result = await session.execute(query)
        user = result.scalars().first()
        if user is None:
            raise UserNotExistError(f"User does not exist: {email}")
        return user

    @Transactional()
    async def get_user_or_none_by_email(self, email: str) -> User | None:
        query = select(self.model).filter(self.model.email == email)
        result = await session.execute(query)
        return result.scalars().first()

    @Transactional()
    async def check_user_exists_by_email(self, email: str) -> bool:
        try:
            await self.get_user_by_email(email=email)
            return True
        except UserNotExistError:
            return False

    @Transactional()
    async def create_user(self, email: str, hashed_password: str) -> User:
        user = self.model(email=email, password=hashed_password)
        session.add(user)
        return user


class EmailVerificationRepository(BaseSQLAlchemyRepository[EmailVerification]):
    model: type[EmailVerification]

    def __init__(self, model: type[EmailVerification]) -> None:
        super().__init__(model)

    @Transactional()
    async def create_email_verification(self, user_id: int, verification_code: str) -> None:
        email_verification = self.model(user_id=user_id, verification_code=verification_code)
        session.add(email_verification)

    @Transactional()
    async def get_email_verification_by_user_id(self, user_id: int) -> EmailVerification:
        query = select(self.model).filter(self.model.user_id == user_id)
        result = await session.execute(query)
        email_verification = result.scalars().first()
        if email_verification is None:
            raise EmailVerificationNotExistError("Email verification does not exist.")
        return email_verification
