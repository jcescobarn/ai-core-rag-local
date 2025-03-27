from llama_cpp import Llama
from app.domain.interfaces import LLMInterface
from app.domain.models import Prompt,LLMResponse
from app.core.config import settings

class LLMLocal(LLMInterface):
    def __init__(self, model_path):
       self.model = Llama(
           model_path=settings.model_path,
           n_ctx=2048,
           n_threads=4,
           n_gpu_layers=0,
           verbose=True
       ) 
    
    def generate_response(self, prompt: Prompt) -> LLMResponse:
        result = self.model(
            prompt=prompt.user_query,
            max_tokens=512,
            stop=["User:", "AI:"]
        )
        text = result["choices"][0]["text"]
        return LLMResponse(
            generated_text=text.strip(),
            model_name="llama-cpp"
        )