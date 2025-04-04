import nltk
from typing import List

nltk.download('punkt_tab', quiet=True)

def split_text(text: str, max_tokens: int = 200) -> List[str]:
    """
    Splits the input text into chunks of a specified maximum number of tokens.

    Args:
        text (str): The input text to be split.
        max_tokens (int): The maximum number of tokens per chunk.

    Returns:
        List[str]: A list of text chunks.
    """
    # Tokenize the text into sentences
    from nltk.tokenize import sent_tokenize

    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = [] 

    current_length = 0
    for sentence in sentences:
        sentence_len = len(sentence.split())
        if current_length + sentence_len > max_tokens:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_length = sentence_len
        else:
            current_chunk.append(sentence)
            current_length += sentence_len
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks