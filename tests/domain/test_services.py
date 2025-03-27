
from app.domain.models import Prompt
from app.domain.services import build_full_prompt, post_process_llm_response

def test_build_prompt_with_context():
    prompt = Prompt(user_query="¿Qué es DevOps?", context="DevOps es...")
    result = build_full_prompt(prompt)
    assert result.startswith("DevOps es...")

def test_build_prompt_without_context():
    prompt = Prompt(user_query="¿Qué es RAG?")
    result = build_full_prompt(prompt)
    assert result.startswith("User: ¿Qué es RAG?")

def test_post_process_llm_response():
    raw = "\n\nEsta es la respuesta del modelo.   "
    processed = post_process_llm_response(raw)
    assert processed.generated_text == "Esta es la respuesta del modelo."
