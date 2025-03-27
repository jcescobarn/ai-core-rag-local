from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):

    #Seguridad
    api_key: str = Field(..., env='API_KEY')

    # LLM Config (si usas local o remoto)
    model_path: str = Field(default="mistralai/Mistral-7B-instruct-v0.2", env='MODEL_PATH')
    llm_provider: str = Field(default="local", env='LLM_PROVIDER')

    #Vector Store
    vector_db_provider: str = Field(default="chroma", env='VECTOR_DB_PROVIDER')
    vector_db_uri: str = Field(default="localhost:8000", env='VECTOR_DB_URI')
    pinecone_api_key: str = Field(default=None, env="PINECONE_API_KEY")
    pinecone_env: str = Field(default=None, env="PINECONE_ENV")
    pinecone_index: str = Field(default=None, env="PINECONE_INDEX")

    #redis / memoria
    redis_host: str = Field(default="localhost", env="REDIS_HOST")
    redis_port: int = Field(default=6379, env="REDIS_PORT")
    redis_db: int = Field(default=0, env="REDIS_DB")

    # Rutas
    data_path: str = Field(default="./data", env="DATA_PATH")
    embeddings_model:str = Field(default="all-MiniLM-L6-v2", env="EMBEDDINGS_MODEL")

    #General
    environment: str = Field(default="development", env='ENVIRONMENT')
    debug: bool = Field(default=True, env='DEBUG')

    class Config:
        env_file = ".env"
settings = Settings()