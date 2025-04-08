from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from Resources import _list_resources, read_resource
from Prompts import _list_prompts, _get_prompts
from Tools import _list_tools, _call_tool

app = FastAPI()

#RESOURCES
@app.get("/resources/list")
async def list_resources(request: Request):
    return JSONResponse(status_code=200, content=_list_resources())

@app.post("/resources/read")
async def read_resources(request: Request):
    data = await request.json()
    uri = data.get("uri")
    if not uri:
        return JSONResponse(status_code=400, content={"error": "Missing 'uri' in request body"})
    try:
        CONTENT = read_resource(uri)
        return JSONResponse(status_code=200, content=CONTENT)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# TODOS 
# resources/subscribe
# notifications/resources/updated

#PROMPTS
@app.get("/prompts/list")
async def list_prompts(request: Request):
    return JSONResponse(status_code=200, content=_list_prompts())

@app.post("/prompts/get")
async def get_prompts(request: Request):
    data = await request.json()
    name = data.get("name")
    language = data.get("language")
    value = data.get("value")
    CONTENT = _get_prompts(name, language, value)
    if not CONTENT:
        return JSONResponse(status_code=400, content="Missing/Invalid values")
    else:
        return JSONResponse(status_code=200, content=CONTENT)

# TODOS 
# Multi-step Workflows
# Dyanamic Prompts

#Tools
@app.get("/tools/list")
async def list_tools(request: Request):
    return JSONResponse(status_code=200, content=_list_tools())

@app.post("/tools/call")
async def call_tool(request: Request):
    data = await request.json()
    RESULT = _call_tool(data)
    if not RESULT:
        return JSONResponse(status_code=500, content="Internal Server Error")
    else:
        return JSONResponse(status_code=200, content=RESULT) 

# TODOS
# Security
# Error handling

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)



