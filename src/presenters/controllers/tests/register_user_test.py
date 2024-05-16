from faker import Faker
from src.infra.test import UserRepositorySpy, PersonRepositorySpy
from src.data.test import FindPeopleSpy, RegisterUserSpy
from src.presenters.helpers import HttpRequest
from ..register_user import RegisterUserController

faker = Faker()


class TestClassRegisterUserController:
    """Register user controller test suite"""

    def test_register_user(self):
        """it should be able to register a valid user"""

        find_people_usecase = FindPeopleSpy(PersonRepositorySpy())
        register_user_usecase = RegisterUserSpy(
            UserRepositorySpy(), find_people_usecase
        )
        register_user_controller = RegisterUserController(register_user_usecase)

        http_request = HttpRequest(
            body={
                "email": faker.email(),
                "password": faker.password(),
                "username": faker.name(),
                "person_tax_id": faker.ssn(),
            }
        )

        response = register_user_controller.handle(http_request)

        assert (
            find_people_usecase.find_people_params["tax_id_number"]
            == http_request.body["person_tax_id"]
        )
        assert (
            register_user_usecase.register_user_params["email"]
            == http_request.body["email"]
        )
        assert (
            register_user_usecase.register_user_params["password"]
            == http_request.body["password"]
        )
        assert (
            register_user_usecase.register_user_params["username"]
            == http_request.body["username"]
        )

        assert response.status_code == 200
        assert response.body

    def test_fail_with_invalid_info_register_user(self):
        """it should not be able to register a user with invalid information"""

        find_people_usecase = FindPeopleSpy(PersonRepositorySpy())
        register_user_usecase = RegisterUserSpy(
            UserRepositorySpy(), find_people_usecase
        )
        register_user_controller = RegisterUserController(register_user_usecase)

        http_request = HttpRequest(
            body={
                "email": faker.random_number(),
                "password": faker.password(),
                "username": faker.name(),
                "person_tax_id": faker.random_number(),
            }
        )

        response = register_user_controller.handle(http_request)

        assert response.status_code == 422
        assert response.body["error"]

    def test_fail_with_missing_info_register_user(self):
        """it should not be able to register a user with missing information"""

        find_people_usecase = FindPeopleSpy(PersonRepositorySpy())
        register_user_usecase = RegisterUserSpy(
            UserRepositorySpy(), find_people_usecase
        )
        register_user_controller = RegisterUserController(register_user_usecase)

        http_request = HttpRequest(
            body={
                "password": faker.password(),
                "username": faker.name(),
                "person_tax_id": faker.random_number(),
            }
        )

        response = register_user_controller.handle(http_request)

        assert response.status_code == 422
        assert response.body["error"]

    def test_fail_with_missing_body(self):
        """it should not be able to register a user with missing information"""

        find_people_usecase = FindPeopleSpy(PersonRepositorySpy())
        register_user_usecase = RegisterUserSpy(
            UserRepositorySpy(), find_people_usecase
        )
        register_user_controller = RegisterUserController(register_user_usecase)

        http_request = HttpRequest()

        response = register_user_controller.handle(http_request)

        assert response.status_code == 400
        assert response.body["error"]
