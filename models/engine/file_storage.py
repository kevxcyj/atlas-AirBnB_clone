#!/usr/bin/python3
"""Module: FileStorage class methods and attributes for serializing and
    and deserializng object instances/json files"""
import json
import os

class FileStorage:
    """class FileStorage

        attributes:
            __file_path: path to/name of json file
            __objects: dictionary, keys/instances of objects to be converted
    """

    def __init__(self, file_path="", objects={}):
        self.__file_path = file_path
        self.__objects = objects

        """methods/setters/getters"""

    def all(self):
        """returns the object dictionaries"""
        return self.__objects
    
    def new(self, obj):
        """sets an object to the dictionary.
        
            variables:
                obj(class instance): instance of a class
        """
        self.__objects = {obj.__class__.__name__.id: obj}

    def save(self):
        """ writes the json str representation to classname.json """
        file = self.__file_path
        with open(file, "w") as f:
              json.dump(list(self.__objects.values()), f)

    def reload(self):
        """ it deserializes the json file back into a dictionary."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                json_str = file.read()
                list_dicts = json.loads(json_str)
                for dict in list_dicts:
                    self.__objects.update(dict)
        else:
            pass
