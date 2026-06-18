"""
State

What:
    Change an object's behavior when its internal state changes.

When / why:
    Use it when conditionals around status values are spreading everywhere, such
    as order workflows, game AI, or connection lifecycles.
"""

from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def pay(self, order: "Order") -> None:
        pass

    @abstractmethod
    def ship(self, order: "Order") -> None:
        pass


class PendingPayment(OrderState):
    def pay(self, order: "Order") -> None:
        print("payment accepted")
        order.state = ReadyToShip()

    def ship(self, order: "Order") -> None:
        print("cannot ship before payment")


class ReadyToShip(OrderState):
    def pay(self, order: "Order") -> None:
        print("already paid")

    def ship(self, order: "Order") -> None:
        print("order shipped")
        order.state = Shipped()


class Shipped(OrderState):
    def pay(self, order: "Order") -> None:
        print("already complete")

    def ship(self, order: "Order") -> None:
        print("already shipped")


class Order:
    def __init__(self) -> None:
        self.state: OrderState = PendingPayment()

    def pay(self) -> None:
        self.state.pay(self)

    def ship(self) -> None:
        self.state.ship(self)


def main() -> None:
    order = Order()
    order.ship()
    order.pay()
    order.ship()
    order.ship()


if __name__ == "__main__":
    main()
