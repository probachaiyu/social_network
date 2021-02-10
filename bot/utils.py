import random
import string

import uuid


class RandomCreator:

    @staticmethod
    def create_password():
        letters = "".join(random.choice(string.ascii_lowercase) for _ in range(5))
        letters_b = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
        numbers = "".join(random.choice(string.digits) for _ in range(3))
        return letters + numbers + letters_b

    @staticmethod
    def get_email():
        return f'{RandomCreator.get_uuid()}@test.com'

    @staticmethod
    def get_uuid():
        return f'{uuid.uuid4()}'


def _prepare_register_data():
    username = RandomCreator.get_uuid()
    password = RandomCreator.create_password()
    data = {"username": username, "password1": password, "password2": password, "email": RandomCreator.get_email()}
    return data, password, username


def _prepare_post_data(user):
    data = {"title": RandomCreator.get_uuid(),
            "body": RandomCreator.get_uuid() * random.randint(1, 10),
            "author": user.id}
    return data
