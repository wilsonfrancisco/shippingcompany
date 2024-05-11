from dataclasses import dataclass
from collections import namedtuple


@dataclass
class PersonData:
    """Person Data"""

    tax_id_number: str
    name: str
    neighborhood: str
    province: str
    street: str
    postal_code: str


Person = namedtuple(
    "User", "tax_id_number, name, neighborhood, province, street, postal_code"
)
