"""
Interpreter

What:
    Model a tiny language or rule syntax as objects that can evaluate input.

When / why:
    Use it for small, controlled rule systems. If the grammar grows large, use a
    real parser library instead.
"""

from abc import ABC, abstractmethod


class Rule(ABC):
    @abstractmethod
    def matches(self, event: dict) -> bool:
        pass


class FieldEquals(Rule):
    def __init__(self, field: str, value: str) -> None:
        self.field = field
        self.value = value

    def matches(self, event: dict) -> bool:
        return event.get(self.field) == self.value


class And(Rule):
    def __init__(self, *rules: Rule) -> None:
        self.rules = rules

    def matches(self, event: dict) -> bool:
        return all(rule.matches(event) for rule in self.rules)


def main() -> None:
    suspicious_login = And(FieldEquals("type", "login"), FieldEquals("country", "unknown"))
    events = [
        {"type": "login", "country": "us"},
        {"type": "login", "country": "unknown"},
    ]

    for event in events:
        print(event, "matches?", suspicious_login.matches(event))


if __name__ == "__main__":
    main()
