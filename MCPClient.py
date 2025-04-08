import requests
import json

BASE_URL = "http://localhost:3000"

def pretty_print(title, response):
    print(f"\n=== {title} ===")
    print(f"Status Code: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        print("Raw Response:", response.text)

def test_resources():
    print("\n--- Testing Resources ---")
    
    # List resources
    res_list = requests.get(f"{BASE_URL}/resources/list")
    pretty_print("Resources List", res_list)

    if res_list.status_code == 200:
        resource = res_list.json()
        uri = resource.get("uri")
        if uri:
            # Read resource
            res_read = requests.post(f"{BASE_URL}/resources/read", json={"uri": uri})
            pretty_print("Read Resource", res_read)

def test_prompts():
    print("\n--- Testing Prompts ---")
    
    # List prompts
    prompts = requests.get(f"{BASE_URL}/prompts/list")
    pretty_print("Prompts List", prompts)

    # Valid prompt request: analyze-code
    code_test = {
        "name": "analyze-code",
        "language": "Python",
        "value": "def foo():\n  return 42"
    }
    code_prompt = requests.post(f"{BASE_URL}/prompts/get", json=code_test)
    pretty_print("Prompt: analyze-code", code_prompt)

    # Valid prompt request: analyze-error
    error_test = {
        "name": "analyze-error",
        "language": "Python",
        "value": "NameError: name 'x' is not defined"
    }
    error_prompt = requests.post(f"{BASE_URL}/prompts/get", json=error_test)
    pretty_print("Prompt: analyze-error", error_prompt)

def test_tools():
    print("\n--- Testing Tools ---")

    # List tools
    tools = requests.get(f"{BASE_URL}/tools/list")
    pretty_print("Tools List", tools)

    # Call tool (example: echo command)
    tool_call_data = {
        "name": "execute command",
        "inputSchema": {
            "command": "echo",
            "args": ["Hello, MCP!"]
        }
    }
    result = requests.post(f"{BASE_URL}/tools/call", json=tool_call_data)
    pretty_print("Call Tool: execute_command", result)

if __name__ == "__main__":
    print("🚀 MCP Client Starting...\n")
    test_resources()
    test_prompts()
    test_tools()
    print("\n✅ All tests completed.")
