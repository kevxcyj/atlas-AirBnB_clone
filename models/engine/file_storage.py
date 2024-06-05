#!/usr/bin/python3
"""Module: FileStorage class methods and attributes for serializing and
    and deserializng object instances/json files"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """class FileStorage

        attributes:
            __file_path: path to/name of json file
            __objects: dictionary, keys/instances of objects to be converted
    """

    def __init__(self, file_path='file.json', objects={}):
        self.__file_path = file_path
        self.__objects = objects
        self.classes = {}

    """methods/setters/getters"""

    def all(self):
        """returns the object dictionaries"""
        return self.__objects

    def new(self, obj):
        """sets an object to the dictionary.

            variables:
                obj(class instance): instance of a class
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """ writes the json str representation to classname.json """
        obj_dict = dict()
        for key, value in self.__objects.items():
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(obj_dict))

    def reload(self):
        """ it deserializes the json file back into a dictionary."""
        try:
            with open(self.__file_path, "r") as file:
                json_str = file.read()
                loaded_data = json.loads(json_str)
                self.__objects.clear()
                for key, value in loaded_data.items():
                    class_name, obj_id = key.split('.')
                    class_instance = globals()[class_name](**value)
                    self.__objects[key] = class_instance
        except FileNotFoundError:
            pass
