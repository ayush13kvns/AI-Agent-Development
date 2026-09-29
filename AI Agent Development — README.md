# AI Agent Development

A Python-based AI application demonstrating how to build AI applications using **Ollama, Qwen, embeddings, and Retrieval-Augmented Generation (RAG)**.

The project is designed to run AI models locally using Ollama rather than requiring a cloud-hosted LLM.

---

## 1. Project Overview

This project demonstrates the basic building blocks required to create an AI application:

- Python
- Virtual environments
- Ollama
- Qwen 3 (`qwen3:4b`)
- Nomic embedding model (`nomic-embed-text`)
- OpenAI Python SDK
- Environment variables
- Retrieval-Augmented Generation (RAG)

The RAG implementation allows the application to:

1. Read documents.
2. Convert documents into embeddings.
3. Store/use those embeddings for similarity search.
4. Retrieve relevant information.
5. Send the retrieved information to an LLM.
6. Generate an answer based on the retrieved context.

---

# 2. Architecture

The overall flow is:

```text
                    User Question
                         |
                         v
                +------------------+
                |   RAG Application |
                +------------------+
                         |
                         v
                Create Query Embedding
                         |
                         v
                nomic-embed-text
                         |
                         v
                  Similarity Search
                         |
                         v
              Relevant Document(s)
                         |
                         v
                    Qwen 3 4B
                         |
                         v
                       Answer
```

The project uses two different models for two different purposes.

### Qwen 3 4B

Used as the **LLM** to generate the final response.

```text
qwen3:4b
```

### Nomic Embed Text

Used to convert text into numerical vectors.

```text
nomic-embed-text
```

These embeddings allow the application to identify documents that are semantically related to a user's question.

---

# 3. Prerequisites

Install the following before running the project:

- Git
- Python 3.x
- Ollama
- VS Code or another Python IDE
- Internet connection for the initial package/model downloads

Verify Python:

```powershell
python --version
```

Verify Git:

```powershell
git --version
```

Verify Ollama:

```powershell
ollama --version
```

---

# 4. Clone the Repository

Clone the repository:

```powershell
git clone https://github.com/ayush13kvns/AI-Agent-Development.git
```

Move into the project:

```powershell
cd AI-Agent-Development
```

Verify the repository:

```powershell
git status
```

---

# 5. Create a Python Virtual Environment

Create the virtual environment:

```powershell
python -m venv .venv
```

If the virtual environment is created successfully, activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(.venv)
```

For example:

```text
(.venv) PS E:\AI-Agent-Development>
```

---

# 6. Deactivate the Virtual Environment

When you want to leave the virtual environment:

```powershell
deactivate
```

You can activate it again later with:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

# 7. Verify Python and pip

After activating the virtual environment, verify that Python points to the project's `.venv`:

```powershell
python -c "import sys; print(sys.executable)"
```

Expected output:

```text
E:\AI-Agent-Development\.venv\Scripts\python.exe
```

Check pip:

```powershell
python -m pip --version
```

### Recommended practice

Use:

```powershell
python -m pip install <package>
```

instead of:

```powershell
pip install <package>
```

This ensures that packages are installed into the Python environment currently being used.

---

# 8. Install Python Dependencies

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install the OpenAI Python SDK:

```powershell
python -m pip install openai
```

Install dotenv support if the project uses a `.env` file:

```powershell
python -m pip install python-dotenv
```

Install NumPy if required:

```powershell
python -m pip install numpy
```

If the repository contains a `requirements.txt` file, the preferred approach is:

```powershell
python -m pip install -r requirements.txt
```

---

# 9. Install Ollama

Download and install Ollama from:

https://ollama.com/

After installation, verify it:

```powershell
ollama --version
```

Check the currently installed models:

```powershell
ollama list
```

---

# 10. Download Qwen 3

The project uses Qwen 3 as the local LLM.

Pull the model:

```powershell
ollama pull qwen3:4b
```

Verify:

```powershell
ollama list
```

You should see:

```text
qwen3:4b
```

You can also test the model directly:

```powershell
ollama run qwen3:4b
```

Try asking it a question.

To exit the Ollama interactive session:

```text
/bye
```

---

# 11. Download the Embedding Model

The RAG implementation uses:

```text
nomic-embed-text
```

Download it:

```powershell
ollama pull nomic-embed-text
```

Verify:

```powershell
ollama list
```

You should see both:

```text
qwen3:4b
nomic-embed-text
```

---

# 12. Ollama Models Used by the Project

| Model | Purpose |
|---|---|
| `qwen3:4b` | Generate AI responses |
| `nomic-embed-text` | Generate document/query embeddings |

These models perform different jobs and both are required for the RAG workflow.

---

# 13. OpenAI-Compatible Ollama API

Ollama provides an API compatible with the OpenAI Python client.

The typical local endpoint is:

```text
http://localhost:11434/v1
```

Therefore Python code can use:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
```

