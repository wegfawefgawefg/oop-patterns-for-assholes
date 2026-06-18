"""
Bridge, but without classes

What:
    Keep "what message should we send?" separate from "how do we send it?"

When / why:
    Use this shape when classes would be overkill. Plain functions are enough if
    you only need to mix alert messages with delivery methods.
"""

from collections.abc import Callable


Sender = Callable[[str, str], None]


def send_email(destination: str, body: str) -> None:
    print(f"email to {destination}: {body}")


def send_sms(destination: str, body: str) -> None:
    print(f"sms to {destination}: {body}")


def password_reset_message() -> str:
    return "Use this link to reset your password."


def server_down_message() -> str:
    return "Production server is not responding."


def trigger_alert(sender: Sender, destination: str, message: str) -> None:
    sender(destination, message)


def main() -> None:
    trigger_alert(send_email, "dev@example.com", password_reset_message())
    trigger_alert(send_sms, "+15551234567", server_down_message())
    trigger_alert(send_sms, "+15557654321", password_reset_message())


if __name__ == "__main__":
    main()
