import itertools
import uuid
next_id = itertools.count()

def get_id():
    return str(next(next_id))

def get_uuid4():
    return str(uuid.uuid4())