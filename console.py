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
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    current_classes = {'BaseModel',
                       'User',
                       'Amenity',
                       'City',
                       'State',
                       'Place',
                       'Review'
                       }

    def emptyline(self):
        """ Handles empty lines """
        pass

    def do_quit(self, line):
        """ Command to exit program """
        return True

    def help_quit(self, arg):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """ Command to exit the program on EOF """
        return True

    def do_create(self, line):
        """creates an instance of given class

            line(str): user-input command 
                arg[0]: class name
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        className = args[0]
        if className not in HBNBCommand.current_classes:
            print("** class doesn't exist **")
            return
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, line):
        """prints string rep of an instance

            line(str): console-input command
                arg[0]: class name
                arg[1]: instance id
        """
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
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, args):
        """ destroys an instance

            args: console-input command
                args[0]: className
                args[1]: instance id
        """
        arg = args.split()
        instance_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.current_classes:

            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")

        elif f"{arg[0]}.{arg[1]}" not in instance_dict:
            print("** no instance found **")
        else:
            obj_instance = f"{arg[0]}.{arg[1]}"
            del instance_dict[obj_instance]
            storage.save()

    def do_all(self, args):
        """ prints str rep of all instances in a given class
            or all instances in storage.all

            args: console-input command
                args[0]: className
        """
        insts = storage.all()
        if len(args) == 0:
            for instance_id in insts.keys():
                print(f"{insts[instance_id]}")
        else:
            arg = args.split()

            if len(arg) > 0:
                className = arg[0]
                if className in HBNBCommand.current_classes:
                    for instance_id in insts.keys():
                        if insts[instance_id].__class__.__name__ == className:
                            print(f"{insts[instance_id]}")
                else:
                    print("** class doesn't exist **")
                    return

    def do_update(self, arg):
        """updates an instance with values to their given attribute.

            arg: console-input command
                arg[0]: className class name of given instanceId
                arg[1]: instandId of given instance of class
                arg[2]: attr_name of attribute to be set for given instance
                arg[3]: value for the attribute refrenced in attr_name
        """
        args = arg.split()
        instance_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        className, instanceId, attr_name, value = args
        key = f"{className}.{instanceId}"
        instances = storage.all()
        if className not in HBNBCommand.current_classes:
            print("** class doesn't exist **")
            return
        if key not in instances:
            print("** no instance found **")
            return
        instance = instances[key]
        setattr(instance, attr_name, value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
