from typing import List, Optional
from dataclasses import dataclass, asdict, field

@dataclass
class _PromptArgument:
    name: str
    description: Optional[str] = None
    required: Optional[bool] = False

@dataclass
class Prompt:
    name: str
    description: Optional[str] = None
    arguments: List[_PromptArgument] = field(default_factory=list)

def _get_prompts(name, language, value):
    if name == "analyze-code":
        return {
            "description": f"Analyze {language} code for potential improvements",
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": (
                            f"Please analyze the following {language} code for potential improvements:\n\n"
                            f"```{language.lower()}\n{value}\n```"
                        )
                    }
                }
            ]
        }

    elif name == "analyze-error":
        return {
            "description": f"Explain a {language} error message",
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": (
                            f"I encountered the following error in my {language} code:\n\n"
                            f"`{value}`\n\n"
                            "Please explain what this means and how to fix it."
                        )
                    }
                }
            ]
        }

    else:
        return {}

def _list_prompts():
    PROMPTS = [
        Prompt(
            name="analyze-code",
            description="Analyze code for potential improvements",
            arguments=[
                _PromptArgument(name="language", description="Programming language", required=True),
                _PromptArgument(name="code", description="Code to analyze", required=True)
            ]
        ),
        Prompt(
            name="analyze-error",
            description="Explain an error message",
            arguments=[
                _PromptArgument(name="error", description="The error message", required=True),
                _PromptArgument(name="description", description="Context or description of the error", required=False)
            ]
        )
    ]
    return [asdict(p) for p in PROMPTS]