The API key is not used as a real cloud authentication key when communicating with local Ollama. A placeholder such as:

```text
ollama
```

is commonly used.

---

# 14. Environment Variables

If the project uses a `.env` file, create:

```text
.env
```

Example:

```env
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=qwen3:4b
```

If embeddings are configured separately, use:

```env
EMBEDDING_MODEL=nomic-embed-text
```

Do **not** commit real API keys or secrets to GitHub.

Add `.env` to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# 15. Running the Basic AI Application

After activating the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the Python application:

```powershell
python hello_ai.py
```

The application should connect to the local Ollama server and send the request to the configured model.

---

# 16. Running the RAG Application

Navigate to the RAG implementation:

```powershell
cd RAG_Implimentation
```

Make sure the virtual environment from the project root is activated.

If it is not activated:

```powershell
..\ .venv\Scripts\Activate.ps1
```

> Remove the space between `..` and `.venv` when typing the command:

```powershell
..\.venv\Scripts\Activate.ps1
```

Run the RAG application:

```powershell
python .\rag.py
```

---

# 17. How the RAG Implementation Works

The RAG implementation follows this general process:

### Step 1 — Load documents

The application reads the available documents.

```text
Documents
   |
   +-- Document 1
   +-- Document 2
   +-- Document 3
```

### Step 2 — Generate embeddings

Each document is passed to:

```text
nomic-embed-text
```

The text is converted into a vector:

```text
Document
   |
   v
Embedding Model
   |
   v
[0.12, -0.31, 0.77, ...]
```

### Step 3 — Store embeddings

The application keeps the document embeddings so that they can be compared with the embedding of a user's question.

### Step 4 — Embed the user query

The user's question is also converted into an embedding using:

```text
nomic-embed-text
```

### Step 5 — Find relevant documents

The query embedding is compared with document embeddings.

The most relevant documents are selected.

### Step 6 — Send context to Qwen

The selected documents are combined with the user's question.

Conceptually:

```text
User Question
      +
Relevant Documents
      |
      v
    Qwen 3
      |
      v
Generated Answer
```

This is the key idea behind Retrieval-Augmented Generation.

---

# 18. RAG vs Normal LLM

### Normal LLM

```text
Question
   |
   v
Qwen
   |
   v
Answer
```

The model answers using the information available within its model/context.

### RAG

```text
Question
   |
   v
Embedding
   |
   v
Search Documents
   |
   v
Relevant Context
   |
   v
Qwen
   |
   v
Answer
```

RAG allows the application to provide external/private information to the LLM at runtime.

---

# 19. Project Structure

The project is organized around the AI application and RAG implementation.

A typical structure is:

```text
AI-Agent-Development/
│
├── .venv/
│
├── hello_ai.py
│
├── RAG_Implimentation/
│   │
│   ├── rag.py
│   ├── test_embedding.py
│   └── ...
│
├── .env
├── .gitignore
└── README.md
```

The exact structure may change as additional AI-agent functionality is added.

---

# 20. Git Feature Branch Workflow

The project uses Git for version control.

Check the current branch:

```powershell
git branch
```

Check all local and remote branches:

```powershell
git branch -a
```

Fetch newly created branches from GitHub:

```powershell
git fetch origin
```

If a feature branch already exists on GitHub:

```powershell
git switch -c feature --track origin/feature
```

Replace `feature` with the actual branch name.

Verify:

```powershell
git branch
```

The current branch is marked with:

```text
*
```

Example:

```text
  main
* feature
```

---

