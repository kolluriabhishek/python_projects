# Importing required libraries
from nsepy import get_history
from datetime import date
import pandas as pd

# Set the stock symbol and date range
symbol = 'SBIN' # SBI Bank stock
start_date = date.today() # Today's date
end_date = date.today()

# Get the historical data using the NSEpy library
data = get_history(symbol=symbol, start=start_date, end=end_date)

# Print the last recorded price
last_price = data['Close'][-1]
print(f"Last recorded price of {symbol} is {last_price}")

# Get real-time stock data
real_time_data = pd.DataFrame(get_history(symbol=symbol, start=end_date, end=end_date, index=True))
real_time_price = real_time_data['Close'][-1]
print(f"Real-time price of {symbol} is {real_time_price}")
