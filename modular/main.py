from menu import print_banner, print_menu
from order import (
    ask_to_order,
    get_menu_item,
    get_quantity,
    ask_order_another,
    calculate_order,
    print_order_summary,
    print_item_added
)
from receipt import print_receipt, print_goodbye


def main():

    menu = {
        "1": {"name": "Cebu Lechon Belly (per kg)", "price": 550.00, "category": "Specialty"},
        "2": {"name": "Grilled Blue Marlin Steak", "price": 320.00, "category": "Grilled"},
        "3": {"name": "Sinuglaw (Tuna & Pork)", "price": 280.00, "category": "Cebuano Classic"},
        "4": {"name": "Buttered Garlic Shrimp", "price": 350.00, "category": "Seafood"},
        "5": {"name": "Chili Crab (per 500g)", "price": 450.00, "category": "Seafood"},
        "6": {"name": "Baked Scallops (6 pcs)", "price": 220.00, "category": "Seafood"},
        "7": {"name": "Kinilaw na Tuna", "price": 200.00, "category": "Cebuano Classic"},
        "8": {"name": "Seafood Paella (good for 3)", "price": 480.00, "category": "Rice"},
        "9": {"name": "Grilled Squid (Pusit)", "price": 250.00, "category": "Grilled"},
        "10": {"name": "Lapu-Lapu Escabeche", "price": 380.00, "category": "Seafood"},
        "11": {"name": "Seafood Chowder Soup", "price": 180.00, "category": "Soup"},
        "12": {"name": "Halo-Halo Special", "price": 120.00, "category": "Dessert"},
        "13": {"name": "Mango Shake", "price": 95.00, "category": "Beverage"},
        "14": {"name": "Buko Juice (Fresh)", "price": 75.00, "category": "Beverage"}
    }

    discounts = {
        "senior": 0.20,
        "pwd": 0.20,
        "bulk": 0.10,
        "loyalty": 0.05
    }

    bulk_discount_threshold = 2000.00

    print_banner()
    print_menu(menu)

    if not ask_to_order():
        print_goodbye()
        return

    cart = []

    while True:
        item_key = get_menu_item(menu)
        quantity = get_quantity()

        item_name = menu[item_key]["name"]
        item_price = menu[item_key]["price"]
        item_total = item_price * quantity

        cart.append({
            "name": item_name,
            "price": item_price,
            "quantity": quantity,
            "total": item_total
        })

        print_item_added(
            item_name,
            quantity,
            item_total
        )

        if not ask_order_another():
            break

    print_order_summary(cart)

    (
        subtotal,
        discount_rate,
        discount_amount,
        grand_total,
        discount_names
    ) = calculate_order(
        cart,
        discounts,
        bulk_discount_threshold
    )

    print_receipt(
        cart,
        subtotal,
        discount_rate,
        discount_amount,
        grand_total,
        discount_names
    )


if __name__ == "__main__":
    main()