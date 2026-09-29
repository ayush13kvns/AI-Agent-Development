# AI Agent Development

A Python-based AI-agent learning project demonstrating local AI
applications with **Ollama, Qwen 3, embeddings, RAG, tools, tool
management, file operations, and an AI planner**.

------------------------------------------------------------------------

## Project Structure

``` text
AI-Agent-Development/
│
├── Basic_agent/
│   ├── hello_ai.py
│   └── assistant.py
│
├── File_Operations/
│   ├── assistant.py
│   ├── tools.py
│   ├── tool_manager.py
│   ├── test_file_tool.py
│   └── data/
│
├── Planner_tool/
│   ├── planner.py
│   ├── assistant.py
│   ├── tools.py
│   └── test_planner.py
│
├── RAG_Implimentation/
│   ├── rag.py
│   ├── retriever.py
│   ├── similarity.py
│   ├── test_embedding.py
│   ├── test_retriever.py
│   └── knowledge/
│
├── Tool_assistant/
│   ├── assistant.py
│   ├── tools.py
│   └── test_tools.py
│
├── Tool_manager/
│   ├── assistant.py
│   ├── tool_manager.py
│   ├── tools.py
│   ├── test_tool_manager.py
│   └── test_tools.py
│
└── README.md
```

------------------------------------------------------------------------

# 1. Project Overview

This repository is organized as a progression of AI-agent concepts:

-   Basic LLM interaction
-   AI assistant
-   Tool/function calling concepts
-   Tool management
-   File operations
-   Retrieval-Augmented Generation (RAG)
-   Planner-based tool selection

The main local models used by the project are:

  -----------------------------------------------------------------------
  Model                               Purpose
  ----------------------------------- -----------------------------------
  `qwen3:4b`                          Local LLM used to understand
                                      requests and generate responses

  `nomic-embed-text`                  Converts text into embeddings for
                                      RAG
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 2. Architecture

``` text
                         User
                          |
                          v
                 +----------------+
                 |  AI Assistant  |
                 +----------------+
                          |
             +------------+------------+
             |            |            |
             v            v            v
          Planner       Tools          RAG
             |            |             |
             v            v             v
       Tool Selection  Tool Execution  Retrieval
             |            |             |
             +------------+-------------+
                          |
                          v
                       Qwen 3
                          |
                          v
                       Answer
```

------------------------------------------------------------------------

# 3. Prerequisites

Install:

-   Git
-   Python 3.x
-   Ollama
-   VS Code or another Python IDE
-   Internet connection for initial package/model downloads

Verify:

``` powershell
python --version
git --version
ollama --version
```

------------------------------------------------------------------------

# 4. Clone the Repository

``` powershell
git clone https://github.com/ayush13kvns/AI-Agent-Development.git
cd AI-Agent-Development
git status
```

------------------------------------------------------------------------

# 5. Create a Virtual Environment

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Deactivate:

``` powershell
deactivate
```

Verify the active Python:

``` powershell
python -c "import sys; print(sys.executable)"
python -m pip --version
```

Recommended practice:

``` powershell
python -m pip install <package>
```

instead of:

``` powershell
pip install <package>
```

------------------------------------------------------------------------

# 6. Install Python Dependencies

``` powershell
python -m pip install --upgrade pip
python -m pip install openai python-dotenv numpy
```

If a `requirements.txt` file is added later:

``` powershell
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

# 7. Configure Ollama

Install Ollama from:

https://ollama.com/

Check:

``` powershell
ollama --version
ollama list
```

------------------------------------------------------------------------

# 8. Download Qwen 3

The project uses Qwen 3 4B as its local LLM.

``` powershell
ollama pull qwen3:4b
```

Test:

``` powershell
ollama run qwen3:4b
```

Exit:

``` text
/bye
```

------------------------------------------------------------------------

# 9. Download the Embedding Model

The RAG implementation uses:

``` text
nomic-embed-text
```

Download:

``` powershell
ollama pull nomic-embed-text
```

Verify:

``` powershell
ollama list
```

------------------------------------------------------------------------

# 10. Ollama OpenAI-Compatible API

Ollama provides a local OpenAI-compatible API:

``` text
http://localhost:11434/v1
```

Example:

``` python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
```

The `ollama` API key is a local placeholder rather than a cloud API
credential.

------------------------------------------------------------------------

# 11. Environment Variables

Example:

``` env
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=qwen3:4b
```

For RAG, the embedding model is:

``` text
nomic-embed-text
```

Keep environment files containing secrets out of source control.

Recommended `.gitignore` entries:

``` gitignore
.env
.venv/
__pycache__/
*.pyc
```

------------------------------------------------------------------------

# 12. Basic Agent

The `Basic_agent` folder contains the initial LLM interaction examples.

Run:

``` powershell
cd Basic_agent
python hello_ai.py
```

Assistant:

``` powershell
python assistant.py
```

------------------------------------------------------------------------

# 13. Tool Assistant

The `Tool_assistant` folder demonstrates an assistant that can use
predefined Python tools.

``` text
Tool_assistant/
├── assistant.py
├── tools.py
└── test_tools.py
```

Concept:

``` text
User Request
     |
     v
