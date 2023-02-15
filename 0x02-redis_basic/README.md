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
