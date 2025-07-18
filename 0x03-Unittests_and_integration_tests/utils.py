# utils.py

def access_nested_map(nested_map, path):
    """Access a nested map with a sequence of keys."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map

import requests

def get_json(url):
    return requests.get(url).json()

# utils.py
def memoize(method):
    """Memoization decorator for methods"""
    attr_name = "_{}".format(method.__name__)

    @property
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return wrapper
