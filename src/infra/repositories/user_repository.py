from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import User
from src.domain.models import UserData, User as UserModel


class UserRepository:
    """User Repository"""

    def add(self, data: UserData) -> UserModel:
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
                    username=data.username,
                    email=data.email,
                    password=data.password,
                    person_tax_id=data.person_tax_id,
                )

                db_connection.session.add(user)
                db_connection.session.commit()

                return UserModel(
                    id=user.id,
                    username=user.username,
                    email=user.email,
                    password=user.password,
                    person_tax_id=user.person_tax_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
