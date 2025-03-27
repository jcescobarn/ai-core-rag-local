
from app.domain.models import Prompt, LLMResponse, VectorDocument

def test_prompt_model():
    prompt = Prompt(user_query="Hola", context="Contexto")
    assert prompt.user_query == "Hola"
    assert prompt.context == "Contexto"

def test_llm_response_model():
    response = LLMResponse(generated_text="Texto generado", model_name="llama-cpp")
    assert response.generated_text == "Texto generado"
    assert response.model_name == "llama-cpp"

def test_vector_document_model():
    doc = VectorDocument(id="1", content="Contenido")
    assert doc.id == "1"
    assert doc.content == "Contenido"
