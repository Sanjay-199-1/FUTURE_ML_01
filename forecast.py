import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Sample - Superstore.csv", encoding='ISO-8859-1')

# Group by order date to get daily sales
df['Order Date'] = pd.to_datetime(df['Order Date'])
daily_sales = df.groupby('Order Date')['Sales'].sum().reset_index()
daily_sales.columns = ['ds', 'y']

# Initialize and train Prophet model
model = Prophet()
model.fit(daily_sales)

# Create future dataframe
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Save forecast output
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('forecast_output.csv', index=False)

# Plot and save forecast
fig = model.plot(forecast)
plt.title("Sales Forecast for Next 30 Days")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig('forecast_plot.png')
plt.show()
