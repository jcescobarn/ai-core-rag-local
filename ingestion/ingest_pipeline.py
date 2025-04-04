from pathlib import Path
from uuid import uuid4

from loader import load_file
from splitter import split_text
from embedder import Embedder
from app.domain.models import VectorDocument
from app.infrastructure.vector_store import ChromaVectorStore

def ingest_document(file_path: str, metadata: dict = None):
    """
    Ingest a document by loading, splitting, embedding, and storing it in a vector store.

    Args:
        file_path (str): Path to the document file.
        metadata (dict, optional): Metadata to associate with the document. Defaults to None.
    """
    # Load the document
    document = load_file(file_path)
    
    # Split the document into chunks
    chunks = split_text(document)
    
    # Embed the chunks
    embedder = Embedder()
    embeddings = embedder.embed(chunks)
    
    # Store the embeddings in a vector store
    vector_store = ChromaVectorStore()
    
    docs = [
        VectorDocument(
            id=str(uuid4()),
            embedding=embedding,
            metadata=metadata or {'source': Path(file_path).name},
            content=chunk,
        )
        for chunk, embedding in zip(chunks, embeddings)
    ]

    vector_store.upsert(docs)
    print(f"Document {file_path} ingested successfully with {len(docs)} chunks.")