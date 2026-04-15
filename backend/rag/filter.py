import asyncio
from backend.fga import check_access

async def filter_documents(user_id: str, documents: list):
    """
    Filters documents based on FGA permissions.
    Each document should have an 'id' field.
    """
    tasks = [check_access(user_id, "viewer", doc['id']) for doc in documents]
    results = await asyncio.gather(*tasks)
    
    authorized_docs = [doc for doc, allowed in zip(documents, results) if allowed]
    return authorized_docs
