from typing import Type, Dict
from src.domain.models import User, UserData, Person
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface
from src.domain.use_cases import FindPeople


class RegisterUser(RegisterUserInterface):
    """Register user use case implementation"""

    def __init__(
        self,
        user_repository: Type[UserRepositoryInterface],
        find_people: Type[FindPeople],
    ) -> None:
        self.user_repository = user_repository
        self.find_peope = find_people

    def execute(self, data: UserData) -> Dict[bool, User]:
        """Use case execution method
        :param - data: a user instance from UserData model
        :return - a Dict[bool, User]
        """
        response = None

        is_valid_entry = (
            isinstance(data.email, str)
            and isinstance(data.password, str)
            and isinstance(data.username, str)
        )

        founded_person = self.__find_person(data.person_tax_id)

        is_valid_data = is_valid_entry and founded_person

        if is_valid_data:
            response = self.user_repository.add(data)

        return {"success": is_valid_data, "data": response}

    def __find_person(self, tax_id_number: str) -> Person:
        """Find the person with the provided tax_id_number
        :param - tax_id_number: The tax id number of an existing person in the repository
        :return - An instance of Person
        """
        person = None

        is_valid_tax_id_number = isinstance(tax_id_number, str)

        if is_valid_tax_id_number:
            person = self.find_peope.execute(tax_id_number)

        return person
