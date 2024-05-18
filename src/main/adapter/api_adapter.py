from typing import Type
from sqlalchemy.exc import IntegrityError
from flask import Request
from src.main.interfaces import RouteInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adapter(request: Type[Request], api_route: Type[RouteInterface]) -> any:
    """Adapter Pattern to Flask
    :param - Flask request
    :api_route: composite routes
    """

    try:
        http_request = HttpRequest(body=request.json)

        response = api_route.handle(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()

        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
