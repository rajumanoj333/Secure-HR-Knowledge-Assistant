from openai import OpenAI
from backend.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def generate_response(query: str, authorized_docs: list):
    if not authorized_docs:
        return "I'm sorry, I don't have access to any documents that can answer your question, or no relevant documents were found."

    context = "\n\n".join([doc['content'] for doc in authorized_docs])
    
    prompt = f"""
    You are an HR Assistant. Use the following documents to answer the user query. 
    If you don't know the answer, say you don't know.
    
    Documents:
    {context}
    
    User Query: {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
