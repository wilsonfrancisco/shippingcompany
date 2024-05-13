from typing import List
from src.domain.models import UserData, User
from src.domain.test import mock_user


class UserRepositorySpy:
    """User Repository Spy utility to help in tests executions"""

    def __init__(self) -> None:
        self.add_user_params = {}
        self.get_user_params = {}

    def add(self, data: UserData) -> User:
        """Spy all the attributes it the add method"""

        self.add_user_params["username"] = data.username
        self.add_user_params["email"] = data.email
        self.add_user_params["password"] = data.password
        self.add_user_params["person_tax_id"] = data.person_tax_id

        return mock_user()

    def get_by_id(self, user_id: int) -> User:
        """Spy all the attributes it the get_by_id method"""

        self.get_user_params["user_id"] = user_id

        return mock_user()

    def get_by_username(self, username: str) -> User:
        """Spy all the attributes it the get_by_username method"""

        self.get_user_params["username"] = username

        return mock_user()

    def get_by_email(self, email: str) -> User:
        """Spy all the attributes it the get_by_email method"""

        self.get_user_params["email"] = email

        return mock_user()

    def get_all(self) -> List[User]:
        """Spy all the attributes it the get_all method"""

        return [mock_user()]
