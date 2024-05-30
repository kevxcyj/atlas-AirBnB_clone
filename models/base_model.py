import datetime



class BaseModel:

self.id = str(uuid.uuid4())
self.created_at = datetime.datetime.now().isoformat()
self.updated_at = datetime.datetime.now().isoformat()




def __init__(self, id=none, created_at, updated_at):
    pass


def __str__(self):
    pass

def save(self)
self.updated_at = datetime.now().isoformat()




if kwargs:
    excluded_keys = ['__class__']
    for key, value in kwargs,items():
            if key not in excluded_keys:
                if isinstance(value, str) and (key == 'created_at' or key == 'updated_at'):
                    value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            setattr(self, key, value)

        else 

            