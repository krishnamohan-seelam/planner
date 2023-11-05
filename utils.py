import itertools
next_id = itertools.count()

def get_id():
    return str(next(next_id))