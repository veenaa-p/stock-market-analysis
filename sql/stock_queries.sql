USE stock_project;

-- 1. Average closing price per ticker
SELECT Ticker, ROUND(AVG(Close), 2) AS avg_close
FROM stock_prices
GROUP BY Ticker
ORDER BY avg_close DESC;

-- 2. Highest single-day gain per ticker
SELECT Ticker, Date, Daily_Return
FROM stock_prices
WHERE Daily_Return = (
    SELECT MAX(Daily_Return) FROM stock_prices AS sp2 WHERE sp2.Ticker = stock_prices.Ticker
);

-- 3. Average volatility per ticker
SELECT Ticker, ROUND(AVG(Volatility), 2) AS avg_volatility
FROM stock_prices
GROUP BY Ticker
ORDER BY avg_volatility DESC;

-- 4. Monthly average closing price trend
SELECT Ticker, DATE_FORMAT(Date, '%Y-%m') AS month, ROUND(AVG(Close), 2) AS avg_close
FROM stock_prices
GROUP BY Ticker, month
ORDER BY Ticker, month;

-- 5. Days where price was above both moving averages (bullish signal)
SELECT Ticker, COUNT(*) AS bullish_days
FROM stock_prices
WHERE Close > MA20 AND Close > MA50
GROUP BY Ticker;