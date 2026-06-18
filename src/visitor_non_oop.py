"""
Visitor, but without the pattern

What:
    Calculate over a mixed list of game objects with plain data and plain
    functions.

When / why:
    Use this when the object model is small and you do not need the ceremony of
    accept methods, visitor base classes, and one method per object type.
"""

from dataclasses import dataclass


@dataclass
class Chest:
    coins: int


@dataclass
class Enemy:
    xp: int


GameObject = Chest | Enemy


def total_rewards(room: list[GameObject]) -> tuple[int, int]:
    coins = 0
    xp = 0

    for obj in room:
        if isinstance(obj, Chest):
            coins += obj.coins
        elif isinstance(obj, Enemy):
            xp += obj.xp
        else:
            raise TypeError(f"Unknown object type: {type(obj)}")

    return coins, xp


def main() -> None:
    room: list[GameObject] = [
        Chest(coins=50),
        Enemy(xp=20),
        Chest(coins=10),
    ]

    coins, xp = total_rewards(room)
    print(f"room rewards: {coins} coins, {xp} xp")


if __name__ == "__main__":
    main()
