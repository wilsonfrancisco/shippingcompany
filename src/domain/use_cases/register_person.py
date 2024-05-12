from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import Person, PersonData


class RegisterPerson(ABC):
    """Register person use case interface"""

    @abstractmethod
    def execute(self, data: PersonData) -> Dict[bool, Person]:
        """Executes the use case
        :param - data: a person object from PersonData class
        :return - Dict[bool, Person]
        """
        raise NotImplementedError("Method not implemented")
