# Crypto Asset Historical Spot Price Analysis

## Overview

This Python program performs historical analysis on crypto asset spot prices, aiming to identify leading and lagging indicator pairs. The analysis involves utilizing the Binance API for fetching historical data, Websockets for real-time data updates, and the Dynamic Time Warping (DTW) algorithm for comparing time series data.

## Features

- **Historical Data Retrieval:** Utilizes the Binance API to fetch historical spot prices for crypto assets.
- **Real-time Updates:** Incorporates Websockets for real-time updates on crypto asset spot prices.
- **Dynamic Time Warping (DTW):** Applies DTW algorithm for measuring similarity between time series data and identifying leading/lagging indicators.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- pandas
- websockets
- ccxt (for Binance API integration)
- scipy (for Dynamic Time Warping)

## Usage

1) Close the Repository
```bash
git clone https://github.com/james19190/AltCoin_ClosePrice_BivariateAnalysis.git
```

2) Navigate to the project directory:
```bash
cd crypto-analysis
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

4) Run the Program
```bash
python crypto_analysis.py
```

## Configuration
Open the config.py file and update the following parameters:

- API_KEY: Your Binance API key.
- API_SECRET: Your Binance API secret.
- SYMBOL: The crypto asset symbol to analyze (e.g., 'BTCUSDT').
- TIME_FRAME: The time frame for historical data (e.g., '1h' for 1-hour intervals).
- Add any additional configuration parameters as needed.
- Save the config.py file.

## Notes
- Ensure that you have obtained API credentials from Binance and have proper permissions.
- This program is a starting point and can be extended for more sophisticated analysis based on your requirements.
- Be cautious with API key storage and sharing. Keep them secure and avoid including them in version control.