AI Assistant
     |
     v
Select/Use Tool
     |
     v
Python Tool
     |
     v
Tool Result
     |
     v
AI Response
```

Run:

``` powershell
cd Tool_assistant
python assistant.py
```

------------------------------------------------------------------------

# 14. Tool Manager

The `Tool_manager` folder separates tool management from the assistant.

``` text
Tool_manager/
├── assistant.py
├── tool_manager.py
├── tools.py
├── test_tool_manager.py
└── test_tools.py
```

Run:

``` powershell
cd Tool_manager
python assistant.py
```

------------------------------------------------------------------------

# 15. File Operations

The `File_Operations` folder demonstrates how an AI assistant can work
with files through Python tools.

``` text
File_Operations/
├── assistant.py
├── tools.py
├── tool_manager.py
├── test_file_tool.py
└── data/
```

Run:

``` powershell
cd File_Operations
python assistant.py
```

------------------------------------------------------------------------

# 16. Planner Tool

The `Planner_tool` folder introduces an important AI-agent concept:
**planning before tool execution**.

``` text
Planner_tool/
├── planner.py
├── assistant.py
├── tools.py
└── test_planner.py
```

## Available Tools

The planner currently knows about three selectable tools:

  Tool                  Purpose
  --------------------- ---------------------------------------
  `get_current_time`    Returns the current date and time
  `roll_dice`           Generates a random number from 1 to 6
  `generate_password`   Generates a secure random password

`tools.py` also contains a `read_text_file(filename)` helper, although
it is not currently part of the planner's selectable tool list.

------------------------------------------------------------------------

# 17. How the Planner Works

The planner receives the user's request and asks the Qwen model to
select the appropriate tool.

It returns **only the tool name**.

Example:

``` text
"What time is it?"
        |
        v
     Planner
        |
        v
get_current_time
        |
        v
Execute Tool
        |
        v
Tool Result
        |
        v
Final Response
```

If no tool is required:

``` text
none
```

The assistant can then answer the request directly using the LLM.

------------------------------------------------------------------------

# 18. Planner Components

## `planner.py`

Contains:

``` python
choose_tool(user_request)
```

This function sends the request to the local LLM and selects one of the
available tools.

## `tools.py`

Contains:

``` python
get_current_time()
roll_dice()
generate_password(length=12)
read_text_file(filename)
```

## `assistant.py`

The assistant:

1.  Accepts the user's request.
2.  Calls the planner.
3.  Executes the selected tool.
4.  Sends the tool result back to the LLM.
5.  Produces the final response.

Type:

``` text
quit
```

to exit.

## `test_planner.py`

Tests planner decisions for requests such as:

-   Current time
-   Password generation
-   Dice rolling
-   Normal questions that do not require a tool

------------------------------------------------------------------------

# 19. Running the Planner Agent

From the repository root:

``` powershell
cd Planner_tool
```

Activate the root virtual environment if it is not already active:

``` powershell
..\.venv\Scripts\Activate.ps1
```

Run:

``` powershell
python assistant.py
```

Example requests:

``` text
What time is it?
Roll a dice
Generate a password
Explain Python
```

Run the planner test:

``` powershell
python test_planner.py
```

------------------------------------------------------------------------

# 20. Planner Workflow

``` text
                   User Request
                        |
                        v
                +----------------+
                |    Planner     |
                +----------------+
                        |
                        v
               Choose Tool Name
                        |
          +-------------+-------------+
          |             |             |
          v             v             v
   current_time     roll_dice    password
          |             |             |
          +-------------+-------------+
                        |
                        v
                  Execute Tool
                        |
                        v
                   Tool Result
                        |
                        v
                 Response LLM
                        |
                        v
                    User Answer
```

If the planner returns `none`:

``` text
User Request
     |
     v
  Planner
     |
     v
   none
     |
     v
   Qwen 3
     |
     v
  Answer
```

------------------------------------------------------------------------

# 21. RAG Implementation

The `RAG_Implimentation` folder demonstrates Retrieval-Augmented
Generation.

``` text
RAG_Implimentation/
├── rag.py
├── retriever.py
├── similarity.py
├── test_embedding.py
├── test_retriever.py
└── knowledge/
```

Pipeline:

``` text
Documents
    |
    v
Nomic Embeddings
    |
    v
Vector Representations
    |
    v
Similarity Search
    |
    v
Relevant Context
    |
    v
Qwen 3
    |
    v
