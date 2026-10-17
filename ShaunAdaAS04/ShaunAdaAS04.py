

def calculate_change(open_price, close_price):
    return close_price - open_price


def calculate_percent_change(open_price, close_price):
    change = close_price - open_price
    return (change / open_price) * 100


def get_market_status(change):
    if change > 0:
        return "GAIN"
    elif change < 0:
        return "LOSS"
    else:
        return "NO CHANGE"


def display_summary(
    stock_name, open_price, close_price, change, percent_change, status
):
    print()
    print("DAILY STOCK SUMMARY")
    print("Stock:", stock_name)
    print("Price Change:", change)
    print("Percent Change:", f"{percent_change:.2f}%")
    print("Status:", status)


def main():
    stock_name = input("Enter stock name: ")
    open_price = float(input("Enter opening price: "))
    close_price = float(input("Enter closing price: "))

    change = calculate_change(open_price, close_price)
    percent_change = calculate_percent_change(open_price, close_price)
    status = get_market_status(change)

    display_summary(
        stock_name, open_price, close_price, change, percent_change, status
    )


if __name__ == "__main__":
    main()
