from typing import Type
from src.domain.models import PersonData
from src.domain.use_cases import RegisterPerson as RegisterPersonUsecase
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors
from src.main.interfaces import RouteInterface


class RegisterPersonController(RouteInterface):
    """Class to handle http requests to register a new person"""

    def __init__(self, register_person: Type[RegisterPersonUsecase]) -> None:
        self.register_person = register_person

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to handle http requests for find people use case"""

        response = None

        if http_request.body:
            body_string_params = http_request.body.keys()

            all_param_check = (
                "tax_id_number" in body_string_params
                and "name" in body_string_params
                and "neighborhood" in body_string_params
                and "province" in body_string_params
                and "street" in body_string_params
                and "postal_code" in body_string_params
            )

            if all_param_check:
                data = PersonData(
                    tax_id_number=http_request.body["tax_id_number"],
                    name=http_request.body["name"],
                    neighborhood=http_request.body["neighborhood"],
                    province=http_request.body["province"],
                    street=http_request.body["street"],
                    postal_code=http_request.body["postal_code"],
                )

                response = self.register_person.execute(data)
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
