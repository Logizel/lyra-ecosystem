# Lyra Ecosystem

A highly scalable, multi-agent artificial intelligence research and engineering assistant. Lyra orchestrates four specialized agents (Researcher, Engineer, Planner, and Critic) to execute complex, multi-step tasks.

Built for enterprise-scale from day one, Lyra features an asynchronous event-driven architecture. It completely decouples agent logic from network connections. This design allows independent scaling and fault tolerance while using a federated model strategy to maximize throughput on free-tier interfaces.

---

## Agent Federation Strategy

To avoid rate limits while maintaining high performance, Lyra assigns specific agents to dedicated application programming interfaces.

*   **Planner:** `gpt-oss-120b` via Cerebras. Breaks down tasks with high reasoning capability at fast speeds without exhausting primary rate limits.
*   **Researcher:** `DeepSeek V4 Flash` via OpenRouter. Uses its massive context window to process large documents and run complex data retrieval pipelines.
*   **Engineer:** `MiniMax M2.5` via OpenRouter. Excels at autonomous coding and tool usage within the execution sandbox.
*   **Critic:** `Llama 3.3 70B` via Groq. Delivers rapid reviews, ensuring the final quality check does not delay the final output.

---

## Architecture and Technology Stack

Lyra separates networking infrastructure from cognitive agent execution using an event-driven message bus.

### High-Concurrency API Gateway
*   **Technology:** Go with the Gin framework.
*   **Role:** Manages authentication, WebSockets, and file uploads. It pushes events to the message broker and handles thousands of persistent connections with minimal memory usage.

### Event-Driven Fabric
*   **Technology:** Apache Kafka.
*   **Role:** Decouples agents. The Planner publishes a task, which the Researcher consumes at its own pace. This ensures reliable message delivery and robust retry logic.

### Cognitive Microservices
*   **Technology:** Python, FastAPI, and LangGraph.
*   **Role:** Each agent runs as an isolated, containerized microservice. This allows independent scaling for resource-heavy agents like the Researcher.

### Code Execution Sandbox
*   **Technology:** Go, Docker, and gVisor.
*   **Role:** Provides a strict, kernel-isolated environment for the Engineer agent to safely compile and test generated code.

### Unified Data Tier
*   **Relational and Graph State:** PostgreSQL. Handles agent state checkpointing and user account data.
*   **Vector Search:** pgvector. A native PostgreSQL extension for storing and querying text embeddings.
*   **Artifact Storage:** AWS S3. Stores user documents and generated code artifacts.

---
### Core Event Flow

    Ingest: The user submits a prompt via the frontend interface.

    Route: The Go API Gateway validates the security token and publishes a task event to Apache Kafka.

    Plan: The Planner Agent consumes the event, creates a step-by-step plan, and publishes a research request.

    Execute: The Researcher and Engineer agents consume their respective tasks. Engineer code is routed to the Go Sandbox worker.

    Review: The Critic Agent consumes the execution outputs and verifies accuracy.

    Stream: The Go Gateway consumes the final completion event and streams the text to the user via WebSockets.

License

MIT
