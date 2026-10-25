"""Labels for support tickets."""

from __future__ import annotations

from triage import claude

LABELS = ("billing", "bug", "account", "other")
SYSTEM = (
    "You label customer support tickets. Answer with exactly one word: "
    + ", ".join(LABELS)
    + "."
)


def label(ticket: str) -> str:
    answer = claude.ask(SYSTEM, ticket).lower().strip(".")
    return answer if answer in LABELS else "other"
