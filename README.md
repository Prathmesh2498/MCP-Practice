# MCPServer

A minimal reference implementation of a Model Context Protocol (MCP) server using FastAPI.

I wanted to write a simple version of MCP Server to see how different components work together.  
I will keep updating this as I add more.

### Current Status

---

### Resources

[x] /resources/list – returns a sample file resource  
[x] /resources/read – reads and returns content from `resource.txt`  
[ ] /resources/subscribe – allow clients to subscribe to resource changes  
[ ] /notifications/resources/updated – notify clients when subscribed resources are updated  

---

### Prompts

[x] /prompts/list – lists available prompt templates  
[x] /prompts/get – returns formatted prompt messages  
[ ] Dynamic prompt generation  
[ ] Multi-step workflow support  

---

### Tools

[x] /tools/list – returns metadata about available tools  
[x] /tools/call – executes a shell command with subprocess  
[ ] Add authentication/security for tools  
[ ] Add support for multiple tool types (e.g. API, async)  

---

### Infra / Misc

[x] Class-based models  
[x] Uses @dataclass + asdict for serialization  
[x] Client script (`mcp_client.py`) to test all endpoints  
[ ] Add Pydantic validation for incoming requests  
[ ] Add subscription and notification logic  

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
