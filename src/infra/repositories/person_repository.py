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
                    tax_id_number=person.tax_id_number,
                    name=person.name,
                    neighborhood=person.neighborhood,
                    province=person.province,
                    street=person.street,
                    postal_code=person.postal_code,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    def get_by_tax_id_number(self, tax_id_number: int = None):
        """Get a person by tax id number
        :param - tax_id_number
        """

        try:
            with DBConnectionHandler() as db_connection:
                return (
                    db_connection.session.query(Person)
                    .filter_by(tax_id_number=tax_id_number)
                    .one()
                )
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

    def get_all(self):
        """Get all people"""
        try:
            with DBConnectionHandler() as db_connection:
                data = db_connection.session.query(Person).all()

            return data
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
