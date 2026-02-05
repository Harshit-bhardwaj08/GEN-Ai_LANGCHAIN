project:
  name: LangChain & GenAI Playground
  description: >
    A structured workspace for learning, experimenting, and building
    Generative AI applications using LangChain and LLMs.
    Covers basics to advanced concepts like RAG systems and AI agents.

structure:
  1ChatModel:
    purpose: Basic LLM and chat model experiments
  2_prompt_templates:
    purpose: Prompt engineering and reusable prompt templates
  3_chains:
    purpose: LangChain chains (LLMChain, SequentialChain, etc.)
  4_RAGs:
    purpose: Retrieval-Augmented Generation (RAG) implementations
  5_agents:
    purpose: AI agents, tools, and multi-agent workflows
  envLang:
    purpose: Python virtual environment
  .env:
    purpose: Environment variables (API keys, configs)
    note: Ignored by Git for security
  .gitignore:
    purpose: Files and folders ignored by Git

learning_objectives:
  - Working with chat models and LLMs
  - Prompt engineering best practices
  - Building chains using LangChain
  - Implementing RAG pipelines
  - Creating autonomous and tool-using agents
  - Secure environment and API key management

setup:
  steps:
    - step: Clone repository
      command: git clone <your-repo-url>
    - step: Navigate to project
      command: cd <repo-name>
    - step: Activate virtual environment (Windows)
      command: envLang\\Scripts\\activate
    - step: Activate virtual environment (macOS/Linux)
      command: source envLang/bin/activate
    - step: Install dependencies
      command: pip install -r requirements.txt
    - step: Configure environment variables
      file: .env
      example:
        OPENAI_API_KEY: your_api_key_here

tech_stack:
  language: Python
  frameworks:
    - LangChain
    - FastAPI
  ai_models:
    - OpenAI LLMs
    - Other supported LLM providers
  vector_databases:
    - FAISS
    - Chroma

usage_notes:
  - Each folder focuses on a single core GenAI concept
  - Designed for learning, experimentation, and interview preparation
  - Can be extended into production-ready GenAI systems

license:
  type: Educational / Learning Use
  note: Free to fork, modify, and extend
