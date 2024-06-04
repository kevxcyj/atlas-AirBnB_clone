#!/bin/usr/python3
""" amenity class module """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class inherits from BaseModel

        attributes:
            name(str): name of amenity
    """
    name = ""
