from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Person(Base):
    """Entidade Pessoas"""

    __tablename__ = "people"

    tax_id_number = Column(String(14), primary_key=True)
    name = Column(String(50), nullable=False)
    neighborhood = Column(String(20), nullable=False)
    province = Column(String(20), nullable=False)
    street = Column(String(50), nullable=False)
    postal_code = Column(String(10), nullable=False)
    user_id = relationship("Users", uselist=False, back_populates="person")

    def __rep__(self):
        return f"Person: [name={self.name}]"
