from app.domain.interfaces import MemoryInterface
from app.infrastructure.db import RedisAdapter

class RedisMemory(MemoryInterface):
    def __init__(self):
        self.redis = RedisAdapter()

    def get_context(self, session_id:str) -> str: 
        data = self.redis.get(session_id)
        if data:
            return "\n".join(data.get("history",[]))
        return ""
    
    def save_context(self, session_id:str, message: str):
        data = self.redis.get(session_id) or {"history":[]}
        data["history"].append(message)
        self.redis.set(session_id)
