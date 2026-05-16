# Lyra Ecosystem

A multi-agent AI research assistant. Four specialized agents - Researcher, Engineer, Planner, and Critic - work together to handle complex research and coding tasks from start to finish.

---

## What it does

You upload a document or ask a question. Lyra figures out what needs to happen, splits the work across agents, and streams the result back to you live. You can watch the agents' reasoning unfold in a visual graph called the BrainHub.

```
User Query
    |
    v
[ Planner ] --> breaks the task into steps
    |
    +--> [ Researcher ] --> finds relevant info from your documents
    +--> [ Engineer ]   --> writes and runs code in a sandbox
    |
    v
[ Critic ] --> checks everything before the final answer
```

---

## Agents

| Agent      | Model               | Job                                   |
|------------|---------------------|---------------------------------------|
| Researcher | LLaMA-3.1-70B       | Finds and summarizes info using RAG   |
| Engineer   | DeepSeek Coder V2.5 | Writes and executes code              |
| Planner    | Qwen-2.5-72B        | Breaks goals into a step-by-step plan |
| Critic     | Qwen-2.5-72B        | Reviews outputs for errors and quality|

---
## Tech stack

**Frontend**
- React 18 + TypeScript + Vite
- Tailwind CSS
- React Flow (for the BrainHub graph)
- Zustand (state management)
- Native WebSockets (real-time agent updates)

**Backend**
- FastAPI + Uvicorn
- JWT auth (python-jose + passlib)
- Celery + Redis (background jobs)
- LangChain / LangGraph (agent logic)
- Temporal (long-running workflow execution)

**Databases**
- PostgreSQL - main database
- pgvector - vector search for RAG
- Neo4j - task and agent relationship graphs
- Redis - caching and queues
- MinIO / S3 - file storage

**Model serving**
- vLLM - runs open-weight models
- Ollama - local dev setup
- Docker-in-Docker + gVisor - sandboxed code execution

---

## Folder structure

```
lyra-ecosystem/
├── backend/
│   └── src/
│       ├── api/              # routes: auth, chat, documents, agents
│       ├── services/         # DB, file storage, PDF extraction
│       └── orchestration/    # agents, prompts, workflow manager
├── frontend/
│   └── src/
│       ├── components/       # BrainHub, chat UI, file upload
│       ├── services/         # API calls, WebSocket connection
│       └── store/            # global state
├── ml_models/
├── infrastructure/           # Terraform, Kubernetes
├── monitoring/               # Prometheus, Grafana
├── ci_cd/
├── docker-compose.yml
├── Makefile
└── alembic/                  # DB migrations
```

---

## Running locally

**Prerequisites:** Docker, Node.js 18+, Python 3.11+, Ollama (optional)

```bash
# 1. Clone
git clone https://github.com/Logizel/lyra-ecosystem.git
cd lyra-ecosystem

# 2. Environment variables
cp backend/.env.example backend/.env
# fill in DB credentials, JWT secret, storage keys

# 3. Start databases
docker-compose up -d

# 4. Run migrations
cd backend && alembic upgrade head

# 5. Start backend
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000

# 6. Start frontend
cd frontend && npm install && npm run dev
# open http://localhost:5173

# 7. Pull a local model (optional)
ollama pull llama3.2:3b
```

---

## API

| Method | Endpoint              | Description                |
|--------|-----------------------|----------------------------|
| GET    | /health               | Health check               |
| POST   | /api/auth/register    | Create an account          |
| POST   | /api/auth/login       | Login, returns JWT         |
| POST   | /api/documents/upload | Upload a PDF               |
| POST   | /api/agent/research   | Ask the Researcher agent   |
| WS     | /ws                   | Real-time BrainHub updates |

---

## Roadmap

- [x] Phase 1 - Docker setup, FastAPI skeleton, React shell, DB schema
- [x] Phase 2 - Auth: register, login, JWT, protected routes
- [ ] Phase 3 - Document upload, MinIO storage, PDF text extraction
- [ ] Phase 4 - RAG: chunking, pgvector, Researcher agent
- [ ] Phase 5 - BrainHub UI, WebSocket integration, chat interface
- [ ] Phase 6 - Engineer, Planner, Critic agents
- [ ] Phase 7 - Multi-agent orchestration with LangGraph
- [ ] Phase 8 - Infrastructure: Kubernetes, Terraform, monitoring

---

## License

MIT
