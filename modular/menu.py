def print_banner():
    print("=" * 60)
    print("         ISLA SUGBO SEAFOOD GRILL")
    print("              Cebu City, Philippines")
    print('         "Lami kaayo ang dagat sa Sugbo!"')
    print("=" * 60)
    print()


def print_menu(menu):
    print("+" + "-" * 58 + "+")
    print("|" + " " * 15 + "M E N U" + " " * 35 + "|")
    print("+" + "-" * 58 + "+")
    print("|  #   {:<35} {:>12}  |".format("Item", "Price (P)"))
    print("+" + "-" * 58 + "+")

    for key, item in menu.items():
        print(
            "|  {:<3} {:<35} P{:>10,.2f}  |".format(
                key,
                item["name"],
                item["price"]
            )
        )

    print("+" + "-" * 58 + "+")
    print()