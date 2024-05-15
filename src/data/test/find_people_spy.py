from typing import List, Dict
from src.domain.models import Person
from src.data.interfaces import PersonRepositoryInterface
from src.domain.test import mock_person


class FindPeopleSpy:
    """Find people spy utility to help in tests execution"""

    def __init__(self, person_repository: PersonRepositoryInterface):
        self.person_repository = person_repository
        self.find_people_params = {}

    def execute(self, tax_id_number: str = None) -> Dict[bool, List[Person]]:
        """Spy all the attributes in the execute method"""

        response = None

        if tax_id_number is None:
            response = self.person_repository.get_all()

            return {"success": True, "data": response}

        is_valid_entry = isinstance(tax_id_number, str)

        self.find_people_params["tax_id_number"] = tax_id_number

        if is_valid_entry:
            response = [mock_person()]

        return {"success": is_valid_entry, "data": response}
