"""
Mediator

What:
    Centralize communication between objects so they do not all reference each
    other directly.

When / why:
    Use it when UI widgets, game systems, or workflow steps would otherwise form
    a tangled graph of direct calls.
"""


class MatchmakingMediator:
    def __init__(self) -> None:
        self.waiting_players: list[str] = []

    def player_ready(self, player_id: str) -> None:
        self.waiting_players.append(player_id)
        print(f"{player_id} entered queue")
        if len(self.waiting_players) >= 2:
            first = self.waiting_players.pop(0)
            second = self.waiting_players.pop(0)
            print(f"match created: {first} vs {second}")


class PlayerClient:
    def __init__(self, player_id: str, mediator: MatchmakingMediator) -> None:
        self.player_id = player_id
        self.mediator = mediator

    def click_ready(self) -> None:
        self.mediator.player_ready(self.player_id)


def main() -> None:
    mediator = MatchmakingMediator()
    PlayerClient("p1", mediator).click_ready()
    PlayerClient("p2", mediator).click_ready()


if __name__ == "__main__":
    main()
