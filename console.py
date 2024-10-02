#!/usr/bin/python3
" Entry for command interperter "
import cmd
from models import storage
from models.user import User


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

    def do_all(self, arg):
        """ Prints string representations based on class name  """
        try:
            cls_name = arg.split()[0]
            print([obj for obj in storage.all().values() if isinstance(obj, eval(cls_name))])
        except NameError:
            print("[BaseModel] " + "\n".join([str(obj) for obj in storage.all().values()]))

    def do_show(self, arg):
        """ Prints string representaion based on class/id """
        try:
            cls_name, obj_id = arg.split()
            obj = storage.all()[f"{cls_name}.{obj_id}"]
            print(obj)
        except KeyError:
            print("** no instance found **")
        except Exception as e:
            print(f"{e}")
            
    def do_destroy(self, arg):
        try:
            cls_name, obj_id = arg.split()
            storage.delete(storage.all()[f"{cls_name}.{obj_id}"])
            storage.save()
        except KeyError:
            print("** no instance found **")
        except Exception as e:
            print(f"{e}")

    def do_update(self, arg):
        """ Updates instance """
        try:
            cls_name, obj_id, attr_name, value = arg.split()
            obj = storage.all()[f"{cls_name}.{obj_id}"]
            setattr(obj, attr_name, eval(value))
            storage.save()
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute doesn't exist **")
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

