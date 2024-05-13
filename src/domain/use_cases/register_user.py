from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import UserData, User


class RegisterUser(ABC):
    """Register user use case interface"""

    @abstractmethod
    def execute(self, data: UserData) -> Dict[bool, User]:
        """Use case execution method
        :param - data: a user instance from UserData model
        :return - a Dict[bool, User]
        """
        raise NotImplementedError("Method not implemented")
