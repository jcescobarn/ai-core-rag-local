import openai
from app.domain.models import Prompt, LLMResponse
from app.domain.interfaces import LLMInterface
from app.core.config import settings 

openai.api_key = settings.openai_api_key

class OpenAILLM(LLMInterface):
    def generate_response(self, prompt: Prompt) -> LLMResponse:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt.system_message},
                {"role": "user", "content": prompt.user_query}
            ]
        )
        content = response.choices[0].message["content"]
        tokens = response["usage"]["total_tokens"]
        return LLMResponse(generated_text=content, tokens_used=tokens ,model_name="openai/gpt-3.5-turbo")