
import pytest
from app.application.llm_service import LLMService
from app.domain.models import Prompt, LLMResponse

class DummyLLM:
    def generate_response(self, prompt: Prompt):
        return LLMResponse(generated_text=f"Echo: {prompt.user_query}")

class DummyRAG:
    def retrieve_context(self, prompt: Prompt):
        return "Contexto simulado"

@pytest.fixture
def llm_service():
    return LLMService(llm_adapter=DummyLLM(), vector_db=DummyRAG())

def test_ask_direct(llm_service):
    response = llm_service.ask_direct("¿Qué es un LLM?")
    assert "Echo" in response.generated_text

def test_ask_with_rag(llm_service):
    response = llm_service.ask_with_rag("¿Qué es RAG?")
    assert "Echo" in response.generated_text
