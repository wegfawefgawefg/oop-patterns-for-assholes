"""
Adapter

What:
    Wrap an object with one interface so it can be used through another.

When / why:
    Use it when integrating third-party libraries or legacy services without
    spreading their awkward API across your codebase.
"""

from typing import Protocol


class PaymentGateway(Protocol):
    def charge_cents(self, user_id: str, cents: int) -> str:
        pass


class LegacyBillingClient:
    def make_payment(self, customer: str, dollars: float) -> dict:
        return {"payment_id": "pay_123", "customer": customer, "amount": dollars}


class LegacyBillingAdapter:
    def __init__(self, client: LegacyBillingClient) -> None:
        self.client = client

    def charge_cents(self, user_id: str, cents: int) -> str:
        result = self.client.make_payment(customer=user_id, dollars=cents / 100)
        return result["payment_id"]


def checkout(gateway: PaymentGateway) -> None:
    payment_id = gateway.charge_cents("user_42", 1999)
    print(f"charged successfully: {payment_id}")


def main() -> None:
    checkout(LegacyBillingAdapter(LegacyBillingClient()))


if __name__ == "__main__":
    main()
