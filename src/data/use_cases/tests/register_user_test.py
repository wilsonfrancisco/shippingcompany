from faker import Faker
from src.domain.models import UserData
from src.infra.test import UserRepositorySpy, PersonRepositorySpy
from src.data.test import FindPeopleSpy
from ..register_user import RegisterUser

faker = Faker()


class TestClassRegisterUser:
    """Register user use case test suite"""

    def test_register_user(self):
        """It should be able to register a user"""

        user_repository = UserRepositorySpy()
        find_people = FindPeopleSpy(PersonRepositorySpy)
        register_user = RegisterUser(user_repository, find_people)

        person = find_people.execute(tax_id_number=faker.ssn())["data"][0]

        attributers = UserData(
            email=faker.email(),
            person_tax_id=person.tax_id_number,
            password=faker.word(),
            username=faker.name(),
        )

        response = register_user.execute(data=attributers)

        assert (
            find_people.find_people_params["tax_id_number"] == attributers.person_tax_id
        )
        assert user_repository.add_user_params["email"] == attributers.email
        assert user_repository.add_user_params["password"] == attributers.password
        assert user_repository.add_user_params["username"] == attributers.username

        assert response["success"] is True
        assert response["data"] is not None

    def test_fail_register_user(self):
        """It should not be able to register a user with a non valid person"""

        user_repository = UserRepositorySpy()
        find_people = FindPeopleSpy(PersonRepositorySpy)
        register_user = RegisterUser(user_repository, find_people)

        person = find_people.execute(tax_id_number=faker.random_number())

        attributers = UserData(
            email=faker.email(),
            person_tax_id=person,
            password=faker.word(),
            username=faker.name(),
        )

        response = register_user.execute(data=attributers)

        assert person["success"] is not True
        assert person["data"] is None
        assert response["success"] is not True
        assert response["data"] is None
