#!/bin/usr/python3
"""review class module"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class inherits from BaseModel

        attributes:
            place_id(str): Place.id is what it will become
            user_id(str): user.id is what this will become
            text(str): probably review from a customer.
    """
    place_id = ""
    user_id = ""
    text = ""