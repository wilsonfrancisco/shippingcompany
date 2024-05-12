from faker import Faker
from src.domain.models import Person

faker = Faker()


def mock_person() -> Person:
    """Utility method to mock a person"""

    return Person(
        tax_id_number=faker.ssn(),
        name=faker.name(),
        neighborhood=faker.city_suffix(),
        province=faker.city(),
        street=faker.street_suffix(),
        postal_code=faker.postalcode(),
    )
