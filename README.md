📊 Real-Time Crypto Price Monitoring & Analytics Engine
🚀 Project Overview

The Real-Time Crypto Price Monitoring & Analytics Engine is a data analytics project that fetches live cryptocurrency prices every 60 seconds and performs real-time analysis using Python and SQL. The system tracks major cryptocurrencies like Bitcoin and Ethereum, stores historical and live data, and enables trend analysis, price monitoring, and market insights.

This project demonstrates practical skills in API integration, real-time data ingestion, database management, and data analytics, making it suitable for Data Analyst and Data Engineering roles.

🎯 Key Features

🔄 Fetches live crypto price data every 60 seconds

📈 Tracks Bitcoin and Ethereum prices

🐍 Automated data collection using Python

🗄️ Stores real-time & historical data in SQL database

📊 Performs price trend analysis and percentage change calculations

⚡ Efficient querying for analytical insights

🔧 Scalable architecture to add more cryptocurrencies

🛠️ Technologies Used

Programming Language: Python

Database: SQL (MySQL / PostgreSQL / SQLite)

APIs: Cryptocurrency Market APIs

Libraries:

requests – API data fetching

pandas – Data processing and analysis

sqlalchemy / mysql-connector – Database connectivity

Tools: VS Code, GitHub

🧠 How It Works

Python script connects to a cryptocurrency API.

Live price data is fetched every 60 seconds.

Data is cleaned and processed.

Processed data is stored in a SQL database.

SQL queries are used to analyze trends and price movements.

Results can be extended to dashboards or reports.

📂 Project Structure
├── data_fetch.py        # Fetches live crypto data
├── database.sql         # SQL table schema
├── data_analysis.py     # Data processing and analytics
├── requirements.txt    # Required Python libraries
├── README.md            # Project documentation

▶️ How to Run the Project

Clone the repository:

git clone https://github.com/your-username/your-repository-name.git


Install required libraries:

pip install -r requirements.txt


Configure database credentials in the Python script.

Run the data fetching script:

python data_fetch.py


Query the SQL database to analyze crypto trends.

📌 Use Cases

Real-time cryptocurrency price tracking

Market trend analysis

Data analytics portfolio project

Foundation for dashboards and forecasting models

🌱 Future Enhancements

Add more cryptocurrencies

Integrate Power BI / Tableau dashboards

Implement price prediction using Machine Learning

Cloud deployment for continuous monitoring
