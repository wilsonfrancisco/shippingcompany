from faker import Faker
from src.infra.test import PersonRepositorySpy
from src.data.test import RegisterPersonSpy
from src.presenters.helpers import HttpRequest
from ..register_person import RegisterPersonController

faker = Faker()


class TestClassRegisterPersonController:
    """Register person controller test suite"""

    def test_register_person(self):
        """it should be able to register a person with valid informations in the body param"""

        register_person_usecase = RegisterPersonSpy(PersonRepositorySpy())
        register_person_controller = RegisterPersonController(register_person_usecase)

        http_request = HttpRequest(
            body={
                "tax_id_number": faker.ssn(),
                "name": faker.name(),
                "neighborhood": faker.city_suffix(),
                "province": faker.street_suffix(),
                "street": faker.street_suffix(),
                "postal_code": faker.postalcode(),
            }
        )

        response = register_person_controller.handle(http_request)

        assert (
            register_person_usecase.register_person_params["name"]
            == http_request.body["name"]
        )
        assert (
            register_person_usecase.register_person_params["tax_id_number"]
            == http_request.body["tax_id_number"]
        )
        assert (
            register_person_usecase.register_person_params["neighborhood"]
            == http_request.body["neighborhood"]
        )
        assert (
            register_person_usecase.register_person_params["province"]
            == http_request.body["province"]
        )
        assert (
            register_person_usecase.register_person_params["street"]
            == http_request.body["street"]
        )
        assert (
            register_person_usecase.register_person_params["postal_code"]
            == http_request.body["postal_code"]
        )

        assert response.status_code == 200
        assert response.body

    def test_fail_with_missing_params(self):
        """it should not be able to register a person with missing information"""

        register_person_usecase = RegisterPersonSpy(PersonRepositorySpy())
        register_person_controller = RegisterPersonController(register_person_usecase)

        http_request = HttpRequest(
            body={
                "tax_id_number": faker.ssn(),
                "name": faker.name(),
                "neighborhood": faker.city_suffix(),
                "province": faker.street_suffix(),
                "street": faker.street_suffix(),
            }
        )

        response = register_person_controller.handle(http_request)

        assert response.status_code == 422
        assert response.body["error"]

    def test_fail_with_invalid_params(self):
        """it should not be able to register a person with missing information"""

        register_person_usecase = RegisterPersonSpy(PersonRepositorySpy())
        register_person_controller = RegisterPersonController(register_person_usecase)

        http_request = HttpRequest(
            body={
                "tax_id_number": faker.random_number(),
                "name": faker.name(),
                "neighborhood": faker.city_suffix(),
                "province": faker.street_suffix(),
                "street": faker.random_number(),
            }
        )

        response = register_person_controller.handle(http_request)

        assert response.status_code == 422
        assert response.body["error"]

    def test_fail_without_body_param_to_register_person(self):
        """it should not be able to register a person without the body param in the request"""

        register_person_usecase = RegisterPersonSpy(PersonRepositorySpy())
        register_person_controller = RegisterPersonController(register_person_usecase)

        http_request = HttpRequest()

        response = register_person_controller.handle(http_request)

        assert response.status_code == 400
        assert response.body["error"]
