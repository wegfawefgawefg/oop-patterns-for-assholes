"""
Factory Method, but without classes

What:
    Pick the right function from runtime input.

When / why:
    Use this when object creation would be ceremony. If all you need is "which
    parser function should handle this provider?", a function factory is enough.
"""

from collections.abc import Callable


WebhookParser = Callable[[dict], dict]


def parse_stripe_webhook(payload: dict) -> dict:
    return {"provider": "stripe", "event": payload["type"], "user_id": payload["data"]["user"]}


def parse_github_webhook(payload: dict) -> dict:
    return {"provider": "github", "event": payload["action"], "user_id": payload["sender"]["login"]}


def get_parser(provider: str) -> WebhookParser:
    if provider == "stripe":
        return parse_stripe_webhook
    if provider == "github":
        return parse_github_webhook
    raise ValueError(f"Unknown webhook provider: {provider}")


def main() -> None:
    incoming = [
        ("stripe", {"type": "invoice.paid", "data": {"user": "cus_123"}}),
        ("github", {"action": "opened", "sender": {"login": "octavia"}}),
    ]

    for provider, payload in incoming:
        parse = get_parser(provider)
        print(parse(payload))


if __name__ == "__main__":
    main()
