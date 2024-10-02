#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        objects_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                objects_dict = json.load(f)
                for key, obj_dict in objects_dict.items():
                    cls = eval(obj_dict['__class__'])
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