Answer
```

Run:

``` powershell
cd RAG_Implimentation
python rag.py
```

------------------------------------------------------------------------

# 22. RAG vs Planner

These components solve different problems.

### RAG

RAG retrieves relevant information to provide context to the LLM.

``` text
Question
   |
   v
Embedding
   |
   v
Retrieve relevant information
   |
   v
Qwen
   |
   v
Answer
```

### Planner

The planner decides which tool should be used for a request.

``` text
Question
   |
   v
Planner
   |
   v
Tool Selection
   |
   v
Execute Tool
   |
   v
Response
```

Together, these concepts can form a more capable AI-agent system.

------------------------------------------------------------------------

# 23. Planner + Tools + RAG --- Future Architecture

A future integrated agent could combine these concepts:

``` text
                         User
                          |
                          v
                    AI Agent / Planner
                          |
             +------------+------------+
             |            |            |
             v            v            v
          RAG Search    Tools      File Tools
             |            |            |
             +------------+------------+
                          |
                          v
                       Context
                          |
                          v
                       Qwen 3
                          |
                          v
                       Answer
```

Possible workflow:

1.  Understand the user's request.
2.  Decide whether information retrieval is required.
3.  Decide whether a tool needs to be executed.
4.  Retrieve relevant documents when necessary.
5.  Execute the selected tool.
6.  Combine tool results and retrieved context.
7.  Generate the final response.

------------------------------------------------------------------------

# 24. Common Problems and Solutions

## OpenAI module not found

``` text
ModuleNotFoundError: No module named 'openai'
```

Solution:

``` powershell
python -m pip install openai
```

## Qwen model not found

``` text
model "qwen3:4b" not found
```

Solution:

``` powershell
ollama pull qwen3:4b
```

## Embedding model not found

``` text
model "nomic-embed-text" not found
```

Solution:

``` powershell
ollama pull nomic-embed-text
```

## Wrong Qwen model name

Correct:

``` text
qwen3:4b
```

Incorrect:

``` text
quen3:4b
```

Verify:

``` powershell
ollama list
```

## Pip launcher error after renaming the project folder

If the virtual environment references an old project path:

``` powershell
deactivate
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install openai python-dotenv numpy
```

------------------------------------------------------------------------

# 25. Git Feature Branch Workflow

Check the current branch:

``` powershell
git branch
```

Fetch remote branches:

``` powershell
git fetch origin
```

List all branches:

``` powershell
git branch -a
```

Create a new feature branch:

``` powershell
git switch main
git pull
git switch -c feature/my-feature
```

Push:

``` powershell
git push -u origin feature/my-feature
```

------------------------------------------------------------------------

# 26. Commit Changes

``` powershell
git status
git add .
git commit -m "Add planner tool"
git push
```

------------------------------------------------------------------------

# 27. Complete Setup --- Quick Start

``` powershell
git clone https://github.com/ayush13kvns/AI-Agent-Development.git
cd AI-Agent-Development

python -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install openai python-dotenv numpy

ollama pull qwen3:4b
ollama pull nomic-embed-text

ollama list
```

Test the basic agent:

``` powershell
cd Basic_agent
python hello_ai.py
```

Test the planner:

``` powershell
cd ..\Planner_tool
python assistant.py
```

Test RAG:

``` powershell
cd ..\RAG_Implimentation
python rag.py
```

------------------------------------------------------------------------

# 28. Important Notes

-   Activate `.venv` before installing packages or running Python
    applications.
-   Use the exact model names `qwen3:4b` and `nomic-embed-text`.
-   Keep `.env` files containing secrets out of GitHub.
-   Ollama must be installed and available locally.
-   The examples in this repository are independent learning components
    and can later be combined into a complete agent architecture.

------------------------------------------------------------------------

# 29. Future Enhancements

Possible next steps:

-   Connect Planner and RAG into a single agent
-   Add more tools
-   Add dynamic tool registration
-   Add tool schemas
-   Add function/tool calling
-   Add persistent conversation memory
-   Add document chunking
-   Add vector database support
-   Add metadata filtering
-   Add PDF ingestion
-   Add web search tools
-   Add file creation/editing tools
-   Add streaming responses
-   Add source/citation display
-   Add FastAPI backend
-   Add web UI
-   Add automated tests
-   Add Docker deployment

------------------------------------------------------------------------

# 30. Technology Stack

  Technology          Purpose
  ------------------- -----------------------------
  Python              Application development
  Ollama              Local LLM runtime
  Qwen 3 4B           Local language model
  Nomic Embed Text    Text embeddings
  OpenAI Python SDK   API client
  python-dotenv       Environment configuration
  NumPy               Numerical/vector operations
  Git                 Version control
  GitHub              Source-code repository

------------------------------------------------------------------------

# 31. Author

**Ayush Kumar**

GitHub:

https://github.com/ayush13kvns

Repository:

https://github.com/ayush13kvns/AI-Agent-Development
