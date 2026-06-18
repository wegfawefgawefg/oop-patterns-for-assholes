"""
Singleton

What:
    Ensure one shared instance exists for a class.

When / why:
    Use carefully. It can be okay for one shared settings object in a small app
    or game, but it is easy to overuse and can make tests annoying.
"""


class Bag:
    def __init__(self) -> None:
        self.items: list[str] = []

class Cum:
    count: Bag | None = None

    def __init__(self) -> None:
        
        
        if Cum.count is None:
            Cum.count = Bag()
        self.count = Cum.count


        self.count.items.append("cum")


def main() -> None:
    c1 = Cum()
    c2 = Cum()
    print(c1.count.items)
    print(c2.count.items)


if __name__ == "__main__":
    main()
