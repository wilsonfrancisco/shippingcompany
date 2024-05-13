from faker import Faker
from sqlalchemy import text

from src.infra.config import DBConnectionHandler
from src.domain.test import mock_person, mock_user
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

        person_data = mock_person()

        person = person_repository.add(person_data)

        data = mock_user()
        data.person_tax_id = person.tax_id_number

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

    def test_get_by_id(self):
        """It should be able to get a user by the user id"""

        person_data = mock_person()

        person = person_repository.add(person_data)

        user_data = mock_user()
        user_data.person_tax_id = person.tax_id_number

        engine = db_connection_handler.get_engine()

        data = user_repository.add(user_data)

        with engine.connect() as connection:
            try:
                user = user_repository.get_by_id(data.id)

                connection.execute(text(f"DELETE FROM users WHERE id = {user.id}"))

                connection.execute(
                    text(
                        f"DELETE FROM people WHERE tax_id_number = '{person.tax_id_number}'"
                    )
                )

                connection.commit()

                assert user.id is not None
            except:
                connection.rollback()
                raise
            finally:
                connection.close()

    def test_get_by_username(self):
        """It should be able to get a user by passing the username"""

        person_data = mock_person()

        person = person_repository.add(person_data)

        user_data = mock_user()
        user_data.person_tax_id = person.tax_id_number

        engine = db_connection_handler.get_engine()

        data = user_repository.add(user_data)

        with engine.connect() as connection:
            try:
                user = user_repository.get_by_username(data.username)

                connection.execute(text(f"DELETE FROM users WHERE id = {user.id}"))

                connection.execute(
                    text(
                        f"DELETE FROM people WHERE tax_id_number = '{person.tax_id_number}'"
                    )
                )

                connection.commit()

                assert user.id is not None
            except:
                connection.rollback()
                raise
            finally:
                connection.close()

    def test_get_by_email(self):
        """It should be able to get a user by passing the email"""

        person_data = mock_person()

        person = person_repository.add(person_data)

        user_data = mock_user()
        user_data.person_tax_id = person.tax_id_number

        engine = db_connection_handler.get_engine()

        data = user_repository.add(user_data)

        with engine.connect() as connection:
            try:
                user = user_repository.get_by_email(data.email)

                connection.execute(text(f"DELETE FROM users WHERE id = {user.id}"))

                connection.execute(
                    text(
                        f"DELETE FROM people WHERE tax_id_number = '{person.tax_id_number}'"
                    )
                )

                connection.commit()

                assert user.id is not None
            except:
                connection.rollback()
                raise
            finally:
                connection.close()

    def test_get_all(self):
        """It should be able to get all users in the database"""

        person_data = mock_person()

        person = person_repository.add(person_data)

        fst_user = mock_user()
        fst_user.person_tax_id = person.tax_id_number

        snd_user = mock_user()
        snd_user.person_tax_id = person.tax_id_number

        thrd_user = mock_user()
        thrd_user.person_tax_id = person.tax_id_number

        engine = db_connection_handler.get_engine()

        fst_user = user_repository.add(fst_user)
        snd_user = user_repository.add(snd_user)
        thrd_user = user_repository.add(thrd_user)

        number_of_added_users = 3

        try:
            with engine.connect() as connection:
                users = user_repository.get_all()

                connection.execute(
                    text(
                        f"""
                        DELETE FROM users
                        WHERE id
                        IN ('{fst_user.id}', '{snd_user.id}', '{thrd_user.id}')
                      """
                    )
                )

                connection.execute(
                    text(
                        f"DELETE FROM people WHERE tax_id_number = '{person.tax_id_number}'"
                    )
                )

                connection.commit()

                assert users is not None
                assert len(users) >= number_of_added_users
        except:
            connection.rollback()
            raise
        finally:
            connection.close()
