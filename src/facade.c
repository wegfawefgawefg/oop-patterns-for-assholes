/*
Facade in C

What:
    Provide one simple function over several lower-level services.

When / why:
    Use it when caller code would otherwise coordinate too many subsystems
    directly. In C, structs plus function pointers can model the "service"
    pieces without classes.

Build / run:
    cc -std=c11 -Wall -Wextra -pedantic src/facade.c -o /tmp/facade
    /tmp/facade
*/

#include <stdio.h>

typedef struct InventoryService InventoryService;
typedef struct PaymentService PaymentService;
typedef struct ShippingService ShippingService;

struct InventoryService {
    void (*reserve)(InventoryService *self, const char *sku);
};

struct PaymentService {
    const char *(*charge)(PaymentService *self, const char *user_id, int cents);
};

struct ShippingService {
    const char *(*create_label)(ShippingService *self, const char *sku);
};

typedef struct {
    const char *payment_id;
    const char *shipping_label;
} CheckoutResult;

typedef struct {
    InventoryService inventory;
    PaymentService payments;
    ShippingService shipping;
} CheckoutFacade;

void reserve_inventory(InventoryService *self, const char *sku) {
    (void)self;
    printf("reserved inventory for %s\n", sku);
}

const char *charge_payment(PaymentService *self, const char *user_id, int cents) {
    (void)self;
    printf("charged %s %d cents\n", user_id, cents);
    return "payment_123";
}

const char *create_shipping_label(ShippingService *self, const char *sku) {
    (void)self;
    printf("created shipping label for %s\n", sku);
    return "label_for_keyboard";
}

CheckoutFacade make_checkout_facade(void) {
    CheckoutFacade facade = {
        .inventory = {.reserve = reserve_inventory},
        .payments = {.charge = charge_payment},
        .shipping = {.create_label = create_shipping_label},
    };

    return facade;
}

CheckoutResult checkout_buy_now(
    CheckoutFacade *facade,
    const char *user_id,
    const char *sku,
    int cents
) {
    facade->inventory.reserve(&facade->inventory, sku);
    const char *payment_id = facade->payments.charge(&facade->payments, user_id, cents);
    const char *shipping_label = facade->shipping.create_label(&facade->shipping, sku);

    CheckoutResult result = {
        .payment_id = payment_id,
        .shipping_label = shipping_label,
    };

    return result;
}

int main(void) {
    CheckoutFacade checkout = make_checkout_facade();
    CheckoutResult result = checkout_buy_now(&checkout, "user_42", "keyboard", 8999);

    printf("{payment_id: %s, shipping_label: %s}\n", result.payment_id, result.shipping_label);
    return 0;
}
