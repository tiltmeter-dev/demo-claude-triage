# Ticket Triage

Labels incoming support tickets with Claude (billing, bug, account or other), over plain
HTTP to the Anthropic Messages API. Written in late 2024.

```bash
uv run --no-project --with pytest python -m pytest -q
```

## A Tiltmeter demo

This code was written for the Messages API of late 2024.
[Tiltmeter](https://github.com/tiltmeter-dev/tiltmeter) follows the OpenAPI spec Anthropic's
SDKs are generated from, compares the 2024 version with today's, and the `API changes`
workflow opens a pull request that adapts the code. The agent's edits are tested before the
pull request opens.
