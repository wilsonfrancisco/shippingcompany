from typing import Type, Dict
from faker import Faker
from src.domain.models import User, UserData
from src.data.interfaces import UserRepositoryInterface
from src.domain.use_cases import FindPeople


faker = Faker()


class RegisterUserSpy:
    """Register user spy utility to help on tests execution"""

    def __init__(
        self,
        user_repository: Type[UserRepositoryInterface],
        find_people: Type[FindPeople],
    ) -> None:
        self.user_repository = user_repository
        self.find_people = find_people
        self.register_user_params = {}

    def execute(self, data: UserData) -> Dict[bool, User]:
        """Spy all the attributes in the use case execute method"""

        response = None

        is_valid_data = (
            isinstance(data.email, str)
            and isinstance(data.username, str)
            and isinstance(data.password, str)
        )

        person = self.__find_person(data.person_tax_id)

        self.register_user_params["email"] = data.email
        self.register_user_params["username"] = data.username
        self.register_user_params["password"] = data.password

        if is_valid_data and person is not None:
            response = self.user_repository.add(data)

        return {"success": is_valid_data, "data": response}

    def __find_person(self, person_tax_id: str):
        person = None

        is_valid_entry = isinstance(person_tax_id, str)

        if is_valid_entry:
            person = self.find_people.execute(tax_id_number=person_tax_id)

        return person
