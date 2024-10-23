import pandas as pd
import numpy as np
from typing import Any

# 1. Load the Data into a Data Frame
data_frame = pd.read_excel("D598 Data Set.xlsx")

# 2. Identify Duplicate Rows in the Data Set
duplicates = data_frame[data_frame.duplicated()]
if not duplicates.empty:
    print("Duplicate rows found:")
    print(duplicates)

# 3. Group IDs by State and Compute Descriptive Statistics
# Group data_frame by the 'Business State' column
grouped_data = data_frame.groupby('Business State')

# Select Numeric Columns, excluding 'Business ID'
numeric_columns = data_frame.select_dtypes(include=np.number).columns.tolist()
numeric_columns = [col for col in numeric_columns if col != 'Business ID']

# Compute Descriptive Statistics
state_statistics = grouped_data[numeric_columns].agg(['mean', 'median', 'min', 'max'])

# 4. Identify Businesses with Negative Debt-to-Equity Ratios
def calculate_debt_to_equity_ratio(row: pd.Series) -> float:
    """
    Calculate the Debt-to-Equity ratio for a business.

    Parameters:
    -----------------
    - row (pd.Series): A row of financial data for a business. The row must contain the columns 'Total Long-term Debt'
      and 'Total Equity'.

    Returns:
    -----------------
    - float: The Debt-to-Equity ratio calculated as 'Total Long-term Debt / Total Equity'.
      Returns NaN if 'Total Equity' is zero or missing.
    """
    total_equity = row['Total Equity']
    if total_equity == 0 or pd.isna(total_equity):
        return np.nan
    else:
        return row['Total Long-term Debt'] / total_equity

# Calculate Debt-to-Equity Ratio
data_frame['Debt-to-Equity Ratio'] = data_frame.apply(calculate_debt_to_equity_ratio, axis=1)

# Filter Negative Ratios
negative_dte = data_frame[data_frame['Debt-to-Equity Ratio'] < 0]

# 5. Create Debt-to-Income Ratio Data Frame
def calculate_debt_to_income_ratio(row: pd.Series) -> float:
    """
    Calculate the Debt-to-Income ratio for a business.

    Parameters:
    -----------------
    - row (pd.Series): A row of financial data for a business. The row must contain the columns 'Total Long-term Debt'
      and 'Total Revenue'.

    Returns:
    -----------------
    - float: The Debt-to-Income ratio calculated as 'Total Long-term Debt / Total Revenue'.
      Returns NaN if 'Total Revenue' is zero or missing.
    """
    total_revenue = row['Total Revenue']
    if total_revenue == 0 or pd.isna(total_revenue):
        return np.nan
    else:
        return row['Total Long-term Debt'] / total_revenue

# Assemble New Data Frame with Debt-to-Income Ratio
dti_data_frame = data_frame[['Business ID']].copy()
dti_data_frame['Debt-to-Income Ratio'] = data_frame.apply(calculate_debt_to_income_ratio, axis=1)

# 6. Concatenate Debt-to-Income Ratio with Original Data Frame
data_frame_with_dti = pd.merge(data_frame, dti_data_frame, on='Business ID', how='left')

# 7. Handle Exceptions and Missing Data
# Replace infinite values with NaN
data_frame_with_dti.replace([np.inf, -np.inf], np.nan, inplace=True)

# 8. Output Final Data Frames
# Save the results to Excel files
state_statistics.to_excel('state_statistics.xlsx')
negative_dte.to_excel('negative_dte.xlsx')
data_frame_with_dti.to_excel('data_frame_with_dti.xlsx', index=False)
