#!/usr/bin/env python3
"""
exercise.py: module to basis redis
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    decorator count_calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        execute redis incr to count # executes of
        a function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    decorator count_calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        store the history of inputs and outputs for a particular function.
        """
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(res))
        return res
    return wrapper


def replay(fn: Callable):
    """
    function to display the history of calls of a particular function.
    """
    namelisti = f"{fn.__qualname__}:inputs"
    namelisto = f"{fn.__qualname__}:outputs"
    listi = fn.__self__._redis.lrange(namelisti, 0, -1)
    listo = fn.__self__._redis.lrange(namelisto, 0, -1)
    Q = fn.__self__._redis.get(fn.__qualname__).decode('utf8')
    print(f"{fn.__qualname__} was called {Q} times:")

    for a, b in list(zip(listi, listo)):
        attr, result = a.decode("utf-8"), b.decode("utf-8")
        print(f"{fn.__qualname__}(*{attr}) -> {result}")


class Cache:
    """
    Cache class.
    """
    def __init__(self):
        """
        store an instance of the Redis client as a private variable named
        _redis and flush the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid)
        store the input data in Redis using the random key and return the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes,
                                                          int, float]:
        """
        method that take a key string argument and an optional
        Callable argument named fn. This callable will be used
        to convert the data back to the desired format
        """
        kvalue = self._redis.get(key)
        value = kvalue
        if kvalue and fn:
            value = fn(kvalue)
        return value

    def get_str(self, key: str) -> str:
        """
        get_str
        """
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        get_int
        """
        return self._redis.get(key).decode("utf-8")
