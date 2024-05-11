from src.infra.config.db_config import DBConnectionHandler
from src.data.interfaces import UserRepositoryInterface
from src.infra.entities import User
from src.domain.models import UserData, User as UserModel


class UserRepository(UserRepositoryInterface):
    """User Repository"""

    def add(self, data: UserData) -> UserModel:
        """Add a new user entity

        :param - username: User username
        :param - email: User email
        :param - password: User password
        :param - tax_id_number: Person tax_id_number

        :return a new user
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

    def get_by_id(self, user_id: int) -> UserModel:
        """Get a user by passing the user id

        :param - user_id: User identifier
        :return: A user entity
        """
        with DBConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(User)
                    .filter_by(id=user_id)
                    .one_or_none()
                )

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

    def get_by_username(self, username: str) -> UserModel:
        """Get a user by passing the username

        :param - username: The username
        :return: A user entity
        """
        with DBConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(User)
                    .filter_by(username=username)
                    .one_or_none()
                )

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

    def get_by_email(self, email: str) -> UserModel:
        """Get a user by passing the user email

        :param - email: User email
        :return: A user entity
        """
        with DBConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(User)
                    .filter_by(email=email)
                    .one_or_none()
                )

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
