from dependency_injector import containers, providers

from peerloop.core.authentication.token_manager import TokenManager
from peerloop.core.email.email_manager import EmailManager
from peerloop.domain.user.models import EmailVerification, User
from peerloop.domain.user.repository import EmailVerificationRepository, UserRepository
from peerloop.domain.user.service import UserService


class UserContainer(containers.DeclarativeContainer):
    user_repository = providers.Factory(UserRepository, model=User)
    email_verification_repository = providers.Factory(EmailVerificationRepository, model=EmailVerification)
    token_manager: providers.Dependency[TokenManager] = providers.Dependency(instance_of=TokenManager)
    email_manager: providers.Dependency[EmailManager] = providers.Dependency(instance_of=EmailManager)
    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
        email_verification_repository=email_verification_repository,
        token_manager=token_manager,
        email_manager=email_manager,
    )
