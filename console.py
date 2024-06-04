#!/usr/bin/python3
""" Contains the entry point of the command interperter """
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def default(self, line):
        """ Handles empty lines """
        return False

    def do_quit(self, line):
        """ Command to exit program """
        return True

    def do_EOF(self, line):
        """" Command to exit the program on EOF """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
