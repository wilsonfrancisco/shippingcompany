from typing import Type
from src.domain.use_cases import FindPeople
from src.presenters.helpers import HttpResponse, HttpRequest
from src.presenters.errors import HttpErrors


class FindPeopleController:
    """Find person controller representation to handle http requests"""

    def __init__(self, find_people: Type[FindPeople]) -> None:
        self.find_people = find_people

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to handle http requests for find people use case"""

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "tax_id_number" in query_string_params:
                tax_id_number = http_request.query["tax_id_number"]
                response = self.find_people.execute(tax_id_number)

            elif "all" in query_string_params:
                response = self.find_people.execute()

            else:
                response = {"success": False, "data": None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])

        http_error = HttpErrors.error_400()

        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
