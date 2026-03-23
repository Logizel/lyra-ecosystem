# 🧠 Lyra Ecosystem

> A multi-agent AI research assistant where specialized agents collaborate to automate complex research and engineering workflows.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![TypeScript](https://img.shields.io/badge/typescript-5.0+-blue)

---

## What is Lyra?

Lyra mimics a human research team. Four specialized agents — **Researcher**, **Engineer**, **Planner**, and **Critic** — work together inside a shared reasoning space called the **BrainHub**. Users can upload documents, ask complex questions, and watch agents think, debate, and refine answers in real time.

```
User Query
    │
    ▼
┌─────────────────────────────────────┐
│              BrainHub               │
│                                     │
│  Planner ──► Researcher ──► Critic  │
│      └──────► Engineer  ──────┘     │
└─────────────────────────────────────┘
    │
    ▼
Streamed Answer + Visual Graph
```

---

## Agents

| Agent | Model | Role |
|---|---|---|
| **Researcher** | LLaMA-3.1-70B | Retrieves & summarizes info via RAG |
| **Engineer** | DeepSeek Coder V2.5 | Writes & executes code in a sandbox |
| **Planner** | Qwen-2.5-72B | Decomposes goals into task graphs |
| **Critic** | Qwen-2.5-72B | Validates logic, facts, and code quality |

---

## Tech Stack

**Frontend**
- React 18 + TypeScript + Vite
- Tailwind CSS for styling
- React Flow for BrainHub visualization
- Zustand for state management
- Native WebSockets for real-time updates

**Backend**
- FastAPI + Uvicorn (async, high-performance)
- JWT authentication (python-jose + passlib)
- Celery + Redis for background task queues
- LangChain / LangGraph for agent orchestration
- Temporal for durable workflow execution

**Data**
- PostgreSQL 15+ (primary DB)
- pgvector extension (semantic search / RAG)
- Neo4j (task dependency graphs)
- Redis (caching, queues, pub/sub)
- MinIO / AWS S3 (document storage)

**Model Serving**
- vLLM for open-weight model inference
- Ollama for local development
- Docker-in-Docker + gVisor for sandboxed code execution

---

## Project Structure

```
lyra-ecosystem/
├── backend/
│   └── src/
│       ├── api/              # FastAPI routes (auth, chat, documents, agents)
│       ├── services/         # DB clients, file storage, PDF extractor
│       └── orchestration/    # LangChain agents, prompts, agent manager
├── frontend/
│   └── src/
│       ├── components/       # BrainHub, ChatInterface, file upload
│       ├── services/         # API client, WebSocket service
│       └── store/            # Zustand state
├── ml_models/                # Model configs and serving setup
├── infrastructure/           # Terraform, Kubernetes manifests
├── monitoring/               # Prometheus, Grafana configs
├── ci_cd/                    # GitHub Actions workflows
├── docker-compose.yml
├── docker-compose.override.yml
├── Makefile
└── alembic/                  # DB migrations
```

---

## Getting Started

### Prerequisites

- Docker + Docker Compose
- Node.js 18+
- Python 3.11+
- Ollama (for local model serving)

### 1. Clone the repo

```bash
git clone https://github.com/Logizel/lyra-ecosystem.git
cd lyra-ecosystem
```

### 2. Set up environment variables

```bash
cp backend/.env.example backend/.env
# Edit .env — fill in DB credentials, JWT secret, S3 keys
```

### 3. Start all services

```bash
docker-compose up -d
# Starts: PostgreSQL, Redis, Neo4j, MinIO
```

### 4. Run DB migrations

```bash
cd backend
alembic upgrade head
```

### 5. Start the backend

```bash
cd backend
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
```

### 6. Start the frontend

```bash
cd frontend
npm install
npm run dev
# Visit http://localhost:5173
```

### 7. Pull a local model (optional, for dev)

```bash
ollama pull llama3.2:3b
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check |
| `POST` | `/api/auth/register` | Create account |
| `POST` | `/api/auth/login` | Login, returns JWT |
| `POST` | `/api/documents/upload` | Upload PDF |
| `POST` | `/api/agent/research` | Ask the Researcher agent |
| `WS` | `/ws` | Real-time BrainHub updates |

---

## Development Roadmap

- [x] Phase 1 — Foundation (Docker, FastAPI, React shell, DB schema)
- [x] Phase 2 — Auth pipeline (JWT, register/login, protected routes)
- [ ] Phase 3 — Document ingestion (upload, MinIO, PDF extraction)
- [ ] Phase 4 — RAG pipeline (chunking, pgvector, Researcher agent)
- [ ] Phase 5 — BrainHub UI (React Flow, WebSocket integration)
- [ ] Phase 6 — Remaining agents (Engineer, Planner, Critic)
- [ ] Phase 7 — Multi-agent orchestration (LangGraph workflows)
- [ ] Phase 8 — Infrastructure (Kubernetes, Terraform, monitoring)

---

## Contributing

This is a learning project built in public. PRs and issues are welcome — especially if you find something broken or a simpler way to do something.

---

## License

MIT — see [LICENSE](./LICENSE)
