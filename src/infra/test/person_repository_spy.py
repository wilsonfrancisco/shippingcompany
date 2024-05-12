from src.domain.models import Person, PersonData
from src.domain.test import mock_person


class PersonRepositorySpy:
    """Person Repository Spy utility to help in tests"""

    def __init__(self) -> None:
        self.add_person_params = {}
        self.get_person_params = {}

    def add(self, data: PersonData) -> Person:
        """Spy all the attributes in the add method"""

        self.add_person_params["name"] = data.name
        self.add_person_params["tax_id_number"] = data.tax_id_number
        self.add_person_params["neighborhood"] = data.neighborhood
        self.add_person_params["postal_code"] = data.postal_code
        self.add_person_params["street"] = data.street
        self.add_person_params["province"] = data.province

        return mock_person()

    def get_by_tax_id_number(self, tax_id_number: int = None):
        """Spy all the attributes in the get_by_tax_id_number method"""

        self.get_person_params["tax_id_number"] = tax_id_number

        return mock_person()

    def get_all(self):
        """Spy all the attributes in the get_all method"""
        return [mock_person()]
