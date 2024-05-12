from typing import Dict, Type
from src.data.interfaces import PersonRepositoryInterface
from src.domain.models import Person, PersonData
from src.domain.use_cases import RegisterPerson as RegisterPersonInterface


class RegisterPerson(RegisterPersonInterface):
    """Class to define usecase: Register Person"""

    def __init__(self, person_repository: Type[PersonRepositoryInterface]):
        self.person_repository = person_repository

    def execute(self, data: PersonData) -> Dict[bool, Person]:
        """Execute register person usecase
        :param - data: Person Data
        :return - Dict[bool, Person]: A dictionary with the informations of the person
        """

        is_valid_entry = (
            isinstance(data.name, str)
            and isinstance(data.neighborhood, str)
            and isinstance(data.postal_code, str)
            and isinstance(data.province, str)
            and isinstance(data.street, str)
            and isinstance(data.tax_id_number, str)
        )

        response = None

        if is_valid_entry:
            response = self.person_repository.add(data)

        return {"sucess": is_valid_entry, "data": response}
