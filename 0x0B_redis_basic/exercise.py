#!/usr/bin/env python3
"""
exercise.py: module to basis redis
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """
    decorator count_calls
    """
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """
        execute redis incr to count # executes of
        a function
        """
        self._redis.incr(fn.__qualname__)
        return fn(self, *args, **kwargs)
    return wrapper


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
