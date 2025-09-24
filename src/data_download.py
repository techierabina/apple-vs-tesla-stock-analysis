import yfinance as yf
import pandas as pd

def download_data(ticker, start_date, end_date, save_path=None):
    data = yf.download(ticker, start=start_date, end=end_date)[['Close']]
    data.rename(columns={'Close': f'{ticker}_Close'}, inplace=True)
    if save_path:
        data.to_csv(save_path)
    return data
