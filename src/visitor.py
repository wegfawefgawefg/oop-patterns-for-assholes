"""
Visitor

What:
    Add operations to a set of object types without putting every operation on
    those objects.

When / why:
    Use it when a stable object model needs many outside operations, such as
    exporting, validating, pricing, or rendering different game entities.
"""

from abc import ABC, abstractmethod


class GameObject(ABC):
    @abstractmethod
    def accept(self, visitor: "GameObjectVisitor") -> None:
        pass


class Chest(GameObject):
    def __init__(self, coins: int) -> None:
        self.coins = coins

    def accept(self, visitor: "GameObjectVisitor") -> None:
        visitor.visit_chest(self)


class Enemy(GameObject):
    def __init__(self, xp: int) -> None:
        self.xp = xp

    def accept(self, visitor: "GameObjectVisitor") -> None:
        visitor.visit_enemy(self)


class GameObjectVisitor(ABC):
    @abstractmethod
    def visit_chest(self, chest: Chest) -> None:
        pass

    @abstractmethod
    def visit_enemy(self, enemy: Enemy) -> None:
        pass


class RewardTotalVisitor(GameObjectVisitor):
    def __init__(self) -> None:
        self.coins = 0
        self.xp = 0

    def visit_chest(self, chest: Chest) -> None:
        self.coins += chest.coins

    def visit_enemy(self, enemy: Enemy) -> None:
        self.xp += enemy.xp


def main() -> None:
    room: list[GameObject] = [Chest(50), Enemy(20), Chest(10)]
    visitor = RewardTotalVisitor()
    for obj in room:
        obj.accept(visitor)
    print(f"room rewards: {visitor.coins} coins, {visitor.xp} xp")


if __name__ == "__main__":
    main()
