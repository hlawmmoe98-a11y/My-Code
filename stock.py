import yfinance as yf
data = yf.download("TSLA", period="1mo")
print(type(data))
print(data.close)

