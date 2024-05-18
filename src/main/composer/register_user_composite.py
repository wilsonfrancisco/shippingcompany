from src.infra.repositories.user_repository import UserRepository
from src.infra.repositories.person_repository import PersonRepository
from src.data.use_cases.register_user import RegisterUser
from src.data.use_cases.find_people import FindPeople
from src.presenters.controllers import RegisterUserController


def register_user_composer():
    """Composing Register user Route
    :param - None
    :return - Object with Register User Route (Controller)
    """

    find_people_usecase = FindPeople(PersonRepository())
    register_user_usecase = RegisterUser(
        user_repository=UserRepository(),
        find_people=find_people_usecase,
    )

    register_user_controller = RegisterUserController(
        register_user=register_user_usecase
    )

    return register_user_controller
