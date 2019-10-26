from .models import *


def add_email(email):
    """
    Add email to the database.

    :param email: str
    :return:
    """
    Email.objects.create(
        email=email
    )


def add_hack(hack_dict):
    """
    Add hack to the database.

    :param hack_dict: dict
    :return:
    """
    for hack in hack_dict:
        print(hack)
