"""
Memento

What:
    Capture object state so it can be restored later without exposing internals.

When / why:
    Use it for undo, editor checkpoints, save games, and draft restore flows.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class DraftSnapshot:
    title: str
    body: str


class BlogDraft:
    def __init__(self) -> None:
        self.title = ""
        self.body = ""

    def snapshot(self) -> DraftSnapshot:
        return DraftSnapshot(self.title, self.body)

    def restore(self, snapshot: DraftSnapshot) -> None:
        self.title = snapshot.title
        self.body = snapshot.body

    def __str__(self) -> str:
        return f"{self.title}: {self.body}"


def main() -> None:
    draft = BlogDraft()
    draft.title = "Launch notes"
    draft.body = "Version one shipped."
    saved = draft.snapshot()

    draft.body = "Accidentally deleted everything"
    print(draft)
    draft.restore(saved)
    print(draft)


if __name__ == "__main__":
    main()
