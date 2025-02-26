# Spend$mart - A One-Stop Finance App

## Overview

Spend$mart is a finance app built using **Streamlit**, designed to provide a seamless experience for users to:

- **Predict Future Stock Prices** using the power of machine learning (Prophet).
- Get detailed **Information about Stocks** (including company profiles, revenue, market capitalization, etc.).
- Stay updated with the latest **Finance News** from the most reliable sources.
- View **Stock Market Trends and Analysis** for various stocks.

With Spend$mart, users can make smarter financial decisions with up-to-date data and forecasts.

---

## Features

1. **Prediction**
    - Users can enter a stock symbol (e.g., AAPL) and specify a date range to view historical stock prices.
    - The app uses **Prophet** to predict future stock prices, allowing users to forecast the trend for a given period.

2. **Market Information**
    - Get detailed information about individual stocks such as:
      - Company Name
      - Industry
      - CEO
      - Revenue
      - Market Capitalization
      - Website link for more information
    - Users can view stock price graphs over a year-long period.

3. **News**
    - Provides the latest finance-related news using the **News API**.
    - Users can search for news by entering a specific keyword (e.g., "bitcoin").
    - Displays relevant articles with publication date, description, and image (if available).

4. **Contact Us**
    - A contact form to directly reach out for inquiries or feedback.
    - Captures the user's name, email, and message.

---

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Jnan-py/spendsmart.git
    cd spendsmart
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:

    ```bash
    streamlit run spendsmart.py
    ```

---

## Technologies Used

- **Streamlit**: For building the user interface.
- **yFinance**: To fetch stock data.
- **Prophet**: For stock price prediction.
- **Plotly**: For data visualization and stock price graph plotting.
- **NewsAPI**: To fetch real-time finance news.
- **Pandas**: For data manipulation and handling.

