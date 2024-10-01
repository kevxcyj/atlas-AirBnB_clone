#!/usr/bin/python3
" Entry for command interperter "
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_create(self, arg):
        try:
            cls = eval(arg)
            obj = cls()
            storage.new(obj)
            storage.save()
            print(f"{obj.id}")
        except NameError:
            print("** class doesn't exist **")
        except Exception as e:
            print(f"{e}")



    def do_EOF(self, arg):
        """ End of file """
        print()
        return True
    
    def do_quit(self, arg):
        """ Quit Command """
        return True
    
    def postcmd(self, stop, arg):
        if stop:
            return stop
        return False
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