# 21. Create a New Feature Branch

Starting from `main`:

```powershell
git switch main
git pull
```

Create a feature branch:

```powershell
git switch -c feature/my-feature
```

Push it to GitHub:

```powershell
git push -u origin feature/my-feature
```

---

# 22. Commit Changes

Check changed files:

```powershell
git status
```

Add files:

```powershell
git add .
```

Commit:

```powershell
git commit -m "Add RAG implementation"
```

Push:

```powershell
git push
```

---

# 23. Common Problems and Solutions

## Problem 1 — `ModuleNotFoundError: No module named 'openai'`

Example:

```text
ModuleNotFoundError: No module named 'openai'
```

Solution:

```powershell
python -m pip install openai
```

Verify:

```powershell
python -m pip show openai
```

---

## Problem 2 — Ollama model not found

Example:

```text
model "qwen3:4b" not found
```

Solution:

```powershell
ollama pull qwen3:4b
```

Then:

```powershell
ollama list
```

---

## Problem 3 — Embedding model not found

Example:

```text
model "nomic-embed-text" not found, try pulling it first
```

Solution:

```powershell
ollama pull nomic-embed-text
```

Verify:

```powershell
ollama list
```

---

## Problem 4 — Wrong model name

Make sure the model name is spelled correctly.

Correct:

```text
qwen3:4b
```

Not:

```text
quen3:4b
```

Always check:

```powershell
ollama list
```

and use the exact model name shown there.

---

# 24. Pip Launcher Error After Renaming the Project Folder

If you receive an error similar to:

```text
Fatal error in launcher: Unable to create process using ...
```

and the error contains two different project paths, for example:

```text
E:\AI-Agent-Developmment
```

and:

```text
E:\AI-Agent-Development
```

the virtual environment was probably created under the old directory.

The clean solution is to recreate the virtual environment.

Deactivate:

```powershell
deactivate
```

Delete the old environment:

```powershell
Remove-Item -Recurse -Force .venv
```

Create it again:

```powershell
python -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then reinstall dependencies:

```powershell
python -m pip install -r requirements.txt
```

or install the required packages individually.

---

# 25. Verify the Complete Installation

Run:

```powershell
python --version
```

```powershell
ollama --version
```

```powershell
ollama list
```

```powershell
python -m pip show openai
```

The Ollama model list should contain:

```text
qwen3:4b
nomic-embed-text
```

Then test the basic application:

```powershell
python hello_ai.py
```

Finally run:

```powershell
cd RAG_Implimentation
python rag.py
```

---

# 26. Complete Setup — Quick Start

For a new machine, the basic workflow is:

```powershell
git clone https://github.com/ayush13kvns/AI-Agent-Development.git

cd AI-Agent-Development

python -m venv .venv

.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

python -m pip install openai python-dotenv numpy

ollama pull qwen3:4b

ollama pull nomic-embed-text

ollama list

python hello_ai.py

cd RAG_Implimentation

python rag.py
```

---

# 27. Important Notes

### Keep the virtual environment active

Before installing Python packages or running the application:

```text
(.venv)
```

should normally appear in your terminal.

### Use `python -m pip`

Prefer:

```powershell
python -m pip install package_name
```

instead of:

```powershell
pip install package_name
```

### Keep `.env` private

Never commit passwords, private API keys, tokens, or other secrets to GitHub.

### Ollama must be available

The application requires Ollama to be installed and its local API to be available.

---

# 28. Future Enhancements

Possible improvements to this project include:

- Vector database integration
- Document chunking
- Metadata filtering
- Semantic search
- Conversation memory
- Multiple document formats
- PDF ingestion
- Web-based UI
- AI agent tools
- Function/tool calling
- Streaming responses
- Source/citation display
- RAG evaluation
- Automated testing
- Docker deployment
- Production API using FastAPI

---

# 29. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Ollama | Local model runtime |
| Qwen 3 4B | Large language model |
| Nomic Embed Text | Text embeddings |
| OpenAI Python SDK | API client |
| Git | Version control |
| GitHub | Source-code repository |

---

# 30. Author

**Ayush Kumar**

GitHub:

https://github.com/ayush13kvns

Repository:

https://github.com/ayush13kvns/AI-Agent-Development