#!/usr/binn/env python3
'''Redis module
'''
import redis
from typing import Union
import uuid


class Cache:
    '''a class storing data in a Redis data storage.
    '''
    def __init__(self) -> None:
        '''Initializes a Cache instance.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores a value in Redis storage and returns the uuid.
        '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
