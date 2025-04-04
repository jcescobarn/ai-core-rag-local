from sentence_transformers import SentenceTransformer
from typing import List

class Embedder:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Initialize the Embedder with a specified model.

        :param model_name: The name of the SentenceTransformer model to use.
        """
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]) -> List[List[float]]:
        """
        Embed a list of texts into their corresponding vector representations.

        :param texts: A list of strings to be embedded.
        :return: A list of lists, where each inner list is the vector representation of the corresponding text.
        """
        return self.model.encode(texts, convert_to_numpy=True).tolist()