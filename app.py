# AI Stock Analyzer Project - Open Source
import yfinance as yf

def analyze_stock(stock):
    data = yf.download(stock, period="1mo")

    if data.empty:
        print("Invalid stock symbol")
        return

    latest_price = data['Close'].iloc[-1]
    avg_price = data['Close'].mean()

    print(f"\nStock: {stock}")
    print(f"Latest Price: {latest_price:.2f}")
    print(f"Average Price (1 month): {avg_price:.2f}")

    if latest_price > avg_price:
        print("Trend: Uptrend 📈")
    else:
        print("Trend: Downtrend 📉")

if __name__ == "__main__":
    stock = input("Enter stock symbol (e.g., RELIANCE.NS): ")
    analyze_stock(stock)
