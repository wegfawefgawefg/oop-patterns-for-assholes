"""
Strategy

What:
    Put interchangeable algorithms behind the same interface.

When / why:
    Use it when behavior changes by configuration or context, such as pricing,
    ranking, pathfinding, compression, or fraud scoring.
"""

from typing import Protocol


class PricingStrategy(Protocol):
    def price_cents(self, base_cents: int) -> int:
        pass


class RegularPricing:
    def price_cents(self, base_cents: int) -> int:
        return base_cents


class SubscriberPricing:
    def price_cents(self, base_cents: int) -> int:
        return int(base_cents * 0.8)


class Checkout:
    def __init__(self, pricing: PricingStrategy) -> None:
        self.pricing = pricing

    def total(self, base_cents: int) -> int:
        return self.pricing.price_cents(base_cents)


def main() -> None:
    print("regular:", Checkout(RegularPricing()).total(1000))
    print("subscriber:", Checkout(SubscriberPricing()).total(1000))


if __name__ == "__main__":
    main()
