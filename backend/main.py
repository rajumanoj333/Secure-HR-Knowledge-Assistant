from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.rag.retriever import retrieve_documents
from backend.rag.filter import filter_documents
from backend.rag.llm import generate_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str
    user_id: str  # In production, this would come from the JWT token

@app.post("/chat")
async def chat(request: ChatRequest):
    # 1. Retrieve relevant docs
    docs = await retrieve_documents(request.query)
    
    # 2. Filter docs using FGA
    authorized_docs = await filter_documents(request.user_id, docs)
    
    # 3. Generate response using LLM
    response = await generate_response(request.query, authorized_docs)
    
    return {"response": response, "authorized_docs_count": len(authorized_docs)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
