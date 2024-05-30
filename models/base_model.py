#!/usr/bin/python3
""" module: base model class """
import datetime
import uuid

class BaseModel:
    """ BaseModel class that is to be inherited by other models

        Attribute:
            id(str): uuid for unique Identifier
            created_at(str): time it was created
            updated_at(str): time instance was updated
            name(str): name of instance
            my_number(int): number given to instance
    """
    def __init__(self, name=None, my_number=0, created_at=None, updated_at=None, id=None):

        self.name = name
        self.my_number = my_number
        self.id = id if id else str(uuid.uuid4())
        self.created_at = created_at if created_at else datetime.datetime.now().isoformat()
        self.updated_at = updated_at if updated_at else datetime.datetime.now().isoformat()

    """ methods/setters/getters """

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates updated_at attribute"""

        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """ returns dictionary keyword/value representations of attributes"""

        return {
            "name": self.name,
            "my_number": self.my_number,
            "id": self.id,
            "created_at": self.created_at,
            "updated_a t": self.updated_at,
            "__class__": self.__class__.__name__,

        }
