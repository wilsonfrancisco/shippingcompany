from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """Interface class for routes"""

    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Route execution method"""
        raise NotImplementedError("Method not implemented.")
