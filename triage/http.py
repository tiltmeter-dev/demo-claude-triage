"""The one place that talks HTTP, so tests can swap it out."""

from __future__ import annotations

import json
import urllib.request
from typing import Any


def post_json(url: str, body: dict[str, Any], headers: dict[str, str]) -> Any:
    data = json.dumps(body).encode()
    request = urllib.request.Request(url, data=data, method="POST")
    request.add_header("content-type", "application/json")
    for name, value in headers.items():
        request.add_header(name, value)
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)
