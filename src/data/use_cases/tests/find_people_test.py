from faker import Faker

from src.infra.test import PersonRepositorySpy
from ..find_people import FindPeople

faker = Faker()


class TestClassFindPeople:
    """Find people test suite"""

    def test_find_by_person_tax_id_number(self):
        """It should be able to find a person passing it's tax_id_number"""

        person_repository = PersonRepositorySpy()
        find_people = FindPeople(person_repository)

        tax_id_number = faker.ssn()

        response = find_people.execute(tax_id_number)

        assert person_repository.get_person_params["tax_id_number"] == tax_id_number
        assert response["success"] is True
        assert response["data"] is not None

    def test_find_by_person_invalid_tax_id_number(self):
        """It should not be able to find a person passing an invalid tax_id_number"""

        person_repository = PersonRepositorySpy()
        find_people = FindPeople(person_repository)

        tax_id_number = faker.random_number()

        response = find_people.execute(tax_id_number)

        assert not (person_repository.get_person_params)
        assert response["success"] is False
        assert response["data"] is None

    def test_find_all_people(self):
        """It should be able to find all people int the repository"""

        person_repository = PersonRepositorySpy()
        find_people = FindPeople(person_repository)

        response = find_people.execute()

        assert response["success"] is True
        assert response["data"] is not None
