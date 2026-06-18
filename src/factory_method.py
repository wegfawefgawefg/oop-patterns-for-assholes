"""
Factory Method

What:
    Put object creation behind a method so the caller asks for "the thing I need"
    instead of naming a concrete class directly.

When / why:
    Use it when backend code needs to choose an implementation from runtime input,
    such as webhook providers, payment gateways, or notification channels.
"""

from abc import ABC, abstractmethod


class WebhookParser(ABC):
    @abstractmethod
    def parse(self, payload: dict) -> dict:
        pass


class StripeWebhookParser(WebhookParser):
    def parse(self, payload: dict) -> dict:
        return {"provider": "stripe", "event": payload["type"], "user_id": payload["data"]["user"]}


class GitHubWebhookParser(WebhookParser):
    def parse(self, payload: dict) -> dict:
        return {"provider": "github", "event": payload["action"], "user_id": payload["sender"]["login"]}


def make_parser(provider: str) -> WebhookParser:
    if provider == "stripe":
        return StripeWebhookParser()
    if provider == "github":
        return GitHubWebhookParser()
    raise ValueError(f"Unknown webhook provider: {provider}")


def main() -> None:
    incoming = [
        ("stripe", {"type": "invoice.paid", "data": {"user": "cus_123"}}),
        ("github", {"action": "opened", "sender": {"login": "octavia"}}),
    ]

    for provider, payload in incoming:
        parser = make_parser(provider)
        print(parser.parse(payload))


if __name__ == "__main__":
    main()
