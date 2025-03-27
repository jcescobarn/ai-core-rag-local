from abc import ABC, abstractmethod
from .models import Prompt, VectorDocument, LLMResponse

class LLMInterface(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass

class VectorStoreInterface(ABC):
    @abstractmethod
    def query(self, query_text: str, top_k: int = 3) -> list[VectorDocument]:
        """Recupera documentos relevantes del vector store"""
        pass
    
    @abstractmethod
    def upsert(self, documents: list[VectorDocument]):
        """Agrega nuevos documentos al vector store"""
        pass

class MemoryInterface(ABC):
    @abstractmethod
    def get_cotext(self, session_id: str) -> str:
        """Recupera el contecto historico de la conversación"""
        pass
    
    @abstractmethod
    def save_context(self, session_id: str, message: str):
        """Guarda un nuevo mensaje en la memoria de conversación"""
        pass
