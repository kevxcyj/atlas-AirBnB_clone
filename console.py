#!/bin/usr/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def default(self, line):
        """ """
        pass

    def do_quit(self, arg):
        """ Command to exit program """
        return True

    def do_EOF(self, arg):
        """" Command to exit the program on EOF """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
