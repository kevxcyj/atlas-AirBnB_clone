#!/bin/usr/python3
"""city class module"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class inheriting from BaseModel

        attributes:
            state_id(str):will be State.id
            name(str): name of city
    """
    state_id = ""
    name = ""
