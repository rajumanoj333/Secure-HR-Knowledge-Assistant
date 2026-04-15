# Mocking a retriever for the HR Knowledge Assistant
# In a real scenario, this would use FAISS or Pinecone

MOCK_DOCS = [
    {"id": "salary_2025", "content": "The salary structure for 2025 includes a 5% inflation adjustment."},
    {"id": "company_policy", "content": "Employees are entitled to 20 days of paid leave per year."}
]

async def retrieve_documents(query: str):
    # For now, returning all mock docs as relevant
    return MOCK_DOCS
