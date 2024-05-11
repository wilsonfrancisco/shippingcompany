from faker import Faker
from sqlalchemy import text

from src.infra.config import DBConnectionHandler
from src.domain.models import UserData, PersonData
from ..user_repository import UserRepository
from ..person_repository import PersonRepository


faker = Faker()
db_connection_handler = DBConnectionHandler()
user_repository = UserRepository()
person_repository = PersonRepository()


class TestClassUserRepository:
    """User Repository test suite"""

    def test_add(self):
        """It should be able to add a user"""

        person_data = PersonData(
            tax_id_number=faker.word(),
            name=faker.name(),
            neighborhood=faker.word(),
            province=faker.word(),
            street=faker.word(),
            postal_code=faker.word(),
        )

        person = person_repository.add(person_data)

        data = UserData(
            email=faker.email(),
            password=faker.word(),
            username=faker.name(),
            person_tax_id=person.tax_id_number,
        )

        engine = db_connection_handler.get_engine()

        user = user_repository.add(data)

        with engine.connect() as connection:
            try:
                query_result = connection.execute(
                    text(f"SELECT id, username, email FROM users WHERE id = {user.id}")
                ).fetchone()

                connection.execute(text(f"DELETE FROM users WHERE id = {user.id}"))

                connection.execute(
                    text(
                        f"DELETE FROM people WHERE tax_id_number = '{person.tax_id_number}'"
                    )
                )

                connection.commit()

                assert query_result.id == user.id
                assert query_result.username == user.username
                assert query_result.email == user.email
            except:
                connection.rollback()
                raise
            finally:
                connection.close()
