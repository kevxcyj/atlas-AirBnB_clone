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




