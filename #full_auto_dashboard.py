
import pyodbc
import requests
import time
from datetime import datetime

# ==========================================
# CONFIGURATION
# ==========================================
# 1. CHANGE THIS to your computer name! 
# (Search "View your PC name" in Windows settings if you don't know it)
SERVER_NAME = 'RASAD_123/MSSQLSERVER' 

DATABASE_NAME = 'RealWorldCryptoDB'

# ==========================================
# PART A: SETUP DATABASE AND TABLE (SQL IN PYTHON)
# ==========================================

def setup_infrastructure():
    print("--- Setting up Database Infrastructure ---")
    
    # Connect to the 'master' database to create a new DB
    # We use autocommit=True because you cannot create a DB inside a transaction
    conn_str_master = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER_NAME};DATABASE=master;Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_str_master, autocommit=True)
    cursor = conn.cursor()

    # 1. SQL COMMAND: Create Database if it doesn't exist
    # This is where we write SQL directly inside Python
    sql_create_db = f"""
    IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '{DATABASE_NAME}')
    BEGIN
        CREATE DATABASE {DATABASE_NAME};
    END
    """
    cursor.execute(sql_create_db)
    print(f"Database '{DATABASE_NAME}' checked/created.")
    conn.close()

    # 2. Connect to the NEW Database
    conn_str_db = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_str_db)
    cursor = conn.cursor()

    # 3. SQL COMMAND: Create Table
    sql_create_table = """
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='CryptoLive' AND xtype='U')
    BEGIN
        CREATE TABLE CryptoLive (
            ID INT IDENTITY(1,1) PRIMARY KEY,
            CryptoName VARCHAR(50),
            PriceUSD DECIMAL(18, 2),
            CaptureTime DATETIME DEFAULT GETDATE()
        )
    END
    """
    cursor.execute(sql_create_table)
    conn.commit() # Save changes
    print("Table 'CryptoLive' checked/created.")
    conn.close()

# ==========================================
# PART B: THE LIVE DATA LOOP
# ==========================================

def fetch_and_insert():
    # Connect to our database
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    try:
        # 1. Get Data from Web (API)
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        current_price = data['bitcoin']['usd']
        
        # 2. SQL COMMAND: Insert Data
        # We use '?' as placeholders for the data variables
        sql_insert = "INSERT INTO CryptoLive (CryptoName, PriceUSD, CaptureTime) VALUES (?, ?, ?)"
        
        # Execute the SQL with Python variables
        cursor.execute(sql_insert, ('Bitcoin', current_price, datetime.now()))
        
        # 3. Commit (Save) the data
        conn.commit()
        print(f"Data Saved! Bitcoin: ${current_price} at {datetime.now().strftime('%H:%M:%S')}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.close()

# ==========================================
# PART C: EXECUTION
# ==========================================

# Run setup once at the start
setup_infrastructure()

print("--- Starting Live Data Feed (Ctrl+C to stop) ---")
while True:
    fetch_and_insert()
    # Wait for 60 seconds before next update
    time.sleep(60)