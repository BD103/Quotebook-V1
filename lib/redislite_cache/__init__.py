import os.path
import pickle

from flask_caching import BaseCache
from redislite import Redis


def encode(o):
    return pickle.dumps(o, protocol=pickle.HIGHEST_PROTOCOL)


def decode(o):
    return pickle.loads(o)


class RedisliteCache(BaseCache):
    def __init__(self, redis_location, default_timeout=300):
        super().__init__(default_timeout=default_timeout)
        self._redis = Redis(redis_location)

    @classmethod
    def factory(cls, app, config, args, kwargs):
        # Use os.path.join(app.instance_path, "cache.db")
        # for saving the database
        app.config.setdefault("CACHE_REDISLITE_LOCATION", None)

        return cls(app.config["CACHE_REDISLITE_LOCATION"], *kwargs)

    def get(self, key):
        res = self._redis.get(key)

        if res is not None:
            return decode(res)

        return None

    def set(self, key, value, timeout=None):
        if timeout == 0:
            timeout = None

        self._redis.set(key, encode(value), ex=timeout)

    def add(self, key, value, timeout=None):
        if self._redis.exists(key):
            return False

        if timeout == 0:
            timeout = None

        self._redis.set(key, encode(value), ex=timeout)
        return True

    def delete(self, key):
        self._redis.delete(key)
        return True

    def has(self, key):
        return self._redis.exists(key)

    def clear(self):
        self._redis.flushdb()
        return True
