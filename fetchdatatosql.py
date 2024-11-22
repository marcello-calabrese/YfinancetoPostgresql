
## Fetching data from Yfinance and storing it in SQL database
# This script will fetch data from Yfinance and store it in a SQL database.
import yfinance as yf

import psycopg2 as pg
from db_config import CONNECTION_STRING

# Shares symbols List of stock symbols to track
STOCKS = ["IMEU.L", "MSFT", "IAAA.L", "SGLN.L", "VHYD.L"]


def fetch_data_to_postgresql():
    # Connect to PostgreSQL
    conn = pg.connect(CONNECTION_STRING)
    cursor = conn.cursor()
    for symbol in STOCKS:
        print(f"Fetching data for {symbol}...")
        
        # Fetch historical data (last 5 years)
        stock = yf.Ticker(symbol)
        hist = stock.history(period="5y")
        
        # Iterate through rows and insert/update the database
        for date, row in hist.iterrows():
            cursor.execute(
                """
                INSERT INTO stock_prices_actions (stock_symbol, date, close_price, volume)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (stock_symbol, date) DO UPDATE
                SET close_price = EXCLUDED.close_price,
                    volume = EXCLUDED.volume;
                """,
                (symbol, date.date(), float(row['Close']), int(row['Volume'])))
            conn.commit()
    
    # Commit changes and close the connection
    conn.commit() # commit the transaction
    cursor.close() # close the cursor
    conn.close()
    print("Data updated successfully.")
    

if __name__ == "__main__":
    fetch_data_to_postgresql()
        






