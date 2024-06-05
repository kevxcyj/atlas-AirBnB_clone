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
            number_bathrooms)(int): number of bathrooms
            max_guest(int): max # of guests
            price_by_night(int): price per night
            latitude(float): 0.0
            longitude(float): 0.0
            amenity_ids(str): list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
