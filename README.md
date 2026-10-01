# CareerPilot AI

**Multi-Agent AI Career & Research Assistant for Students**

CareerPilot AI is a student-focused AI career assistant that uses multiple specialized AI agents to help students with resume analysis, career planning, learning plans, project recommendations, interview preparation, and research-based career guidance.

The system combines **Google Gemini, LangGraph, RAG, ChromaDB, FastAPI, SQLite-based memory, and Streamlit** into a modular multi-agent architecture.

---

## 🚀 Live Application

**Frontend:** Streamlit Community Cloud

**Backend API:** Render

The frontend communicates with the deployed FastAPI backend through a configurable API URL.

---

## 🎯 Project Goal

CareerPilot AI is designed to provide students with a single AI-powered system for different stages of career preparation.

Instead of using one large prompt for every task, the system separates responsibilities across specialized agents.

The system currently supports:

- Resume Analysis
- Career Roadmap Generation
- Personalized Learning Plans
- Project Recommendations
- Interview Preparation
- Research-Based Career Questions

---

# 🧠 System Architecture

```text
                    ┌─────────────────────┐
                    │      Streamlit      │
                    │      Frontend       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │        API          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     LangGraph       │
                    │  Workflow Engine    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Supervisor Agent   │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │          │         │         │          │
          ▼          ▼         ▼         ▼          ▼
      Resume      Career    Learning   Project   Interview
       Agent      Agent      Agent      Agent      Agent
          │          │         │         │          │
          └──────────┴─────────┴─────────┴──────────┘
                               │
                               ▼
                       Research Agent
                               │
                               ▼
                          Research Tool
                               │
                               ▼
                         RAG Pipeline
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
                ChromaDB          Gemini Embeddings




🤖 Multi-Agent Architecture

CareerPilot AI uses 7 agents.

1. Resume Agent

Analyzes uploaded resumes and extracts relevant information that can be used for career-related recommendations.

2. Career Agent

Generates personalized career roadmaps based on the student's profile, skills, interests, and target career.

3. Learning Agent

Creates structured learning plans based on the student's target role and current skill set.

4. Project Agent

Recommends projects appropriate for the student's experience level and target career.

5. Interview Agent

Generates interview preparation material based on the selected role and skills.

6. Research Agent

Handles research-oriented questions using the project's RAG pipeline and research knowledge base.

7. Supervisor Agent

Acts as the routing layer for the multi-agent system.

It determines which specialized agent should handle a request.

🔄 Agent Execution Flow

The application follows this general flow:

User Request
     │
     ▼
FastAPI
     │
     ▼
LangGraph
     │
     ▼
Supervisor Agent
     │
     ▼
Specialized Agent
     │
     ▼
Tool
     │
     ▼
Prompt
     │
     ▼
Gemini Service
     │
     ▼
Gemini API

This separation keeps agent coordination, business logic, prompting, and LLM communication modular.

🔎 Research & RAG Pipeline

The Research Agent uses a Retrieval-Augmented Generation pipeline.

Research Question
       │
       ▼
Research Agent
       │
       ▼
Research Tool
       │
       ▼
RAG Pipeline
       │
       ▼
Retriever
       │
       ▼
ChromaDB
       │
       ├──► Gemini Embeddings
       │
       ▼
Relevant Documents
       │
       ▼
Gemini
       │
       ▼
Research Answer + Sources

The research knowledge base contains career-related documents covering areas such as:

AI Engineering
Machine Learning Engineering
Data Science
Generative AI Engineering
Prompt Engineering

The system uses Gemini Embeddings for vector representations and ChromaDB for vector search.

🧩 Core Technology Stack
Backend
Python 3.11
FastAPI
Uvicorn
LangGraph
LangChain
Google Gemini API
ChromaDB
SQLite
Pydantic
AI / RAG
Gemini
Gemini Embeddings
Retrieval-Augmented Generation
ChromaDB
LangChain document loaders
Recursive text splitting
Frontend
Streamlit
Requests
Deployment
Render — Backend
Streamlit Community Cloud — Frontend
GitHub — Source Control
📁 Project Structure
careerpilot-ai/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── config/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── prompts/
│   │   ├── rag/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── tools/
│   │   └── utils/
│   │
│   ├── uploads/
│   ├── .env
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── assets/
├── datasets/
├── docs/
├── scripts/
├── tests/
│
├── .gitignore
└── README.md
🔌 API Endpoints

The FastAPI backend exposes endpoints for the main CareerPilot capabilities.

Endpoint	Purpose
POST /resume/upload	Resume analysis
POST /career/roadmap	Career roadmap generation
POST /learning/plan	Learning plan generation
POST /project/recommend	Project recommendations
POST /interview/prepare	Interview preparation
POST /research/ask	Research-based questions
GET /	Backend health/welcome endpoint

Interactive API documentation is available through FastAPI's /docs endpoint when the backend is running.

🧠 Memory System

CareerPilot AI includes a session-based memory layer.

The memory system is responsible for maintaining relevant context across requests so that the system can use previously available session information when generating responses.

The memory implementation uses SQLite during the current deployment architecture.

🔐 Environment Variables

The Gemini API key is stored as an environment variable.

Create a .env file inside the backend directory:

GEMINI_API_KEY=your_gemini_api_key

The .env file is intentionally excluded from Git.

Never commit API keys or other secrets to the repository.

For deployment, the Gemini API key is configured through the hosting platform's secret/environment-variable settings.

💻 Local Setup
1. Clone the repository
git clone https://github.com/anandkrishna24/careerpilot-ai.git
cd careerpilot-ai
2. Create a virtual environment

From the backend directory:

cd backend
python -m venv .venv
3. Activate the environment
Windows PowerShell
.venv\Scripts\Activate.ps1
4. Install backend dependencies
pip install -r requirements.txt
5. Configure Gemini

Create:

backend/.env

and add:

GEMINI_API_KEY=your_gemini_api_key
6. Start the backend
uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

FastAPI documentation:

http://127.0.0.1:8000/docs
🖥️ Frontend Setup

Open a second terminal and move into the frontend directory:

cd frontend

Install dependencies:

pip install -r requirements.txt

Set the backend URL if required:

$env:CAREERPILOT_API_URL="http://127.0.0.1:8000"

Start Streamlit:

streamlit run app.py
⚙️ Configuration

The Streamlit frontend uses:

API_BASE_URL = os.getenv(
    "CAREERPILOT_API_URL",
    "http://127.0.0.1:8000"
)

This allows the same frontend application to communicate with either:

A local FastAPI backend
The deployed Render backend

without changing the application code.

☁️ Deployment Architecture

The deployed system uses separate hosting for frontend and backend.

                 Internet
                    │
                    ▼
        ┌──────────────────────┐
        │ Streamlit Community  │
        │        Cloud         │
        └──────────┬───────────┘
                   │
                   │ HTTPS
                   ▼
        ┌──────────────────────┐
        │       Render         │
        │     FastAPI API      │
        └──────────┬───────────┘
                   │
                   ▼
              Gemini API
Backend

Hosted on Render as a Python web service.

Frontend

Hosted on Streamlit Community Cloud.

AI Provider

Google Gemini API.

⚠️ Deployment Considerations

The current deployment is designed as a portfolio/demo deployment using free hosting resources.

The free Render environment has limited memory and ephemeral filesystem behavior.

Because of this:

Runtime-generated files should not be treated as permanent storage.
SQLite data is not intended as durable production storage.
The research vector store used by the deployed application is included with the project so the static research corpus is available after deployment.
The current architecture is appropriate for demonstrating the system and its AI workflows.

A production-scale deployment could later introduce dedicated persistent storage and infrastructure, but those components are outside the current project scope.

🧪 Validation

The deployed application has been tested across the major user-facing workflows:

 Backend health endpoint
 Resume Analysis
 Career Roadmap
 Learning Plan
 Project Recommendation
 Interview Preparation
 Research / RAG
 Frontend → Backend communication
 Gemini API integration
 Gemini Embeddings
 Production dependency installation
 Environment variable configuration
 GitHub deployment
🔒 Security

Sensitive configuration is intentionally excluded from source control.

The repository ignores:

.env
.venv/
__pycache__/
*.pyc
uploads/
*.db

API credentials are supplied through environment variables rather than hard-coded into application code.

🎓 Intended Users

CareerPilot AI is designed specifically for students and early-career users who want AI-assisted support for:

Career exploration
Skill development
Resume preparation
Project selection
Interview preparation
Career-related research

The current project is student-focused rather than recruiter-focused.

🚀 Future Scope

Potential future improvements include:

More career-domain knowledge sources
Larger research knowledge bases
More sophisticated persistent storage
Authentication and user accounts
Production-grade database infrastructure
More advanced evaluation and observability
Additional career-specific tools

These are future possibilities and are not required for the current system.

👨‍💻 Project

CareerPilot AI

A multi-agent AI career and research assistant built to demonstrate practical implementation of:

Multi-agent systems
LangGraph orchestration
Retrieval-Augmented Generation
Vector databases
LLM integration
Prompt engineering
API development
AI application deployment
Session memory
Cloud deployment
License

This project is intended as a portfolio and educational project.


**Important:** don't paste or commit any Gemini API key into this README. The placeholder is intentional.

Once you've replaced the README, **don't commit yet**. We'll first inspect the rendered/a