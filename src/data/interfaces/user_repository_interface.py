from abc import ABC, abstractmethod
from src.domain.models import User, UserData


class UserRepositoryInterface(ABC):
    """Interface to User Repository"""

    @abstractmethod
    def add(self, data: UserData) -> User:
        """Add a new user entity

        :param - username: User username
        :param - email: User email
        :param - password: User password
        :param - tax_id_number: Person tax_id_number

        :return a new user
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        """Get a user by passing the user id

        :param - user_id: User identifier
        :return: A user entity
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_username(self, username: str) -> User:
        """Get a user by passing the username

        :param - username: The username
        :return: A user entity
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        """Get a user by passing the user email

        :param - email: User email
        :return: A user entity
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_all(self) -> User:
        """Get all users"""
        raise NotImplementedError("Method not implemented")
