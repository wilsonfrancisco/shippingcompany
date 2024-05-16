from typing import Type
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.domain.models import UserData
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterUserController:
    """Register user controller to handle http request to create a new user"""

    def __init__(self, register_user: Type[RegisterUserInterface]) -> None:
        self.register_user = register_user

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Controller handle method to treat http requests to create a new user"""

        response = None

        if http_request.body:
            body_string_params = http_request.body.keys()

            all_param_check = (
                "username" in body_string_params
                and "email" in body_string_params
                and "password" in body_string_params
                and "person_tax_id" in body_string_params
            )

            if all_param_check:
                data = UserData(
                    email=http_request.body["email"],
                    username=http_request.body["username"],
                    password=http_request.body["password"],
                    person_tax_id=http_request.body["person_tax_id"],
                )

                response = self.register_user.execute(data)

            else:
                response = {"success": all_param_check, "data": None}

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
