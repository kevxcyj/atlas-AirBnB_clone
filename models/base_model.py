#!/usr/bin/python3

import uuid
import datetime


class BaseModel:

def __init__(self):
    self.id = str(uuid.uuid4())
    self.created_at = datetime.now().isoformat()
    self.updated_at = datetime.now().isoformat()


def save(self):
    self.updated_at = datetime.now().isoformat()

def to_dict(self):
    return {
        "__class__": self.__class__.__name__,
        **self.__dict__
    }
