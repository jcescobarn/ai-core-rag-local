from fastapi import APIRouter, Body
from app.application.llm_service import LLMService
from app.infrastructure.llm_local import LLMLocal
from app.infrastructure.vector_store import ChromaVectorStore
from app.domain.models import LLMResponse
from app.core.config import settings

router = APIRouter()

llm_adapter = LLMLocal(settings.model_path)
vector_store_adapter = ChromaVectorStore()
llm_service = LLMService(llm_adapter, vector_store_adapter)

@router.post("/ask", response_model=LLMResponse)
async def ask_llm(query: str = Body(..., embed=True)):
    response = llm_service.ask_direct(query)
    return response 