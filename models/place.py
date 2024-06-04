#!/bin/usr/python3
"""place class module """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class inheits from BaseModel

        attributes:
            city_id(str): will be City.id
            user_id(str): will be User.id
            name(str): name of state
            description(str): description of the air bnb
            number_rooms(int): number of rooms in air bnb
    """
    name = ""
