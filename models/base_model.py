#!/usr/bin/python3
""" module: base model class """
import datetime
import uuid
import models


class BaseModel:
    """ BaseModel class that is to be inherited by other models

        Attribute:
            id(str): uuid for unique Identifier
            created_at(str): time it was created
            updated_at(str): time instance was updated
            name(str): name of instance
            my_number(int): number given to instance
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            excluded_keys = ['__class__']
            for key, value in kwargs.items():
                if key not in excluded_keys:
                    if isinstance(value, str) and (key == 'created_at' or 
                                                   key == 'updated_at'):
                        value = datetime.datetime.fromisoformat(value)
                    setattr(self, key, value)

        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    """ methods/setters/getters """

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_at attribute"""

        self.updated_at = datetime.datetime.now()

        """ Import storage and save method """
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns dictionary keyword/value representations of attributes"""

        return {
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "id": self.id,
            "created_at": self.created_at.isoformat(),

        }
