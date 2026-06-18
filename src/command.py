"""
Command

What:
    Represent an action as an object.

When / why:
    Use it for queues, undo/redo, audit logs, game inputs, or background jobs.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SendEmailCommand(Command):
    def __init__(self, to: str, subject: str) -> None:
        self.to = to
        self.subject = subject

    def execute(self) -> None:
        print(f"email sent to {self.to}: {self.subject}")


class RecalculateLeaderboardCommand(Command):
    def execute(self) -> None:
        print("leaderboard recalculated")


class JobQueue:
    def __init__(self) -> None:
        self.jobs: list[Command] = []

    def enqueue(self, command: Command) -> None:
        self.jobs.append(command)

    def run(self) -> None:
        while self.jobs:
            self.jobs.pop(0).execute()


def main() -> None:
    queue = JobQueue()
    queue.enqueue(SendEmailCommand("player@example.com", "Daily reward ready"))
    queue.enqueue(RecalculateLeaderboardCommand())
    queue.run()


if __name__ == "__main__":
    main()
