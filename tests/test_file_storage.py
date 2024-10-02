#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_user = User()
storage.new(my_user)
my_user.first_name = "First"
my_user.last_name = "User"
my_user.email = "first_user@e.mail"
my_user.password = "password"
storage.save()
print(my_user)
