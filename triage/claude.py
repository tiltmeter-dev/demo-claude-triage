"""Claude, through the Anthropic Messages API."""

from __future__ import annotations

import os

from triage import http

MESSAGES_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-3-5-sonnet-20241022"


class TruncatedAnswer(Exception):
    """Claude ran out of tokens before it finished."""


def ask(system: str, prompt: str, *, max_tokens: int = 64) -> str:
    response = http.post_json(
        MESSAGES_URL,
        {
            "model": MODEL,
            "max_tokens": max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": prompt}],
        },
        {
            "x-api-key": os.environ.get("ANTHROPIC_API_KEY", ""),
            "anthropic-version": "2023-06-01",
        },
    )
    stop_reason = response["stop_reason"]
    if stop_reason in ("end_turn", "stop_sequence"):
        return response["content"][0]["text"].strip()
    if stop_reason == "max_tokens":
        raise TruncatedAnswer(prompt[:40])
    raise ValueError(f"unexpected stop_reason {stop_reason!r}")  # tool_use: no tools here
