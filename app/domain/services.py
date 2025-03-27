from .models import Prompt, LLMResponse

def build_full_prompt(prompt: Prompt) -> str:
    if prompt.context:
        return f"{prompt.context}\n\nUser: {prompt.user_query}\nAI:"
    return f"User: {prompt.user_query}\nAI:"

def post_process_llm_response(raw_response: str) -> LLMResponse:
    """"""
    cleaned = raw_response.strip()
    return LLMResponse(generated_text=cleaned)