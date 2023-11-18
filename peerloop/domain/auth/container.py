from dependency_injector import containers, providers

from peerloop.core.authentication.token_manager import TokenManager
from peerloop.domain.auth.service import AuthService


class AuthContainer(containers.DeclarativeContainer):
    token_manager: providers.Dependency[TokenManager] = providers.Dependency()
    auth_service = providers.Factory(AuthService, token_manager=token_manager)
