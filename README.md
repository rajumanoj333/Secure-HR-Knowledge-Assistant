# 🧠 Secure HR Knowledge Assistant (Auth0 FGA + RAG)

An internal chatbot that provides answers from sensitive HR documents using Retrieval-Augmented Generation (RAG), with strict access control enforced by **Auth0 Fine-Grained Authorization (FGA)**.

## 🏗️ Architecture

```
User → React Frontend → FastAPI Backend → Auth0 FGA Check → RAG Retrieval → OpenAI LLM → Response
```

## 🔐 Core Privacy Logic

1.  **Retrieve:** System finds relevant documents for the query.
2.  **Authorize:** For each document, the backend calls Auth0 FGA to check if the current user has `viewer` relation.
3.  **Generate:** Only authorized documents are sent to the LLM (GPT-4o-mini) to generate the final answer.

## 🚀 Tech Stack

*   **Frontend:** React (TypeScript) + Tailwind CSS + Vite
*   **Backend:** FastAPI (Python)
*   **Authorization:** Auth0 FGA (OpenFGA)
*   **LLM:** OpenAI API
*   **Icons:** Lucide-react

## 📂 Project Structure

```
.
├── backend/
│   ├── main.py          # FastAPI entry point
│   ├── config.py        # Environment settings
│   ├── fga.py           # Auth0 FGA client integration
│   └── rag/
│       ├── filter.py    # FGA filtering logic (CRITICAL)
│       ├── llm.py       # OpenAI generation
│       └── retriever.py # Document retrieval (Mocked)
├── frontend/
│   └── src/
│       └── App.tsx      # Chat interface
├── .env.example         # Template for environment variables
└── README.md
```

## 🛠️ Setup

### Backend
1. `cd backend`
2. `python -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. Create `.env` from `.env.example`
6. `python main.py`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`

## 🧪 Demo Scenario

*   **Alice (HR Manager):** Can view `salary_2025.pdf` and `company_policy.pdf`.
*   **Bob (Employee):** Can only view `company_policy.pdf`.

When Bob asks about salaries, the system filters out the unauthorized document before it ever reaches the LLM.
