#!/usr/bin/python3

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        print()
        return True
    
    def do_quit(self, arg):
        return True
    
    def postcmd(self, stop, arg):
        if stop:
            return stop
        return False
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
