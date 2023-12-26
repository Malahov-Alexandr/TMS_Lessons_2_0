from dataclasses import dataclass
import random
from datetime import datetime
from faker import Faker

fake = Faker()


@dataclass
class Person:
    first_name: str
    last_name: str
    blood_status: str
    born: int


def new_mag():
    data = fake.date_between_dates(date_start=datetime(1995, 1, 1),
                                   date_end=datetime(2000, 12, 31)).year
    blood = random.choice(('Half-blood', 'Muggle-born'))
    return f'"{fake.first_name()}", "{fake.last_name()}", "{blood}", {data}'


def person_format(result):
    if type(result) is tuple:
        return Person(*result)
    else:
        return [Person(*one) for one in result]
