from dataclasses import dataclass
from collections import namedtuple


@dataclass
class UserData:
    """User Data"""

    username: str
    email: str
    password: str
    person_tax_id: str


User = namedtuple("User", "id, username, email, password, person_tax_id")
