"""
Flyweight

What:
    Share repeated immutable data instead of storing it on every object.

When / why:
    Use it when a game or backend workload creates many similar objects, such as
    thousands of particles, tiles, or permission records.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TileType:
    name: str
    texture: str
    walkable: bool


class TileTypeFactory:
    def __init__(self) -> None:
        self._types: dict[str, TileType] = {}

    def get(self, name: str, texture: str, walkable: bool) -> TileType:
        if name not in self._types:
            self._types[name] = TileType(name, texture, walkable)
        return self._types[name]


@dataclass
class Tile:
    x: int
    y: int
    tile_type: TileType


def main() -> None:
    factory = TileTypeFactory()
    grass = factory.get("grass", "grass.png", True)
    wall = factory.get("wall", "stone.png", False)
    level = [Tile(0, 0, grass), Tile(1, 0, grass), Tile(2, 0, wall)]

    for tile in level:
        print(tile)
    print(level[0].tile_type is level[1].tile_type)


if __name__ == "__main__":
    main()
