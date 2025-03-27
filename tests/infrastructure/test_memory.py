
from app.infrastructure.memory import RedisMemory

def test_memory_save_and_get(monkeypatch):
    class FakeRedis:
        def __init__(self):
            self.store = {}

        def get(self, key):
            return self.store.get(key)

        def set(self, key, value, ex=None):
            self.store[key] = value

    memory = RedisMemory()
    memory.redis.redis = FakeRedis()

    session_id = "session1"
    memory.save_context(session_id, "Hola")
    context = memory.get_context(session_id)
    assert "Hola" in context
