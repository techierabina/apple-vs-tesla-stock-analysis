# Apple vs Tesla Stock Analysis

## Overview
This project compares the stock performance of Apple (AAPL) and Tesla (TSLA).  
It includes data download, analysis, visualization, and rolling averages.

## Project Structure
- `data/` - CSV files with stock data  
- `notebooks/` - Jupyter notebooks for exploration  
- `src/` - Python scripts for analysis  
- `results/` - Plots and output  
- `main.py` - Main script  
- `requirements.txt` - Dependencies
- `README.md`  - This file

## Features
📈 Automated stock data download using Yahoo Finance API
📊 Comprehensive statistical analysis of stock performance
📉 Daily returns calculation and rolling averages
🎨 Professional visualizations and charts
💾 Export results to CSV and image files

## Installation
# Prerequisites
Python 3.12+
Conda (recommended) or pip

# Setup Instructions
Clone the repository:

```bash
git clone https://github.com/techierabina/apple-vs-tesla-stock-analysis.git
cd apple-vs-tesla-stock-analysis
```

Create a Conda environment:
```bash
conda create -n stock-analysis python=3.12 -y
conda activate stock-analysis
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
# Quick Start
Run the main analysis script:
bashpython main.py
What the Script Does
This will automatically:

# Download Apple (AAPL) and Tesla (TSLA) stock data and save to data/ folder
Compute daily returns and rolling averages (30-day default)
Perform statistical analysis comparing both stocks
Generate comprehensive visualizations
Save all plots and results to the results/ folder

# Running Jupyter Notebooks
For interactive exploration:
bashjupyter notebook notebooks/
Dependencies

# Python 3.12+
pandas - Data manipulation and analysis
numpy - Numerical computing
matplotlib - Plotting library
seaborn - Statistical data visualization
yfinance - Yahoo Finance API wrapper
scikit-learn - Machine learning utilities
statsmodels - Statistical modeling
jupyter - Interactive notebook environment

# Sample Output
The project generates several types of visualizations:
Generated Plots

# Closing Prices Over Time - Historical stock price trends
30-Day Rolling Average - Smoothed price movements
Returns Distribution - Statistical distribution of daily returns
Correlation Analysis - Relationship between AAPL and TSLA
Volatility Comparison - Risk assessment charts

All plots are automatically saved in the results/ folder as high-resolution PNG files.
Data Output

Raw stock data: data/aapl_data.csv, data/tsla_data.csv
Analysis results: results/analysis_summary.csv
Statistical metrics: results/performance_metrics.csv

# Configuration
You can modify the analysis parameters by editing main.py:
python# Example configuration options
START_DATE = '2020-01-01'  # Analysis start date
END_DATE = '2023-12-31'    # Analysis end date
ROLLING_WINDOW = 30        # Rolling average window (days)
Example Results
Here's what you can expect from the analysis:
Key Metrics Generated:

# Average daily returns
Volatility (standard deviation)
Sharpe ratio
Maximum drawdown
Correlation coefficient

Sample Statistics:
AAPL vs TSLA Performance (2020-2023)
=====================================
AAPL Average Return: 0.12%
TSLA Average Return: 0.18%
Correlation: 0.65
Contributing
Contributions are welcome! Here's how you can help:

Fork the repository
Create a feature branch: git checkout -b feature-name
Make your changes and add tests if applicable
Commit your changes: git commit -m 'Add new feature'
Push to the branch: git push origin feature-name
Submit a pull request

# Roadmap

 Add more stocks for comparison (e.g., Google, Microsoft)
 Implement technical indicators (RSI, MACD, Bollinger Bands)
 Add machine learning price prediction models
 Create interactive web dashboard
 Add real-time data updates


# Author
Rabina Karki

# GitHub: @techierabina


This project is for educational purposes and should not be considered as financial advice.