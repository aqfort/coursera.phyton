import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result
    return wrapped

@to_json
def get_data():
  return {
    'data': 42
  }
  
print(get_data())  # вернёт '{"data": 42}'

"""
import functools
import json


def to_json(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped
"""
