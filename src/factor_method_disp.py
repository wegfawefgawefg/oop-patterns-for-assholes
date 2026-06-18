"""
Factory Method via dispatch dictionary

What:
    Pick the right function by looking it up in a dictionary.

When / why:
    Use this when an if/elif factory starts looking noisy. A dispatch dictionary
    makes the mapping from input names to behavior direct and easy to extend.
"""

def parse_stripe_webhook(payload: dict) -> dict:
    return {"provider": "stripe", "event": payload["type"], "user_id": payload["data"]["user"]}


def parse_github_webhook(payload: dict) -> dict:
    return {"provider": "github", "event": payload["action"], "user_id": payload["sender"]["login"]}


parser_by_provider = {
    "stripe": parse_stripe_webhook,
    "github": parse_github_webhook,
}

def main() -> None:
    incoming = [
        ("stripe", {"type": "invoice.paid", "data": {"user": "cus_123"}}),
        ("github", {"action": "opened", "sender": {"login": "octavia"}}),
    ]

    for provider, payload in incoming:
        try:
            parse = parser_by_provider[provider]
            print(parse(payload))
        except KeyError:
            print(f"Unknown webhook provider: {provider}")


if __name__ == "__main__":
    main()
