"""
Observer

What:
    Let subscribers react when an object publishes an event.

When / why:
    Use it for domain events: order placed, player leveled up, cache invalidated,
    achievement unlocked.
"""

from typing import Protocol




def email(self, event: str, data: dict) -> None:
    if event == "order_placed":
        print(f"email receipt to {data['email']}")


def track_analytics(self, event: str, data: dict) -> None:
    print(f"analytics event={event} user={data['user_id']}")

def send(subs   ) -> None:
    print("send email receipt")
    for sub in subs:
        do_something("order_placed", {"user_id": "u1", "email": "u1@example.com"})

def main() -> None:
    subs = [email, track_analytics]
    send(subs)


if __name__ == "__main__":
    main()
