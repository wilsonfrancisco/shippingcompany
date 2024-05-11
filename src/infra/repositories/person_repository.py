from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import Person
from src.domain.models import Person as PersonModel, PersonData


class PersonRepository:
    """Person Repository"""

    def add(self, data: PersonData) -> PersonModel:
        """Add a new person entity
        :param - tax_id_number
        :param - name
        :param - neighborhood
        :param - province
        :param - street
        :param - postal_code

        :return - Tuple with a new user
        """

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

                return PersonModel(
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
