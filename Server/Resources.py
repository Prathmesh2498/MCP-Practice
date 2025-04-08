from typing import Optional
from dataclasses import dataclass, asdict
import os

@dataclass
class Resource:
    uri: str
    name: str
    description: Optional[str] = None
    mimeType: Optional[str] = None

def _list_resources():
    res = Resource(
        uri="file://resource.txt",
        name="Sample Resource",
        description="Hello World",
        mimeType="application/text"
    )
    return asdict(res)

def read_resource(uri: str) -> dict:
    if not uri.startswith("file://"):
        raise ValueError("Only file:// URIs are supported")

    rel_path = uri.replace("file://", "")
    abs_path = os.path.join(os.getcwd(), rel_path)

    if not os.path.isfile(abs_path):
        raise FileNotFoundError(f"File not found: {abs_path}")

    with open(abs_path, "r", encoding="utf-8") as f:
        text = f.read()

    return {
        "contents": [
            {
                "uri": uri,
                "mimeType": "text/plain",
                "text": text
            }
        ]
    }
