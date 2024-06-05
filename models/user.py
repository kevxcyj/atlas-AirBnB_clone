#!/usr/bin/python3
""" user class module """
from models.base_model import BaseModel


class User(BaseModel):
    """ class User inheriting from BaseModel

        attributes:
            email(str): email of a user
            password(str): password of a user
            first_name(str): first name of a user
            last_name(str): last name of a user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
