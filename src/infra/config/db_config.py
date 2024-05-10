import urllib.parse
from sqlalchemy import create_engine


class DBConnectionHandler:
    """SqlAlchemy (ORM) database connection"""

    def __init__(self) -> None:
        db_password = urllib.parse.quote_plus("wilson@mysql")
        self.__connection_string = (
            f"mysql+pymysql://root:{db_password}@172.17.0.2/shippingcompany"
        )
        self.session = None

    def get_engine(self):
        """Return connection engine
        :param - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine
