"""
Composite

What:
    Treat single objects and groups of objects through the same interface.

When / why:
    Use it for trees: game scene graphs, menu hierarchies, file explorers, or
    nested permissions.
"""

from abc import ABC, abstractmethod


class SceneNode(ABC):
    @abstractmethod
    def render(self, indent: int = 0) -> None:
        pass


class Sprite(SceneNode):
    def __init__(self, name: str) -> None:
        self.name = name

    def render(self, indent: int = 0) -> None:
        print(" " * indent + f"sprite: {self.name}")


class Group(SceneNode):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: list[SceneNode] = []

    def add(self, node: SceneNode) -> None:
        self.children.append(node)

    def render(self, indent: int = 0) -> None:
        print(" " * indent + f"group: {self.name}")
        for child in self.children:
            child.render(indent + 2)


def main() -> None:
    level = Group("level_1")
    player_layer = Group("players")
    player_layer.add(Sprite("mage"))
    player_layer.add(Sprite("archer"))
    level.add(Sprite("background"))
    level.add(player_layer)
    level.render()


if __name__ == "__main__":
    main()
