Spend$mart - A Single Time Finance App
Spend$mart is a full finance application that provides stock price predictions, information about specific stock tokens, the latest news related to finance, and an interactive interface for users to explore various financial data. This app uses advanced data sources, APIs, and machine learning models to provide reliable predictions and financial insights.

Features
Stock Price Prediction: Predicts future stock prices using the Prophet machine learning model. A user can input any stock token, choose a date range for historical data, and specify a future prediction date.

Stock Token Information: Detailed information about a specific stock token including industry, sector, CEO, market capitalization, total revenue, and link to the official website.

Latest News: It fetches the latest news related to finance based on keywords using the News API. Users can input any keyword, such as Bitcoin or the stock market, to get the most recent articles.

Contact Us: A form where users can send a message to the app's creators via email.

Tech Stack
Frontend: Streamlit
Backend: Python
Data Source: Yahoo Finance API, News API
Prediction Model: Prophet (for stock price prediction)
Visualization: Plotly (for interactive graphs)
Setup and Installation
To set up the application locally, do the following:

Step 1: Clone the repository

bash
Copy code
git clone <repository_url>
cd Spend$mart
Step 2: Create a virtual environment (Optional but recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
Step 3: Install the required dependencies

bash
Copy code
pip install -r requirements.txt
Step 4: Run the app

bash
Copy code
streamlit run app.py
Step 5: Open your browser and go to:
arduino
Copy code
http://localhost:8501
Now, the app should be up and running.

File Structure

bash
Copy code
Spend$mart/
│
├── app.py # Main Streamlit application code
├── requirements.txt # List of required packages
└── .gitignore # Git ignore file for the project
