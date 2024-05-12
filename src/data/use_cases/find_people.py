from typing import Dict, List, Type
from src.domain.models import Person
from src.domain.use_cases import FindPeople as FindPeopleInterface
from src.data.interfaces import PersonRepositoryInterface


class FindPeople(FindPeopleInterface):
    """Class to implement the use case: find people"""

    def __init__(self, person_repository: Type[PersonRepositoryInterface]):
        self.person_repository = person_repository

    def execute(self, tax_id_number: str = None) -> Dict[bool, List[Person]]:
        """Executes the find people use case
        :param - tax_id_number: a person tax id number, if this parameter is not passed
        this function returns all people in the data repository
        :return - Dict[bool, [Person]]
        """

        response = None

        if tax_id_number is None:
            response = self.person_repository.get_all()

            return {"success": True, "data": response}

        is_valid_entry = isinstance(tax_id_number, str)

        if is_valid_entry:
            response = self.person_repository.get_by_tax_id_number(tax_id_number)

        return {"success": is_valid_entry, "data": response}
