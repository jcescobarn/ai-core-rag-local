from app.domain.interfaces import VectorStoreInterface
from app.domain.models import Prompt

class RAGService:
    """
    Servicio encargado de realizar la busqueda de contexto 
    relevante en la base vectorial (RAG) 
    """

    def __init__(self, vector_store: VectorStoreInterface):
        self.vector_store = vector_store
    
    def retrieve_context(self, prompt: Prompt, top_k: int = 3) -> str:
        """
        Realiza la busqueda semántica y devuelve un string con los textos relevantes 
        """

        documents = self.vector_store.query(prompt.user_query, top_k=top_k)
        context = "\n---\n".join([doc.content for doc in documents])
        prompt.context = context
        return context