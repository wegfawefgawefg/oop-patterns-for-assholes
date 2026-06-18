"""
State via enum

What:
    Change an object's behavior when its mode changes.

When / why:
    Use this when full state classes are overkill. An enum is often enough for
    simple workflows like pending payment -> ready to ship -> shipped.
"""

from enum import Enum, auto


class OrderMode(Enum):
    PENDING_PAYMENT = auto()
    READY_TO_SHIP = auto()
    SHIPPED = auto()


class Order:
    def __init__(self) -> None:
        self.mode = OrderMode.PENDING_PAYMENT

    def pay(self) -> None:
        if self.mode == OrderMode.PENDING_PAYMENT:
            print("payment accepted")
            self.mode = OrderMode.READY_TO_SHIP
            return

        if self.mode == OrderMode.READY_TO_SHIP:
            print("already paid")
            return

        print("already complete")

    def ship(self) -> None:
        if self.mode == OrderMode.PENDING_PAYMENT:
            print("cannot ship before payment")
            return

        if self.mode == OrderMode.READY_TO_SHIP:
            print("order shipped")
            self.mode = OrderMode.SHIPPED
            return

        print("already shipped")


def main() -> None:
    order = Order()
    order.ship()
    order.pay()
    order.ship()
    order.ship()


if __name__ == "__main__":
    main()
