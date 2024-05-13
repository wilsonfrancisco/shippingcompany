from faker import Faker
from src.domain.models import UserData

faker = Faker()


def mock_user():
    """Utility class to mock a user"""

    return UserData(
        email=faker.email(),
        password=faker.word(),
        username=faker.name(),
        person_tax_id=faker.ssn(),
    )
