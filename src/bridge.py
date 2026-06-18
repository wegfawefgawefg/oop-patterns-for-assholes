"""
Bridge

What:
    Split an abstraction from its implementation so both sides can vary.

When / why:
    Use it when you have two independent axes of change, such as notification
    type and delivery channel.
"""

from abc import ABC, abstractmethod


class Sender(ABC):
    @abstractmethod
    def send(self, destination: str, body: str) -> None:
        pass


class EmailSender(Sender):
    def send(self, destination: str, body: str) -> None:
        print(f"email to {destination}: {body}")


class SmsSender(Sender):
    def send(self, destination: str, body: str) -> None:
        print(f"sms to {destination}: {body}")


class Alert:
    def __init__(self, sender: Sender) -> None:
        self.sender = sender

    def trigger(self, destination: str) -> None:
        self.sender.send(destination, self.message())

    def message(self) -> str:
        raise NotImplementedError


class PasswordResetAlert(Alert):
    def message(self) -> str:
        return "Use this link to reset your password."


class ServerDownAlert(Alert):
    def message(self) -> str:
        return "Production server is not responding."


def main() -> None:
    PasswordResetAlert(EmailSender()).trigger("dev@example.com")
    ServerDownAlert(SmsSender()).trigger("+15551234567")


if __name__ == "__main__":
    main()
