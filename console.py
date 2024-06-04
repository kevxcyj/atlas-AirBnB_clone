#!/usr/bin/python3
""" Contains the entry point of the command interperter """
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def handle_empty_line(self, line):
        """ Handles empty lines """
        return False

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
            return
        obj = storage.new(className)
        obj.save()
        print(obj.id)

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
