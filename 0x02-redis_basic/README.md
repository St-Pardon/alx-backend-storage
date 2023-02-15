# 0x02. Redis basic

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/40eab4627f1bea7dfe5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230215%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230215T181752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=822d03d50e472048b6295af1627606c8bdf5d3c998a9e46773f009de2e6215c2)

## Resourses

- [Redis commands](https://redis.io/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)


## Install Redis on Ubuntu 18.04
```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```


## Tasks
### [0. Writing strings to Redis](./exercise.py)

Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.

Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g. using `uuid`), store the input data in Redis using the random key and return the key.

Type-annotate `store` correctly. Remember that `data` can be a `str`, `bytes`, `int` or `float`.
```bash
user@ubuntu:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

user@ubuntu:~$ python3 main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
user@ubuntu:~$ 
```


### [1. Reading from Redis and recovering original type](./exercise.py)
mandatory
Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a `byte` string. Hence if you store `"a"` as a `UTF-8` string, it will be returned as `b"a"` when retrieved from the server.

In this exercise we will create a `get` method that take a key string argument and an optional Callable argument named fn. This `callable` will be used to convert the data back to the desired format.

Remember to conserve the original `Redis.get` behavior if the key does not exist.

Also, implement 2 new methods: `get_str` and `get_int` that will automatically parametrize `Cache.get` with the correct conversion function.

The following code should not raise:
```py
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```