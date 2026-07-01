import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Stock Market Analysis",
    page_icon="📈",
    layout="wide"
)

# ── Header ───────────────────────────────────────────────────
st.markdown("""
    <div style='background-color:#3B1F33; padding:20px; border-radius:10px; margin-bottom:20px'>
        <h1 style='color:white; text-align:center'>📈 Stock Market Analysis App</h1>
        <p style='color:#D6A8C4; text-align:center'>Real-time stock data, trends and insights</p>
    </div>
""", unsafe_allow_html=True)

# ── Sidebar inputs ───────────────────────────────────────────
st.sidebar.header("⚙️ Settings")
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL").upper()
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2026-06-30"))
ma_short = st.sidebar.slider("Short MA (days)", 5, 50, 20)
ma_long = st.sidebar.slider("Long MA (days)", 20, 200, 50)

# ── Fetch data ───────────────────────────────────────────────
st.markdown("---")
if st.sidebar.button("🔍 Analyse Stock"):
    with st.spinner(f"Fetching data for {ticker}..."):
        try:
            df = yf.download(ticker, start=start_date, end=end_date)

            if df.empty:
                st.error("No data found. Please check the ticker symbol.")
            else:
                # Flatten multi-level columns if needed
                if isinstance(df.columns, pd.MultiIndex):
                    df.columns = df.columns.get_level_values(0)

                df.reset_index(inplace=True)

                # Calculate metrics
                df['MA_Short'] = df['Close'].rolling(ma_short).mean()
                df['MA_Long'] = df['Close'].rolling(ma_long).mean()
                df['Daily_Return'] = df['Close'].pct_change() * 100
                df['Volatility'] = df['Daily_Return'].rolling(20).std()

                # ── KPI row ──────────────────────────────────
                st.markdown(f"### 📊 {ticker} — Key Metrics")
                col1, col2, col3, col4, col5 = st.columns(5)
                col1.metric("Current Price", f"${df['Close'].iloc[-1]:.2f}")
                col2.metric("Avg Price", f"${df['Close'].mean():.2f}")
                col3.metric("Max Price", f"${df['Close'].max():.2f}")
                col4.metric("Avg Daily Return", f"{df['Daily_Return'].mean():.2f}%")
                col5.metric("Avg Volatility", f"{df['Volatility'].mean():.2f}%")

                # ── Price + MA chart ─────────────────────────
                st.markdown("### 📈 Price Trend with Moving Averages")
                fig, ax = plt.subplots(figsize=(12, 5))
                ax.plot(df['Date'], df['Close'], label='Close Price', alpha=0.7, color='#2E75B6')
                ax.plot(df['Date'], df['MA_Short'], label=f'MA{ma_short}', color='orange')
                ax.plot(df['Date'], df['MA_Long'], label=f'MA{ma_long}', color='red')
                ax.set_title(f"{ticker} Price with Moving Averages")
                ax.legend()
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
                plt.xticks(rotation=45)
                st.pyplot(fig)

                # ── Daily Return chart ───────────────────────
                st.markdown("### 📉 Daily Returns")
                fig2, ax2 = plt.subplots(figsize=(12, 4))
                colors = ['green' if x >= 0 else 'red' for x in df['Daily_Return'].fillna(0)]
                ax2.bar(df['Date'], df['Daily_Return'], color=colors, alpha=0.7)
                ax2.axhline(0, color='black', linewidth=0.8)
                ax2.set_title(f"{ticker} Daily Returns (%)")
                ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
                plt.xticks(rotation=45)
                st.pyplot(fig2)

                # ── Volatility chart ─────────────────────────
                st.markdown("### ⚡ Rolling Volatility")
                fig3, ax3 = plt.subplots(figsize=(12, 4))
                ax3.plot(df['Date'], df['Volatility'], color='purple', alpha=0.8)
                ax3.fill_between(df['Date'], df['Volatility'], alpha=0.3, color='purple')
                ax3.set_title(f"{ticker} Rolling 20-Day Volatility")
                ax3.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
                plt.xticks(rotation=45)
                st.pyplot(fig3)

                # ── Raw data ─────────────────────────────────
                st.markdown("### 🗃️ Raw Data")
                st.dataframe(df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Daily_Return', 'Volatility']].tail(30))

        except Exception as e:
            st.error(f"Error fetching data: {e}")
else:
    st.info("👈 Enter a stock ticker in the sidebar and click 'Analyse Stock' to get started!")