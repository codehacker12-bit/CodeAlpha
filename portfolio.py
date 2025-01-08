import yfinance as yf #Library to get real-time stock price data

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # store stock details (symbol, quantity, price)

    def add_stock(self, symbol, quantity):
        """Add stock to portfolio."""
        current_price = self.get_current_price(symbol)
        if current_price is None: # If the stock price cannot be fetched, display an error message
            print(f"Failed to fetch data for {symbol}. Please check the symbol.")
            return
        if symbol in self.portfolio: # If the stock is already in the portfolio, update the quantity
            self.portfolio[symbol]['quantity'] += quantity
        else: # If it’s new, add it with the price and quantity
            self.portfolio[symbol] = {'quantity': quantity, 'price': current_price}
        print(f"Added {quantity} shares of {symbol} to the portfolio.")

    def remove_stock(self, symbol, quantity):
        """Remove stock from portfolio."""
        if symbol in self.portfolio:
            if self.portfolio[symbol]['quantity'] >= quantity:
                self.portfolio[symbol]['quantity'] -= quantity
                if self.portfolio[symbol]['quantity'] == 0:
                    del self.portfolio[symbol]
                print(f"Removed {quantity} shares of {symbol}.")
            else:
                print(f"Not enough shares of {symbol} to remove.")
        else:
            print(f"{symbol} is not in the portfolio.")

    def get_current_price(self, symbol):
        """Fetch the current stock price."""
        try:
            stock = yf.Ticker(symbol) # Uses yfinance to fetch the latest stock price
            data = stock.history(period="1d")
            if data.empty:
                print(f"No data returned for {symbol}.")
                return None
            price = data['Close'].iloc[-1] # Retrieves the closing price for the most recent day
            return price
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None

    def track_performance(self):
        """Calculate the total value of the portfolio."""
        total_value = 0
        for symbol, data in self.portfolio.items():
            current_price = self.get_current_price(symbol)
            if current_price: # Multiplies the current price by the quantity and adds it to the total
                total_value += current_price * data['quantity']
        return total_value

    def display_portfolio(self):
        """Display the portfolio details."""
        print("\nPortfolio Dashboard:")
        if not self.portfolio:
            print("Your portfolio is empty.")
            return
        for symbol, data in self.portfolio.items():
            print(f"{symbol}: {data['quantity']} shares @ {data['price']:.2f} (initial price)")
        print(f"Total Portfolio Value: {self.track_performance():.2f}\n")


if __name__ == "__main__":
    portfolio = StockPortfolio()

    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. Display Current Portfolio\n4. Exit")
        choice = input("Your choice, please: ")

        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
            quantity = int(input("Ready to invest? Enter the quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Input the stock symbol for removal: ").upper()
            quantity = int(input("Input the quantity of stocks for removal: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == "3":
            portfolio.display_portfolio()
        elif choice == "4":
            print("Goodbye! Remember, buy low and sell high!")
            break
        else:
            print("Invalid selection. Kindly try again with a valid input.")
