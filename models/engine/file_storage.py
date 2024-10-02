#!/usr/bin/python3
""" Initalizing file_storage """
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ Class for serializing instances to a JSON file 
    
    Attributes:
        __file_path (str): Path to JSON where files start
        __objects (dict): Dictionary containing instanced objects
    
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary objects """
        return self.__objects
    
    def new(self, obj):
        """ Adds new object to dictionary """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Serializes object to JSON file """
        objects_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """ Deserializes JSON file """
        try:
            with open(self.__file_path, "r") as f:
                objects_dict = json.load(f)
                for key, obj_dict in objects_dict.items():
                    cls = eval(obj_dict['__class__'])
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
