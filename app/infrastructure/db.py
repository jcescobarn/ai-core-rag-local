import redis
import json
from app.core.config import settings

class RedisAdapter:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db
        )

    def set(self, key, value):
        self.client.set(key, json.dumps(value))

    def get(self, key):
        value = self.client.get(key)
        return json.loads(value) if value else None

    def delete(self, key):
        self.client.delete(key)