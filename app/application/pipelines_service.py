from typing import List
from app.domain.models import VectorDocument
from app.domain.interfaces import VectorStoreInterface

class IngestionPipeline:
    """
    Pipeline responsable de recibir datos crudos
    procesarlos y almacenarlos como embeddings en la vector store.
    """

    def __init__(self, vector_store: VectorStoreInterface):
        self.vector_store = vector_store

    def process_documents(self, raw_documents: List[str], metadata:dict = None) -> List[VectorDocument]:
        """
        Procesa una lista de documentos crudos y los almacena en la vector store.
        """
        vector_documents = []
        for idx, content in enumerate(raw_documents):
            doc = VectorDocument(
                id=f"doc-{idx}",
                content=content,
                metadata=metadata or {}
            )
            vector_documents.append(doc)
        return vector_documents