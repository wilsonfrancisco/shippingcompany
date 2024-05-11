from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.config import Base


class User(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    person_tax_id = Column(String(14), ForeignKey("people.tax_id_number"))
    person = relationship("Person", back_populates="user_id")

    def __rep__(self):
        return f"Usr: [username={self.username}, tax_id_number={self.person}]"

    def __eq__(self, other):
        if (
            self.username == other.username
            and self.email == other.email
            and self.password == other.password
        ):
            return True

        return False
