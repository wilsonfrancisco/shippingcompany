from abc import ABC, abstractmethod
from src.domain.models import Person, PersonData


class PersonRepositoryInterface(ABC):
    """Interface to User Repository"""

    @abstractmethod
    def add(self, data: PersonData) -> Person:
        """Add a new person entity
        :param - tax_id_number
        :param - name
        :param - neighborhood
        :param - province
        :param - street
        :param - postal_code

        :return - Tuple with a new user
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_tax_id_number(self, tax_id_number: int = None):
        """Get a person by tax id number
        :param - tax_id_number
        """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_all(self):
        """Get all people"""
        raise NotImplementedError("Method not implemented")
