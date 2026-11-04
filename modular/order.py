def ask_to_order():
    while True:
        response = input(
            "Would you like to place an order? (yes/no): "
        ).strip().lower()

        if response in ["yes", "y"]:
            return True

        elif response in ["no", "n"]:
            return False

        else:
            print("Please enter 'yes' or 'no' only.")


def get_menu_item(menu):
    while True:
        choice = input("Enter menu item number: ").strip()

        if choice in menu:
            return choice

        print(
            "Invalid item number. Please choose from 1-{}.".format(
                len(menu)
            )
        )


def get_quantity():
    while True:
        qty = input("Enter quantity: ").strip()

        if qty.isdigit() and int(qty) > 0:
            return int(qty)

        print("Please enter a valid positive whole number.")


def ask_order_another():
    while True:
        response = input(
            "\nOrder another item? (yes/no): "
        ).strip().lower()

        if response in ["yes", "y", "oo", "opo"]:
            return True

        elif response in ["no", "n", "dili", "wala"]:
            return False

        else:
            print("Please enter 'yes' or 'no' only.")


def ask_discounts(subtotal, discounts, bulk_discount_threshold):
    applied_discounts = []
    total_discount_rate = 0.0

    print("\n" + "-" * 60)
    print("              D I S C O U N T S")
    print("-" * 60)

    is_senior_or_pwd = input(
        "Are you a Senior Citizen or PWD? (yes/no): "
    ).strip().lower()

    if is_senior_or_pwd in ["yes", "y"]:
        total_discount_rate += discounts["senior"]
        applied_discounts.append(
            "Senior Citizen / PWD (20%)"
        )

    has_loyalty = input(
        "Do you have a Loyalty Card? (yes/no): "
    ).strip().lower()

    if has_loyalty in ["yes", "y"]:
        total_discount_rate += discounts["loyalty"]
        applied_discounts.append(
            "Loyalty Card (5%)"
        )

    if subtotal >= bulk_discount_threshold:
        total_discount_rate += discounts["bulk"]
        applied_discounts.append(
            "Bulk Order >= P2,000 (10%)"
        )

    if total_discount_rate > 0.30:
        total_discount_rate = 0.30
        applied_discounts.append(
            "Maximum discount capped at 30%"
        )

    return total_discount_rate, applied_discounts


def calculate_order(cart, discounts, bulk_discount_threshold):
    subtotal = 0.0

    for item in cart:
        subtotal += item["total"]

    discount_rate, discount_names = ask_discounts(
        subtotal,
        discounts,
        bulk_discount_threshold
    )

    discount_amount = subtotal * discount_rate
    grand_total = subtotal - discount_amount

    return (
        subtotal,
        discount_rate,
        discount_amount,
        grand_total,
        discount_names
    )


def print_order_summary(cart):
    print("\n" + "-" * 60)
    print("             O R D E R  S U M M A R Y")
    print("-" * 60)

    print(
        "  {:<5} {:<30} {:>10} {:>10}".format(
            "Qty", "Item", "Price", "Total"
        )
    )

    print("  " + "-" * 56)

    for item in cart:
        print(
            "  {:<5} {:<30} P{:>8,.2f} P{:>8,.2f}".format(
                item["quantity"],
                item["name"][:30],
                item["price"],
                item["total"]
            )
        )

    print("  " + "-" * 56)
    print()


def print_item_added(name, qty, total):
    print(
        "  Added: {} x{} = P{:,.2f}".format(
            name,
            qty,
            total
        )
    )
    print()