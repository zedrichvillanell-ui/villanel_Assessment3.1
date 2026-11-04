from datetime import datetime


class IslaSugbo:

    def __init__(self):

        self.menu = {
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

        self.discounts = {
            "senior": 0.20,
            "pwd": 0.20,
            "bulk": 0.10,
            "loyalty": 0.05
        }

        self.bulk_discount_threshold = 2000.00

        self.cart = []

    def print_banner(self):

        print("=" * 60)
        print("         ISLA SUGBO SEAFOOD GRILL")
        print("              Cebu City, Philippines")
        print('         "Lami kaayo ang dagat sa Sugbo!"')
        print("=" * 60)
        print()

    def print_menu(self):

        print("+" + "-" * 58 + "+")
        print("|" + " " * 15 + "M E N U" + " " * 35 + "|")
        print("+" + "-" * 58 + "+")
        print("|  #   {:<35} {:>12}  |".format(
            "Item",
            "Price (P)"
        ))
        print("+" + "-" * 58 + "+")

        for key, item in self.menu.items():

            print(
                "|  {:<3} {:<35} P{:>10,.2f}  |".format(
                    key,
                    item["name"],
                    item["price"]
                )
            )

        print("+" + "-" * 58 + "+")
        print()

    def ask_to_order(self):

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

    def get_menu_item(self):

        while True:

            choice = input(
                "Enter menu item number: "
            ).strip()

            if choice in self.menu:
                return choice

            print(
                "Invalid item number. Please choose from 1-{}.".format(
                    len(self.menu)
                )
            )

    def get_quantity(self):

        while True:

            qty = input(
                "Enter quantity: "
            ).strip()

            if qty.isdigit() and int(qty) > 0:
                return int(qty)

            print(
                "Please enter a valid positive whole number."
            )

    def ask_order_another(self):

        while True:

            response = input(
                "\nOrder another item? (yes/no): "
            ).strip().lower()

            if response in ["yes", "y", "oo", "opo"]:
                return True

            elif response in ["no", "n", "dili", "wala"]:
                return False

            else:
                print(
                    "Please enter 'yes' or 'no' only."
                )

    def ask_discounts(self, subtotal):

        applied_discounts = []
        total_discount_rate = 0.0

        print("\n" + "-" * 60)
        print("              D I S C O U N T S")
        print("-" * 60)

        is_senior_or_pwd = input(
            "Are you a Senior Citizen or PWD? (yes/no): "
        ).strip().lower()

        if is_senior_or_pwd in ["yes", "y"]:

            total_discount_rate += self.discounts["senior"]

            applied_discounts.append(
                "Senior Citizen / PWD (20%)"
            )

        has_loyalty = input(
            "Do you have a Loyalty Card? (yes/no): "
        ).strip().lower()

        if has_loyalty in ["yes", "y"]:

            total_discount_rate += self.discounts["loyalty"]

            applied_discounts.append(
                "Loyalty Card (5%)"
            )

        if subtotal >= self.bulk_discount_threshold:

            total_discount_rate += self.discounts["bulk"]

            applied_discounts.append(
                "Bulk Order >= P2,000 (10%)"
            )

        if total_discount_rate > 0.30:

            total_discount_rate = 0.30

            applied_discounts.append(
                "Maximum discount capped at 30%"
            )

        return total_discount_rate, applied_discounts

    def calculate_order(self):

        subtotal = 0.0

        for item in self.cart:

            subtotal += item["total"]

        discount_rate, discount_names = self.ask_discounts(
            subtotal
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

    def print_order_summary(self):

        print("\n" + "-" * 60)
        print("             O R D E R  S U M M A R Y")
        print("-" * 60)

        print(
            "  {:<5} {:<30} {:>10} {:>10}".format(
                "Qty",
                "Item",
                "Price",
                "Total"
            )
        )

        print("  " + "-" * 56)

        for item in self.cart:

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

    def print_item_added(self, name, qty, total):

        print(
            "  Added: {} x{} = P{:,.2f}".format(
                name,
                qty,
                total
            )
        )

        print()

    def print_receipt(
        self,
        subtotal,
        discount_rate,
        discount_amount,
        grand_total,
        discount_names
    ):

        now = datetime.now()

        receipt_no = now.strftime(
            "%Y%m%d-%H%M%S"
        )

        print()

        print("+" + "=" * 50 + "+")

        print(
            "|" + " " * 10 +
            "ISLA SUGBO SEAFOOD GRILL" +
            " " * 16 + "|"
        )

        print(
            "|" + " " * 14 +
            "Cebu City, Philippines" +
            " " * 15 + "|"
        )

        print(
            "|" + " " * 12 +
            "Tel: (032) 123-4567" +
            " " * 19 + "|"
        )

        print("+" + "=" * 50 + "+")

        print(
            "|  Receipt No: {:<36} |".format(
                receipt_no
            )
        )

        print(
            "|  Date: {:<43} |".format(
                now.strftime("%B %d, %Y")
            )
        )

        print(
            "|  Time: {:<43} |".format(
                now.strftime("%I:%M %p")
            )
        )

        print("+" + "=" * 50 + "+")

        print(
            "|  Qty  Item                          Price     Total  |"
        )

        print("+" + "=" * 50 + "+")

        for item in self.cart:

            name = item["name"][:28]
            qty = item["quantity"]
            price = item["price"]
            total = item["total"]

            print(
                "|  {:>3}  {:<28} P{:>7,.2f} P{:>7,.2f}  |".format(
                    qty,
                    name,
                    price,
                    total
                )
            )

        print("+" + "=" * 50 + "+")

        print(
            "|  {:>30}  P{:>10,.2f}  |".format(
                "SUBTOTAL:",
                subtotal
            )
        )

        if discount_rate > 0:

            print("|" + " " * 50 + "|")

            for discount in discount_names:

                print(
                    "|  {:<45} |".format(
                        "* " + discount
                    )
                )

            print(
                "|  {:>30} -P{:>10,.2f}  |".format(
                    "DISCOUNT:",
                    discount_amount
                )
            )

        print("|" + " " * 50 + "|")

        print("+" + "=" * 50 + "+")

        print(
            "|  {:>30}  P{:>10,.2f}  |".format(
                "GRAND TOTAL:",
                grand_total
            )
        )

        print("+" + "=" * 50 + "+")

        print(
            "|" + " " * 8 +
            "Thank you for dining with us!" +
            " " * 12 + "|"
        )

        print(
            "|" + " " * 6 +
            '"Lami kaayo ang dagat sa Sugbo!"' +
            " " * 10 + "|"
        )

        print(
            "|" + " " * 12 +
            "Please come again!" +
            " " * 20 + "|"
        )

        print("+" + "=" * 50 + "+")
        print()

    def print_goodbye(self):

        print()

        print("=" * 60)
        print(
            "     Thank you for visiting Isla Sugbo Seafood Grill!"
        )
        print(
            "         We hope to serve you next time."
        )
        print("=" * 60)

        print()

    def run(self):

        self.print_banner()

        self.print_menu()

        if not self.ask_to_order():

            self.print_goodbye()

            return

        while True:

            item_key = self.get_menu_item()

            quantity = self.get_quantity()

            item_name = self.menu[item_key]["name"]

            item_price = self.menu[item_key]["price"]

            item_total = item_price * quantity

            self.cart.append({
                "name": item_name,
                "price": item_price,
                "quantity": quantity,
                "total": item_total
            })

            self.print_item_added(
                item_name,
                quantity,
                item_total
            )

            if not self.ask_order_another():
                break

        self.print_order_summary()

        (
            subtotal,
            discount_rate,
            discount_amount,
            grand_total,
            discount_names
        ) = self.calculate_order()

        self.print_receipt(
            subtotal,
            discount_rate,
            discount_amount,
            grand_total,
            discount_names
        )