from typing import Type, Dict
from src.domain.models import Person, PersonData
from src.data.interfaces import PersonRepositoryInterface


class RegisterPersonSpy:
    """Register person utility to help in test execution"""

    def __init__(self, person_repository: Type[PersonRepositoryInterface]) -> None:
        self.person_repository = person_repository
        self.register_person_params = {}

    def execute(self, data: PersonData) -> Dict[bool, Person]:
        """Spy all the atributtes in the execute method"""

        response = None

        is_valid_entry = (
            isinstance(data.name, str)
            and isinstance(data.neighborhood, str)
            and isinstance(data.postal_code, str)
            and isinstance(data.province, str)
            and isinstance(data.street, str)
            and isinstance(data.tax_id_number, str)
        )

        self.register_person_params = {
            "name": data.name,
            "neighborhood": data.neighborhood,
            "postal_code": data.postal_code,
            "province": data.province,
            "street": data.street,
            "tax_id_number": data.tax_id_number,
        }

        if is_valid_entry:
            response = self.person_repository.add(data)

        return {"success": is_valid_entry, "data": response}
