"""
Prototype

What:
    Create new objects by cloning an existing configured object.

When / why:
    Use it when setup is expensive or verbose, such as spawning game enemies
    from a tuned template and changing only a few fields.
"""

from copy import deepcopy
from dataclasses import dataclass, replace


@dataclass
class Enemy:
    kind: str
    hp: int
    damage: int
    loot_table: list[str]
    x: int = 0
    y: int = 0

    def clone_at(self, x: int, y: int) -> "Enemy":
        clone = deepcopy(self)
        clone.x = x
        clone.y = y
        return clone


def main() -> None:
    drone_template = Enemy("security drone", hp=30, damage=6, loot_table=["scrap", "battery"])
    cave_wave = [drone_template.clone_at(10, 5), drone_template.clone_at(14, 8)]
    boss = replace(drone_template.clone_at(20, 10), kind="heavy drone", hp=120, damage=14)

    for enemy in [*cave_wave, boss]:
        print(enemy)


if __name__ == "__main__":
    main()
