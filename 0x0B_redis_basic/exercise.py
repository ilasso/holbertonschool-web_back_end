#!/usr/bin/env python3
"""
exercise.py: module to basis redis
"""
from redis.client import Redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """
    Cache class.
    """
    def __init__(self):
        """
        store an instance of the Redis client as a private variable named
        _redis and flush the instance using flushdb
        """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key and return the key
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

# a = Cache()
# print(a.store("hola,mundo"))
