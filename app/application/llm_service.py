from app.domain.interfaces import LLMInterface, VectorStoreInterface
from app.domain.models import Prompt, LLMResponse
from app.domain.services import build_full_prompt, post_process_llm_response
from app.application.rag_service import RAGService

class LLMService:
    def __init__(self, llm_adapter: LLMInterface, vector_db: VectorStoreInterface):
        self.llm_adapter = llm_adapter
        self.rag = RAGService(vector_db)

    def ask_direct(self, query_text: str) -> LLMResponse:
        """
        Pregunta directa al LLM, sin recuperación RAG. 
        """

        prompt = Prompt(user_query=query_text)
        full_prompt = build_full_prompt(prompt)
        raw_response = self.llm_adapter.generate_response(Prompt(user_query=full_prompt))
        return post_process_llm_response(raw_response.generated_text) 
    
    def ask_with_rag(self, query_text: str) -> LLMResponse:
        """
        Flujo completo: busca contexto con RAG y responde con LLM 
        """

        # Paso 1: busca contexto con RAG y responde con LLM
        prompt = Prompt(user_query=query_text)

        # Paso 2: Recuperar contexto (si hay)
        context = self.rag.retrieve_context(prompt)
        prompt.context = context

        # Paso 3: Construir el prompt final
        full_prompt = build_full_prompt(prompt)

        raw_response = self.llm_adapter.generate_response(Prompt(user_query=full_prompt))

        # Paso 5: Preprocesar la respuesta
        return post_process_llm_response(raw_response.generated_text)