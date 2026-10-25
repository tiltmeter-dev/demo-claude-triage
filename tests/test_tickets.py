from __future__ import annotations

from typing import Any

import pytest

from triage import claude, http, tickets


def answer(text: str, stop_reason: str = "end_turn") -> dict[str, Any]:
    return {
        "id": "msg_1",
        "type": "message",
        "role": "assistant",
        "model": claude.MODEL,
        "content": [{"type": "text", "text": text}],
        "stop_reason": stop_reason,
        "stop_sequence": None,
        "usage": {"input_tokens": 52, "output_tokens": 2},
    }


@pytest.fixture
def replies(monkeypatch: pytest.MonkeyPatch) -> list[dict[str, Any]]:
    queue: list[dict[str, Any]] = []
    monkeypatch.setattr(http, "post_json", lambda url, body, headers: queue.pop(0))
    return queue


def test_tickets_get_a_label(replies: list[dict[str, Any]]) -> None:
    replies += [answer("Billing."), answer("refund please")]
    assert tickets.label("I was charged twice") == "billing"
    assert tickets.label("??") == "other"


def test_a_truncated_answer_is_an_error(replies: list[dict[str, Any]]) -> None:
    replies.append(answer("bil", stop_reason="max_tokens"))
    with pytest.raises(claude.TruncatedAnswer):
        tickets.label("I was charged twice")
