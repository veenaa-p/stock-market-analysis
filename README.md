# 📈 Stock Market Analysis Dashboard

An end-to-end data analytics project analyzing real-time stock market trends, 
financial metrics, and investment signals for AAPL, MSFT, and GOOGL using 
Python, SQL, Power BI, and Streamlit.

## 🔗 Live App
[👉 Click here to view the live Streamlit app]((https://veenaa-stock-analysis.streamlit.app/)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Data fetching, cleaning, EDA, metrics |
| yfinance API | Real-time stock data from Yahoo Finance |
| Pandas & NumPy | Data manipulation and calculations |
| Matplotlib & Seaborn | Data visualizations |
| MySQL | Data storage and SQL analysis |
| Power BI | Interactive 2-page business dashboard |
| Streamlit | Live deployable web application |

---

## 📁 Project Structure

```
stock_project/
│
├── app/
│   └── app.py                     ← Streamlit web app
│
├── data/
│   ├── raw/
│   │   └── stock_data_raw.csv     ← Original API data
│   └── cleaned/
│       └── stock_data_cleaned.csv ← Processed data
│
├── notebooks/
│   └── analysis.ipynb             ← Python EDA & metrics
│
├── powerbi/
│   └── stock_dashboard.pbix       ← Power BI dashboard
│
├── sql/
│   └── stock_queries.sql          ← SQL analysis queries
│
└── README.md
```

---

## 📊 Project Workflow

```
Yahoo Finance API (yfinance)
        ↓
Python — fetch, clean, calculate metrics
        ↓
MySQL — store & query with SQL
        ↓
Power BI — 2-page interactive dashboard
        ↓
Streamlit — live deployable web app
```

---

## 🔍 Key Features

### Python Analysis
- Fetched 3+ years of daily stock data for AAPL, MSFT, and GOOGL
- Calculated key financial metrics:
  - Daily Returns (%)
  - 20-day and 50-day Moving Averages
  - Rolling 20-day Volatility
- Visualized price trends, volatility, and return distributions

### SQL Analysis (MySQL)
- Stored 2622 rows of processed stock data
- Wrote 5 analytical queries:
  1. Average closing price per ticker
  2. Highest single-day gain per ticker
  3. Average volatility per ticker
  4. Monthly average closing price trend
  5. Bullish signal days (price above both MAs)

### Power BI Dashboard (2 pages)
**Page 1 — Overview:**
- 6 KPI cards (Avg Close, Max Close, Min Close, Avg Return, Avg Volatility, Tickers Tracked)
- Stock price trend comparison (line chart)
- Volatility by ticker (donut chart)
- Average daily return by ticker (bar chart)
- Rolling volatility over time (line chart)

**Page 2 — Deep Dive:**
- Price with Moving Averages (MA20 + MA50)
- Bullish days by ticker (bar chart)
- Monthly average close price (matrix table)
- Daily return distribution (histogram)
- Bookmark navigation between pages

### Streamlit App
- Enter any stock ticker (not just AAPL/MSFT/GOOGL)
- Select custom date range
- Adjust MA windows using sliders
- Real-time KPI metrics
- Price trend with moving averages chart
- Daily returns bar chart (green/red)
- Rolling volatility area chart
- Raw data table (last 30 days)

---

## 📈 Key Insights

- **MSFT** had the highest average closing price ($396.22) with the lowest volatility (1.46) — most stable stock
- **GOOGL** had the highest average daily return (0.18%) but also highest volatility (1.83) — highest risk/reward
- **AAPL** had the single biggest one-day gain (+15.3% on 2025-04-09)
- **GOOGL** spent the most days in bullish territory (503 days above both MAs)

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/veenaa-p/stock-market-analysis.git
cd stock-market-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
cd app
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
yfinance
matplotlib
sqlalchemy
pymysql
```

---

## 👩‍💻 Author

**Veena P**
- 📧 veenapullaikodi04@gmail.com
- 📍 Kasaragod, Kerala
- 🔗 [GitHub](https://github.com/veenaa-p)
