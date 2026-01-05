# data_collector.py

import requests
import sqlite3
import time
import datetime

# 1. API Endpoint (Bitcoin price in USD)
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
DB_NAME = "crypto_data.db"
TABLE_NAME = "bitcoin_price"

def get_crypto_price():
    """Fetches the current Bitcoin price from CoinGecko API."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        
        # Extract price and ensure it's a float
        price = data['bitcoin']['usd']
        
        # Get the current timestamp (in a readable format)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{timestamp}] Fetched BTC Price: ${price}")
        return timestamp, price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None, None

def store_data(timestamp, price):
    """Stores the timestamp and price in the SQLite database."""
    conn = None
    try:
        # Connect to the SQLite database file
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                timestamp TEXT PRIMARY KEY,
                price REAL
            )
        """)
        
        # Insert the new data point
        cursor.execute(f"INSERT OR IGNORE INTO {TABLE_NAME} VALUES (?, ?)", (timestamp, price))
        
        conn.commit()
        print(f"Data stored in {DB_NAME}")
        
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

def main_collector(interval_seconds=60):
    """Main loop to collect and store data."""
    print("Starting Bitcoin price collector. Press Ctrl+C to stop.")
    while True:
        timestamp, price = get_crypto_price()
        
        if timestamp and price is not None:
            store_data(timestamp, price)
        
        # Wait for the specified interval before the next fetch
        time.sleep(interval_seconds)

if __name__ == "__main__":
    # Fetch data every 60 seconds (1 minute)
    # Be aware of the API's rate limits
    main_collector(interval_seconds=60)