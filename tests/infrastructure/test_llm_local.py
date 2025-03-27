
import pytest
from app.infrastructure.llm_local import LLMLocal
from app.domain.models import Prompt

def test_llm_local_generates_response():
    llm = LLMLocal()
    prompt = Prompt(user_query="Hola")
    response = llm.generate_response(prompt)
    assert isinstance(response.generated_text, str)
    assert len(response.generated_text) > 0
