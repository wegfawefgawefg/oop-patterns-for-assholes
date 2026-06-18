"""
Observer

What:
    Let subscribers react when an object publishes an event.

When / why:
    Use it for domain events: order placed, player leveled up, cache invalidated,
    achievement unlocked.
"""

from typing import Protocol


class Subscriber(Protocol):
    def update(self, event: str, data: dict) -> None:
        pass


class EventBus:
    def __init__(self) -> None:
        self.subscribers: list[Subscriber] = []

    def subscribe(self, subscriber: Subscriber) -> None:
        self.subscribers.append(subscriber)

    def publish(self, event: str, data: dict) -> None:
        for subscriber in self.subscribers:
            subscriber.update(event, data)


class EmailReceiptSender:
    def update(self, event: str, data: dict) -> None:
        if event == "order_placed":
            print(f"email receipt to {data['email']}")


class AnalyticsTracker:
    def update(self, event: str, data: dict) -> None:
        print(f"analytics event={event} user={data['user_id']}")


def main() -> None:
    bus = EventBus()
    bus.subscribe(EmailReceiptSender())
    bus.subscribe(AnalyticsTracker())
    bus.publish("order_placed", {"user_id": "u1", "email": "u1@example.com"})


if __name__ == "__main__":
    main()
