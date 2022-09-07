import logging
from functools import wraps


def loggable(func):
    name = func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(f'{name} -> args: {args}, kwargs {kwargs}')
        return func(*args, **kwargs)

    return wrapper
