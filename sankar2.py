# Stock Portfolio Tracker - Single Line Input Version

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

# Step 2: Get all stock inputs in one line
print("Enter your stock holdings in the format: SYMBOL:QTY, separated by commas")
print("Example: AAPL:5, TSLA:3, GOOGL:2\n")

user_input = input("Enter your stocks: ")

# Step 3: Process the input
portfolio = {}
entries = user_input.split(",")
for entry in entries:
    try:
        stock, qty = entry.strip().split(":")
        stock = stock.strip().upper()
        qty = int(qty.strip())
        if stock in stock_prices:
            portfolio[stock] = qty
        else:
            print(f"⚠ {stock} not found in price list, skipped.")
    except ValueError:
        print(f"⚠ Invalid entry format: {entry}")

# Step 4: Calculate total investment
total_investment = 0
print("\n📊 Your Portfolio Summary:")
print("-" * 40)
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print("-" * 40)
print(f"💰 Total Investment Value: ${total_investment}")

# Step 5: Optionally save to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-" * 40 + "\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total Investment Value: ${total_investment}\n")
    print("✅ Portfolio summary saved to 'portfolio_summary.txt'")
else:
    print("❌ Portfolio not saved.")