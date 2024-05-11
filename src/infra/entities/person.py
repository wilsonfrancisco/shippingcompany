from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Person(Base):
    """Person Entity"""

    __tablename__ = "people"

    tax_id_number = Column(String(14), primary_key=True)
    name = Column(String(50), nullable=False)
    neighborhood = Column(String(20), nullable=False)
    province = Column(String(20), nullable=False)
    street = Column(String(50), nullable=False)
    postal_code = Column(String(10), nullable=False)
    user_id = relationship("User", uselist=False, back_populates="person")

    def __rep__(self):
        return f"Person: [name={self.name}]"

    def __eq__(self, other):
        if self.tax_id_number == other.tax_id_number:
            return True

        return False
