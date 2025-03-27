from pydantic import BaseModel
from typing import List, Optional

class Prompt(BaseModel):
    user_query: str
    context: Optional[str] = None

class LLMResponse(BaseModel):
    generated_text: str
    tokens_used: Optional[int] = None
    model_name : Optional[str] = None

class VectorDocument(BaseModel):
    id: str
    content: str
    metadata: Optional[dict] = None

class SessionContext(BaseModel):
    session_id: str
    conversation_history: List[str]
    user_id: Optional[str] = None