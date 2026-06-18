"""
Adapter via Interface

What:
    Define the interface your app wants, let new code implement it directly, and
    wrap old or third-party code with an adapter so it also fits.

When / why:
    Use this when you are standardizing messy integrations. New payment gateways
    can follow your app's clean interface, while old gateways get adapted instead
    of leaking their weird method names and data shapes everywhere.
"""

from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def charge_cents(self, user_id: str, cents: int) -> str:
        pass


class ModernPaymentGateway(PaymentGateway):
    def charge_cents(self, user_id: str, cents: int) -> str:
        print(f"modern gateway charged {user_id} {cents} cents")
        return "modern_payment_123"


class LegacyBillingClient:
    def make_payment(self, customer: str, dollars: float) -> dict:
        print(f"legacy billing charged {customer} ${dollars:.2f}")
        return {"payment_id": "legacy_payment_456"}


class LegacyBillingAdapter(PaymentGateway):
    def __init__(self, client: LegacyBillingClient) -> None:
        self.client = client

    def charge_cents(self, user_id: str, cents: int) -> str:
        result = self.client.make_payment(customer=user_id, dollars=cents / 100)
        return result["payment_id"]


def checkout(gateway: PaymentGateway, user_id: str, cents: int) -> None:
    payment_id = gateway.charge_cents(user_id, cents)
    print(f"checkout saved payment id: {payment_id}")


def main() -> None:
    checkout(ModernPaymentGateway(), "user_42", 1999)
    checkout(LegacyBillingAdapter(LegacyBillingClient()), "user_99", 2500)


if __name__ == "__main__":
    main()
