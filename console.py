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


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    current_classes = {'BaseModel', 'User',
                    'Amenity', 'City', 'State',
                    'Place'}

    def handle_empty_line(self):
        """ Handles empty lines """
        pass

    def do_quit(self, line):
        """ Command to exit program """
        return True

    def help_quit(self, arg):
        """
        """
        print("Quit command to exit the program")   

    def do_EOF(self, line):
        """" Command to exit the program on EOF """
        return True
    
    def do_create(self, line):
        args = line.split()
        if len(args)!= 1:
            print("** class name missing **")
            return
        className = args[0]
        if className not in HBNBCommand.current_classes:
            print("** class doesn't exist **")
            return
        else:
            storage.save()
            print(eval(args[0])().id)

    def do_show(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        className = args[0]
        if className not in HBNBCommand.current_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objectId = args[1]
        key = f'{className}.{objectId}'
        obj = storage.all()
        if key not in obj:
            print("** no instance found **")
            return
        print(str(obj))

    def do_destroy(self, args):
        if len(args) < 2:
            print("** class name missing **")
            return
        className, id = args[:2]
        if className not in HBNBCommand.current_classes:
            print("** class doesn't exist **")
            return
        if id not in self.storage.instances[className]:
            print("** no instance found **")
            return
        del self.storage.instances[className][id]

    def do_all(self, args):
        instances = storage.all()
        if len(args) == 0:
            for instance_id in instances.keys():
                print(f"{instances[instance_id]}")
        else:
            arg = args.split()

            if len(arg) > 0:
                className = arg[0]
                if className in HBNBCommand.current_classes:
                    for instance_id in instances.keys():
                        if instances[instance_id].__class__.__name__ == className:
                            print(f"{instances[instance_id]}")
                else:
                    print("** class doesn't exist **")
                    return

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
