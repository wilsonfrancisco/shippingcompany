from faker import Faker
from sqlalchemy import text

from src.infra.config import DBConnectionHandler
from ..person_repository import PersonRepository, PersonData

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
