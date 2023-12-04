import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Set the working directory
os.chdir("C:\\Path\\To\\Folder")

# Read the CSV file (get help from panda documentation for different formats)
df = pd.read_csv('File_name.csv', parse_dates=['Dates'], date_parser=lambda x: pd.to_datetime(x, format='%m/%d/%y'))

# Plot prices against dates
fig, ax = plt.subplots()
ax.plot(df['Dates'], df['Prices'], label='Original Prices')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Insert_Commodity_Name_Prices')
ax.tick_params(axis='x', rotation=45)
ax.legend()

plt.show()

# Calculate days from start
days_from_start = (df['Dates'] - df['Dates'].min()).dt.days.values

# Use numpy's polyfit for linear regression
slope, intercept = np.polyfit(days_from_start, df['Prices'], 1)

# Calculate residuals (differences between actual prices and predicted prices)
residuals = df['Prices'] - (days_from_start * slope + intercept)

# Identify cheap and costly months based on residuals
mean_residual = np.mean(residuals)
std_residual = np.std(residuals)

# Define a threshold (adjust as needed)
threshold = 0.5 * std_residual

cheap_months = df.loc[residuals < -threshold, 'Dates'].dt.strftime('%B')
costly_months = df.loc[residuals > threshold, 'Dates'].dt.strftime('%B')

# Find up to 4 most repeated cheap and costly months
most_repeated_cheap_months = cheap_months.value_counts().nlargest(4).index.tolist()
most_repeated_costly_months = costly_months.value_counts().nlargest(4).index.tolist()

# Plot linear trend with cheap and costly months highlighted
fig, ax = plt.subplots()
ax.plot(df['Dates'], df['Prices'], label='Original Prices')
ax.plot(df['Dates'], days_from_start * slope + intercept, label='Linear Trend', linestyle='--')
ax.scatter(df.loc[residuals < -threshold, 'Dates'], df.loc[residuals < -threshold, 'Prices'], color='green', label='Cheap Months')
ax.scatter(df.loc[residuals > threshold, 'Dates'], df.loc[residuals > threshold, 'Prices'], color='red', label='Costly Months')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Linear Trend with Cheap and Costly Months Highlighted')
ax.tick_params(axis='x', rotation=45)
ax.legend()

plt.show()

print("Linear Regression: Slope =", slope)
print("Most Repeatedly Cheap Months:", most_repeated_cheap_months)
print("Most Repeatedly Costly Months:", most_repeated_costly_months)