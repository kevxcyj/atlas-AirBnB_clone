#!/bin/usr/python3
""" state class module """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class

        attributes:
            name(str): name of state
    """
    name = ""
