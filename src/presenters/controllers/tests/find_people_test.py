from faker import Faker
from src.data.test import FindPeopleSpy
from src.infra.test import PersonRepositorySpy
from src.presenters.helpers import HttpRequest
from ..find_people import FindPeopleController


faker = Faker()


class TestClassFindPeopleController:
    """Find people controller test suite"""

    def test_handle(self):
        """it should be able to handle a http request to find a specific person using query params"""

        find_people = FindPeopleSpy(PersonRepositorySpy())
        find_people_controller = FindPeopleController(find_people)

        http_request = HttpRequest(query={"tax_id_number": faker.ssn()})

        response = find_people_controller.handle(http_request)

        assert (
            find_people.find_people_params["tax_id_number"]
            == http_request.query["tax_id_number"]
        )
        assert response.status_code == 200
        assert response.body

    def test_find_all_handle(self):
        """it should be able to handle a http request to find all people using query params"""

        find_people = FindPeopleSpy(PersonRepositorySpy())
        find_people_controller = FindPeopleController(find_people)

        http_request = HttpRequest(query={"all": True})

        response = find_people_controller.handle(http_request)

        assert not (find_people.find_people_params)
        assert response.status_code == 200
        assert response.body

    def test_handle_with_invalid_query(self):
        """it should not be able to handle a http request to find people with an invalid query param"""

        find_people = FindPeopleSpy(PersonRepositorySpy())
        find_people_controller = FindPeopleController(find_people)

        http_request = HttpRequest(query={"somethingElse": True})

        response = find_people_controller.handle(http_request)

        assert not (find_people.find_people_params)
        assert response.status_code == 422
        assert "error" in response.body.keys()

    def test_handle_with_missing_param(self):
        """it should not be able to handle a http request to find people with a missing param param"""

        find_people = FindPeopleSpy(PersonRepositorySpy())
        find_people_controller = FindPeopleController(find_people)

        http_request = HttpRequest(query={})

        response = find_people_controller.handle(http_request)

        assert not (find_people.find_people_params)
        assert response.status_code == 400
        assert "error" in response.body.keys()

    def test_handle_with_no_query(self):
        """it should not be able to handle a http request to find people without a query param"""

        find_people = FindPeopleSpy(PersonRepositorySpy())
        find_people_controller = FindPeopleController(find_people)

        http_request = HttpRequest()

        response = find_people_controller.handle(http_request)

        assert not (find_people.find_people_params)
        assert response.status_code == 400
        assert "error" in response.body.keys()
