# Equity Fund Analysis

## Project Overview

This project is designed to analyze the performance of 150 U.S. companies across multiple industries, based on data from the most recent quarter.
The analysis provides insights for fund managers looking to rebalance their holdings.
The analysis covers multiple key financial metrics, including debt-to-equity ratio and debt-to-income ratio.
The data is analyzed using Python, with the following objectives:

1. **Data Import**: Import the data from the Excel file.
2. **Duplicate Detection**: Identify and report duplicate rows in the dataset.
3. **Descriptive Statistics by State**: Group companies by state and calculate descriptive statistics (mean, median, min, max) for numeric financial variables.
4. **Debt-to-Equity Ratio**: Identify businesses with negative debt-to-equity ratios.
5. **Debt-to-Income Ratio**: Calculate and store the debt-to-income ratio for each business.
6. **Data Concatenation**: Merge the debt-to-income ratio into the original dataset for further analysis.
7. **Output Results**: Save the final data frames to Excel files for further review.

## Project Files

- **`analysis.py`**: The Python script containing the logic for data processing, analysis, and result generation.
- **`D598 Data Set.xlsx`**: The input dataset containing financial data for 150 U.S. companies

## Data Analysis

The analysis follows these steps:

### 1. **Data Import**
   - The `D598 Data Set.xlsx` is imported into a Pandas data frame for analysis.

### 2. **Duplicate Detection**
   - Duplicate rows in the data set are identified using `data_frame.duplicated()` and are printed for review.

### 3. **Grouping and Descriptive Statistics**
   - Companies are grouped by their business state, and descriptive statistics (mean, median, min, and max) are calculated for all numeric columns (excluding the Business ID).

### 4. **Debt-to-Equity Ratio Calculation**
   - The script calculates the debt-to-equity ratio for each company and filters out businesses with negative ratios.

### 5. **Debt-to-Income Ratio Calculation**
   - The debt-to-income ratio, defined as the ratio of long-term debt to total revenue, is computed for each business and stored in a new data frame.

### 6. **Data Concatenation**
   - The original data frame is concatenated with the newly computed debt-to-income ratio data.

### 7. **Output**
   - The final results are saved to three Excel files: `state_statistics.xlsx`, `negative_dte.xlsx`, and `data_frame_with_dti.xlsx`.

## Installation

To run this project, ensure you have the following dependencies installed:

```bash
pip install pandas numpy openpyxl
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/rudydesplan/d598.git
   ```

2. Navigate to the project directory:
   ```bash
   cd d598
   ```

3. Place the data file (`D598 Data Set.xlsx`) in the project directory.

4. Run the Python script:
   ```bash
   python analysis.py
   ```

5. After running the script, the following files will be generated in the project directory:
   - `state_statistics.xlsx`
   - `negative_dte.xlsx`
   - `data_frame_with_dti.xlsx`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out at `rdespl2@wgu.edu`.
