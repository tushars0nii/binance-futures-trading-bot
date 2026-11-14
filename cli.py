from orders import (
    get_balance,
    get_positions,
    place_market_order,
    place_limit_order,
    cancel_order
)

from validators import (
    validate_side,
    validate_quantity,
    validate_price
)


def menu():

    while True:

        print("\n" + "=" * 40)
        print(" BINANCE FUTURES TRADING BOT ")
        print("=" * 40)

        print("1. Check Balance")
        print("2. Market Order")
        print("3. Limit Order")
        print("4. View Positions")
        print("5. Cancel Order")
        print("6. Exit")

        choice = input("\nSelect Option: ")

        try:

            if choice == "1":

                balance = get_balance()

                print(f"\nUSDT Balance: {balance}")

            elif choice == "2":

                symbol = input("Symbol: ").upper()

                side = validate_side(
                    input("Side (BUY/SELL): ")
                )

                quantity = validate_quantity(
                    input("Quantity: ")
                )

                order = place_market_order(
                    symbol,
                    side,
                    quantity
                )

                print("\nMarket Order Submitted")
                print("Order ID:", order["orderId"])

            elif choice == "3":

                symbol = input("Symbol: ").upper()

                side = validate_side(
                    input("Side (BUY/SELL): ")
                )

                quantity = validate_quantity(
                    input("Quantity: ")
                )

                price = validate_price(
                    input("Price: ")
                )

                order = place_limit_order(
                    symbol,
                    side,
                    quantity,
                    price
                )

                print("\nLimit Order Submitted")
                print("Order ID:", order["orderId"])

            elif choice == "4":

                positions = get_positions()

                if positions:

                    print("\nOpen Positions:")

                    for p in positions:

                        print("-" * 30)
                        print("Symbol:", p["symbol"])
                        print("Quantity:", p["quantity"])
                        print("Entry Price:", p["entry_price"])

                else:

                    print("No Open Positions")

            elif choice == "5":

                symbol = input("Symbol: ").upper()

                order_id = int(
                    input("Order ID: ")
                )

                result = cancel_order(
                    symbol,
                    order_id
                )

                print(
                    "\nOrder Status:",
                    result["status"]
                )

            elif choice == "6":

                print("\nGoodbye!")
                break

            else:

                print("Invalid Choice")

        except Exception as e:

            print("\nError:")
            print(e)


if __name__ == "__main__":
    menu()