# Time Series Analysis Script

## Overview

This Python script performs time series analysis on a dataset containing date and price information. It utilizes linear regression to identify trends, analyzes residuals for deviations, and highlights months with significant price variations.

## Setup

1. **Environment Setup:**
    - Ensure you have Python installed on your system.
    - Install the required libraries using: `pip install pandas numpy matplotlib`.

2. **Dataset Format:**
    - Prepare a CSV file with two columns: 'Dates' and 'Prices', where 'Dates' represent the date information, and 'Prices' represent the corresponding prices.

    - Example Dataset (see 'Nat_Gas.csv' in the repository for formatting):
      ```
      Dates, Prices
      10/31/20, 1.5
      11/30/20, 2.0
      12/31/20, 1.8
      ```

3. **Running the Script:**
    - Adjust the script if necessary (e.g., file paths, date formats).
    - Run the script using: `python LinearTrend.py`.

## Script Functionality

- **Linear Regression:**
    - Calculates a linear trend for the prices over time.

- **Residual Analysis:**
    - Identifies residuals (differences between actual prices and predicted prices).

- **Cheap and Costly Months:**
    - Determines months where prices deviate significantly from the linear trend.

- **Visualization:**
    - Plots the original prices, linear trend, and highlights cheap and costly months.

## Results

- The script outputs the linear regression slope, most repeatedly cheap months, and most repeatedly costly months.

## Example Dataset

- The repository includes an example dataset (`Nat_Gas.csv`) with natural gas prices. Use it as a reference for formatting your dataset.

## Notes

- Ensure your dataset follows the required format, and adjust date formats in the script if necessary.
