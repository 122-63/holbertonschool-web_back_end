#!/usr/bin/env python3
"""
    String Redis
"""
import redis
from uuid import uuid4
from typing import Union
from functools import wraps


class Cache:
    """ Functionality Redis """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Store the cache
            Args:
                data: bring the information to store
            Return:
                Key or number uuid
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key