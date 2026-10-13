# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 400,
    "AMZN": 200
}

# Variable to store total investment
total_investment = 0

print("====================================")
print("       STOCK PORTFOLIO TRACKER")
print("====================================")

while True:

    # Display available stocks
    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(stock, "→ $", price)

    # Get stock name from user
    stock_name = input("\nEnter stock name: ").upper()

    # Check whether stock exists
    if stock_name in stock_prices:

        # Get quantity
        quantity = int(input("Enter quantity: "))

        # Get price of selected stock
        price = stock_prices[stock_name]

        # Calculate investment for this stock
        investment = price * quantity

        # Add to total investment
        total_investment += investment

        print("\nStock:", stock_name)
        print("Price per share: $", price)
        print("Quantity:", quantity)
        print("Investment: $", investment)

    else:
        print("Stock not found. Please enter a valid stock.")

    # Ask whether user wants to add another stock
    choice = input("\nDo you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

# Display final result
print("\n====================================")
print("       PORTFOLIO SUMMARY")
print("====================================")
print("Total Investment: $", total_investment)
print("Thank you for using Stock Portfolio Tracker!")