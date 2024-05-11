from dataclasses import dataclass
from collections import namedtuple

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import Person


@dataclass
class PersonData:
    """Person Data"""

    tax_id_number: str
    name: str
    neighborhood: str
    province: str
    street: str
    postal_code: str


class PersonRepository:
    """Person Repository"""

    def add(self, data: PersonData) -> Person:
        """Add a new person entity
        :param - tax_id_number
        :param - name
        :param - neighborhood
        :param - province
        :param - street
        :param - postal_code

        :return - Tuple with a new user
        """

        added_data = namedtuple(
            "User", "tax_id_number, name, neighborhood, province, street, postal_code"
        )

        with DBConnectionHandler() as db_connection:
            try:
                person = Person(
                    tax_id_number=data.tax_id_number,
                    name=data.name,
                    neighborhood=data.neighborhood,
                    province=data.province,
                    street=data.street,
                    postal_code=data.postal_code,
                )

                db_connection.session.add(person)
                db_connection.session.commit()

                return added_data(
                    tax_id_number=data.tax_id_number,
                    name=data.name,
                    neighborhood=data.neighborhood,
                    province=data.province,
                    street=data.street,
                    postal_code=data.postal_code,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
