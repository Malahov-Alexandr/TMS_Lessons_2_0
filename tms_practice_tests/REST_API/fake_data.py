from faker import Faker
import string
import random


def password_gen(x):
    password = ''
    for i in range(x):
        password += str(random.randint(1, 9))
    return password


def fake_data(text=None):
    text = text if text is not None else 'en_US'
    fake = Faker(text)
    fake_full_name = fake.name().split()
    username, lastname = fake_full_name
    firstname = 'Black'
    email = fake.email()
    phone = fake.phone_number()
    password = password_gen(5)

    return username, firstname, lastname, email, phone, password
