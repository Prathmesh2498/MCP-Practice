from typing import Optional, Dict, Any
from dataclasses import dataclass, asdict
import subprocess

@dataclass
class Tool:
    name: str
    inputSchema: Dict[str, Any]
    description: Optional[str] = None

def _list_tools():
    execute_command_tool = Tool(
        name="execute_command",
        description="Run a shell command",
        inputSchema={
            "type": "object",
            "properties": {
                "command": {"type": "string"},
                "args": {"type": "array", "items": {"type": "string"}}
            }
        }
    )
    return [asdict(execute_command_tool)]

def _call_tool(data):
    if data.get("name") == "execute command":
        input_schema = data.get("inputSchema", {})
        command = input_schema.get("command")
        args = input_schema.get("args", [])

        if not command:
            return {"error": "Missing 'command' in inputSchema"}

        try:
            result = subprocess.run(
                [command] + args,
                capture_output=True,
                text=True,
                check=True,
                shell=True  #Only for Windows
            )
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except subprocess.CalledProcessError as e:
            return {
                "error": "Command failed",
                "stdout": e.stdout,
                "stderr": e.stderr,
                "returncode": e.returncode
            }
        except Exception as e:
            return {"error": str(e)}
    return {"error": "Unsupported tool"}
