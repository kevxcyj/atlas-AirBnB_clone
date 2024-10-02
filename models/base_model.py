#!/usr/bin/python3
""" BaseModel class """
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for HBNB models

    Attributes:
        id (str): Unique identifier for the model instance
        created_at (datetime): Timestamp when the instance is created
        updated_at (datetime): Timestamp when the instance is updated

    """

    def __init__(self, *args, **kwargs):
        """ 
        Initializes a BaseModel instance 
        
        Args:
            *args: Variable number of positional arguments
            **kwargs: Keyworded variable number of kkeyword arguments
        
        """
        if args:
            raise TypeError("__init__() takes no positional arguments")
        
        if kwargs:
            self.__dict__.update(kwargs)
        if 'created_at' in kwargs:
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
        if 'updated_at' in kwargs:
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

            models.storage.new(self)


    def save(self):
        """ Updates updated_at with time """
        self.updated_at = datetime.now().isoformat()
        models.storage.save()

    def to_dict(self):
        """ Converts instance to dictionary """
        return {
            "__class__": self.__class__.__name__,
            **self.__dict__
            
        }

    def __str__(self):
        """ Returns a string representation of object """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
