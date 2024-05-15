from faker import Faker

from src.infra.test import PersonRepositorySpy
from src.domain.models import PersonData
from ..register_person import RegisterPerson

faker = Faker()


class TestClassRegisterPerson:
    """RegisterPerson Test suite"""

    def test_person_register(self):
        """It should be able to register a person"""

        user_repository = PersonRepositorySpy()
        register_person = RegisterPerson(user_repository)

        attributes = PersonData(
            tax_id_number=faker.ssn(),
            name=faker.name(),
            neighborhood=faker.city_suffix(),
            province=faker.city(),
            street=faker.street_suffix(),
            postal_code=faker.postalcode(),
        )

        response = register_person.execute(data=attributes)

        assert user_repository.add_person_params["name"] == attributes.name
        assert (
            user_repository.add_person_params["tax_id_number"]
            == attributes.tax_id_number
        )
        assert (
            user_repository.add_person_params["neighborhood"] == attributes.neighborhood
        )
        assert user_repository.add_person_params["province"] == attributes.province
        assert user_repository.add_person_params["street"] == attributes.street
        assert (
            user_repository.add_person_params["postal_code"] == attributes.postal_code
        )

        assert response["success"] is True
        assert response["data"] is not None

    def test_person_register_fail(self):
        """It should not be able to register a person with invalid attributes"""

        user_repository = PersonRepositorySpy()
        register_person = RegisterPerson(user_repository)

        attributes = PersonData(
            tax_id_number=faker.random_number(),  # Invalid Tax_id_number
            name=faker.name(),
            neighborhood=faker.city_suffix(),
            province=faker.city(),
            street=faker.street_suffix(),
            postal_code=faker.postalcode(),
        )

        response = register_person.execute(data=attributes)

        assert not (user_repository.add_person_params)

        assert response["success"] is False
        assert response["data"] is None
