from src.main.interfaces import RouteInterface
from src.presenters.controllers import RegisterPersonController
from src.data.use_cases.register_person import RegisterPerson
from src.infra.repositories.person_repository import PersonRepository


def register_person_composer() -> RouteInterface:
    """Composing Register user Route
    :param - None
    :return - Object with Register Person Route (Controller)
    """

    person_repository = PersonRepository()
    register_person_usecase = RegisterPerson(person_repository)
    register_person_route = RegisterPersonController(
        register_person=register_person_usecase
    )

    return register_person_route
