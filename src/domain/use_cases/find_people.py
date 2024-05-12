from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import Person


class FindPeople(ABC):
    """Find people use case interface"""

    @abstractmethod
    def execute(self, tax_id_number: str = None) -> Dict[bool, List[Person]]:
        """Executes the find people use case
        :param - tax_id_number: a person tax id number, if this parameter is not passed
        this function returns all people in the data repository
        :return - Dict[bool, [Person]]
        """

        raise NotImplementedError("Method not implemented.")
