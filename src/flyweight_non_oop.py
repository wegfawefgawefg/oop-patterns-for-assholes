"""
Flyweight via enum

What:
    Share repeated immutable data instead of storing it on every object.

When / why:
    Use this when the shared values are known ahead of time. An enum gives you
    one shared object per tile type without writing a factory.
"""

from dataclasses import dataclass
from enum import Enum


class TileType(Enum):
    GRASS = ("grass.png", True)
    WALL = ("stone.png", False)
    WATER = ("water.png", False)

    def __init__(self, texture: str, walkable: bool) -> None:
        self.texture = texture
        self.walkable = walkable


@dataclass
class Tile:
    x: int
    y: int
    tile_type: TileType


def main() -> None:
    level = [
        Tile(0, 0, TileType.GRASS),
        Tile(1, 0, TileType.GRASS),
        Tile(2, 0, TileType.WALL),
        Tile(3, 0, TileType.WATER),
    ]

    for tile in level:
        print(
            tile.x,
            tile.y,
            tile.tile_type.name.lower(),
            tile.tile_type.texture,
            "walkable" if tile.tile_type.walkable else "blocked",
        )

    print(level[0].tile_type is level[1].tile_type)


if __name__ == "__main__":
    main()
