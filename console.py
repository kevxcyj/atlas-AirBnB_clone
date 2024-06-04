#!/usr/bin/python3
""" Contains the entry point of the command interperter """
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
import models

current_classes = {'BaseModel': BaseModel, 'User': User,
                    'Amenity': Amenity, 'City': City, 'State': State,
                    'Place': Place}

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def handle_empty_line(self):
        """ Handles empty lines """
        pass

    def do_quit(self, line):
        """ Command to exit program """
        return True

    def do_EOF(self, line):
        """" Command to exit the program on EOF """
        return True

    def do_create(self, line):
        args = line.split()
        if len(args)!= 1:
            print("** class name missing **")
            return
        className = args[0]
        if className not in storage.classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()
            

    def do_show(self, line):
        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        className = args[0]
        if className not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 3:
            print("** instance id missing **")
            return
        objectId = args[1]
        obj = storage.get(className, objectId)
        if obj is None:
            print("** no instance found **")
            return
        print(str(obj))

    def do_destroy(self, args):
        if len(args) < 2:
            print("** class name missing **")
            return
        className, id = args[:2]
        if className not in self.storage.classes:
            print("** class doesn't exist **")
            return
        if id not in self.storage.instances[className]:
            print("** no instance found **")
            return
        del self.storage.instances[className][id]

    def do_all(self, args):
        if len(args) > 0 and args[0]!= "BaseModel":
            print("** class doesn't exist **")
            return
        for className in self.storage.classes:
            for obj_id, obj in self.storage.instances[className].items():
                print("[{}] ({}) {}".format(className, obj_id, obj)) 

    def do_update(self,args):
        if len(args) < 3:
            print("** class name missing **")
            return
        className, id, attr_name, attr_value = args[:4]
        if className not in self.storage.classes:
            print("** class doesn't exist **")
            return
        if id not in self.storage.classes:
            print(" ** no instance found **")
            return
        if attr_name not in self.storage.instances[className][id]:
            print("** attribute name missing **")
            return

        self.storage.instances[className][id][attr_name] = attr_value
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
