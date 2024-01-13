from binance.client import Client
import pandas as pd


def getHistoricalData(ticker_symbol: str, interval:str, start_date:str) -> pd.DataFrame:
    
    client = Client()
    historical = client.get_historical_klines(ticker_symbol, interval, start_date)
    historical_df = formatHistData(historical)

    return historical_df

def formatHistData(historical):

    # Convert historical data to pd.Dataframe
    hist_df = pd.DataFrame(historical)
    hist_df.columns = [
            'Open Time',
            'Open',
            'High',
            'Low',
            'Close',
            'Volume',
            'Close Time',
            'Quote Asset Volume',
            'Number of Trades',
            'Taker buy base Asset Volume',
            'Taker buy quote Asset Volume',
            'Ignore'
        ]
    
    #remove uneccesary data
    hist_df = hist_df.drop(columns=['Ignore'])

    # Convert int64 to DateTime
    hist_df['Open Time'] = pd.to_datetime(hist_df['Open Time'], unit='ms')
    hist_df['Close Time'] = pd.to_datetime(hist_df['Close Time'], unit='ms')

    # convert object to float values
    numerics = [
            'Open',
            'High',
            'Low',
            'Close',
            'Volume',
            'Quote Asset Volume',
            'Number of Trades',
            'Taker buy base Asset Volume',
            'Taker buy quote Asset Volume',
        ]
    
    hist_df[numerics] = hist_df[numerics].apply(pd.to_numeric)

    return hist_df

def get_all_tickers():

    client = Client()
    all_data = client.get_all_tickers()
    ticker_list = []

    for coin in all_data:
        ticker_list.append(coin["symbol"])

    ticker_df = pd.DataFrame(ticker_list, columns=["Ticker"])
    ticker_df["Ticker"] = ticker_df["Ticker"].astype('|S80')
    
    return ticker_df

def convert_hist_to_percentagechange(historical):
    
    close_values = ['Open Time','Close']
    close_df = historical[close_values]

    #Add Percentage Change Column
    close_df['Percentage Change'] = close_df['Close'].pct_change()*100
    close_df = close_df.dropna()
    close_df = close_df.reset_index(drop=True)
    close_df = close_df[['Open Time', 'Percentage Change']]
    
    return close_df
