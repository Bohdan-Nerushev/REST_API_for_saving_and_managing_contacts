import redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def cache_set(key, value):
    redis_client.set(key, value)

def cache_get(key):
    return redis_client.get(key)
