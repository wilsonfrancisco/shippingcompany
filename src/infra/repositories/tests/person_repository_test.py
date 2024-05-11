from faker import Faker
from sqlalchemy import text

from src.infra.config import DBConnectionHandler
from src.domain.models import PersonData
from ..person_repository import PersonRepository

faker = Faker()
person_repository = PersonRepository()
db_connection_handler = DBConnectionHandler()


class TestClassPersonRepository:
    """PersonRepository Test suite"""

    def test_add(self):
        """It should be able to add a person"""

        data = PersonData(
            tax_id_number=faker.word(),
            name=faker.name(),
            neighborhood=faker.word(),
            province=faker.word(),
            street=faker.word(),
            postal_code=faker.word(),
        )

        engine = db_connection_handler.get_engine()

        person = person_repository.add(data)

        try:
            with engine.connect() as connection:
                query_person = connection.execute(
                    text(
                        f"""
                        SELECT tax_id_number
                        FROM people WHERE tax_id_number = '{person.tax_id_number}'
                      """
                    )
                ).fetchone()

                connection.execute(
                    text(
                        f"""
                        DELETE FROM people
                        WHERE tax_id_number = '{person.tax_id_number}'
                      """
                    )
                )

                connection.commit()

                assert person.tax_id_number == query_person.tax_id_number
        except:
            connection.rollback()
            raise
        finally:
            connection.close()

    def test_get_by_taxt_id_number(self):
        """It should be able to get a person by it tax id number"""

        data = PersonData(
            tax_id_number=faker.word(),
            name=faker.name(),
            neighborhood=faker.word(),
            province=faker.word(),
            street=faker.word(),
            postal_code=faker.word(),
        )

        engine = db_connection_handler.get_engine()

        person_repository.add(data)

        try:
            with engine.connect() as connection:
                person = person_repository.get_by_tax_id_number(data.tax_id_number)

                connection.execute(
                    text(
                        f"""
                        DELETE FROM people
                        WHERE tax_id_number = '{person.tax_id_number}'
                      """
                    )
                )

                connection.commit()

                assert person.tax_id_number == data.tax_id_number
        except:
            connection.rollback()
            raise
        finally:
            connection.close()
