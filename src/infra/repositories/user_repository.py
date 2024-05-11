from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import User


class UserRepository:
    """User Repository"""

    def add(self, username: str, email: str, password: str, tax_id_number: str):
        """Add a new user entity

        :param - username: User username
        :param - email: User email
        :param - password: User password
        :param - tax_id_number: Person tax_id_number

        :return
        """
        with DBConnectionHandler() as db_connection:
            try:
                user = User(
                    username=username,
                    email=email,
                    password=password,
                    tax_id_number=tax_id_number,
                )

                db_connection.session.add(user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
