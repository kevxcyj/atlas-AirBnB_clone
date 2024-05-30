#!/usr/bin/python3
""" module: base model class """
import datetime

class BaseModel:
    """ BaseModel class that is to be inherited by other models

        Attribute:
            id(str): uuid for unique Identifier
            created_at(str): time it was created
            updated_at(str): time instance was updated
    """
    def __init__(self, id=None, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    """ methods/setters/getters """

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict}"
    
    def save(self):
        """updates updated_at attribute"""

        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """ returns dictionary keyword/value representations of attributes"""

        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_a t": self.updated_at,
            "__class__": self.__class__.__name__,
