# MCPServer

A minimal reference implementation of a Model Context Protocol (MCP) server using FastAPI.

I wanted to write a simple version of MCP Server to see how different components work together.  
I will keep updating this as I add more.

### Current Status

---

### Resources

TODOS [x] /resources/list – returns a sample file resource  
TODOS [x] /resources/read – reads and returns content from `resource.txt`  
TODOS [ ] /resources/subscribe – allow clients to subscribe to resource changes  
TODOS [ ] /notifications/resources/updated – notify clients when subscribed resources are updated  

---

### Prompts

TODOS [x] /prompts/list – lists available prompt templates  
TODOS [x] /prompts/get – returns formatted prompt messages  
TODOS [ ] Dynamic prompt generation  
TODOS [ ] Multi-step workflow support  

---

### Tools

TODOS [x] /tools/list – returns metadata about available tools  
TODOS [x] /tools/call – executes a shell command with subprocess  
TODOS [ ] Add authentication/security for tools  
TODOS [ ] Add support for multiple tool types (e.g. API, async)  

---

### Infra / Misc

TODOS [x] Class-based models  
TODOS [x] Uses @dataclass + asdict for serialization  
TODOS [x] Client script (`mcp_client.py`) to test all endpoints  
TODOS [ ] Add Pydantic validation for incoming requests  
TODOS [ ] Add subscription and notification logic  

---

## Getting Started

### Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Requests

Install dependencies:

```bash
pip install -r requirements.txt
