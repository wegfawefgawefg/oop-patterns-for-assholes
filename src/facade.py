"""
Facade

What:
    Provide one simple interface over several lower-level services.

When / why:
    Use it when a route handler or game action would otherwise coordinate too
    many subsystems directly.
"""


class InventoryService:
    def reserve(self, sku: str) -> None:
        print(f"reserved inventory for {sku}")


class PaymentService:
    def charge(self, user_id: str, cents: int) -> str:
        print(f"charged {user_id} {cents} cents")
        return "payment_123"


class ShippingService:
    def create_label(self, sku: str) -> str:
        return f"label_for_{sku}"


class CheckoutFacade:
    def __init__(self) -> None:
        self.inventory = InventoryService()
        self.payments = PaymentService()
        self.shipping = ShippingService()

    def buy_now(self, user_id: str, sku: str, cents: int) -> dict:
        self.inventory.reserve(sku)
        payment_id = self.payments.charge(user_id, cents)
        label = self.shipping.create_label(sku)
        return {"payment_id": payment_id, "shipping_label": label}


def main() -> None:
    checkout = CheckoutFacade()
    print(checkout.buy_now("user_42", "keyboard", 8999))


if __name__ == "__main__":
    main()
