# wget https://download.redis.io/releases/redis-6.2.5.tar.gz
# tar xzf redis-6.2.5.tar.gz
# cd redis-6.2.5
# make

# src/redis-server

# src/redis-cli
# redis> set foo bar
# redis> get foo


import redis

host = "localhost"
port  = 6379

def redis_string():
    try:
        r = redis.StrictRedis(
            host = host,
            port = port,
            decode_responses= True
        )
        r.set("message",{"a":1})
        msg = r.get("message")
        print(msg)
    except Exception as e:
        print(e)

redis_string()
