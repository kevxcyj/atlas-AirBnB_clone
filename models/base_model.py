#!/usr/bin/python3

import uuid
from datetime import datetime
import models
from models.engine.file_storage import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
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

            storage.new(self)


    def save(self):
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        return {
            "__class__": self.__class__.__name__,
            **self.__dict__
        }

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"