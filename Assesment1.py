import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# NSE tickers
stocks = {
    "Idea": "IDEA.NS",
    "Adani Industries": "ADANIENT.NS",
    "Reliance Industries": "RELIANCE.NS",
    "Bajaj Auto": "BAJAJ-AUTO.NS"
}

results = []

for name, ticker in stocks.items():
    try:
        # Fetch 1 year of data
        data = yf.Ticker(ticker).history(period="1y")

        if data.empty:
            print(f"No data for {name}")
            continue

        # Current price
        current = data["Close"].iloc[-1]

        # --- 52-week period ---
        high_52w = data["High"].max()
        low_52w = data["Low"].min()
        score_52w = ((current - low_52w) / (high_52w - low_52w)) * 100

        # --- 3-month period ---
        data_3m = data.last("3M")
        high_3m = data_3m["High"].max()
        low_3m = data_3m["Low"].min()
        score_3m = ((current - low_3m) / (high_3m - low_3m)) * 100

        # --- 1-month period ---
        data_1m = data.last("1M")
        high_1m = data_1m["High"].max()
        low_1m = data_1m["Low"].min()
        score_1m = ((current - low_1m) / (high_1m - low_1m)) * 100

        # --- Overall score (average) ---
        overall = (score_52w + score_3m + score_1m) / 3

        # Save results
        results.append({
            "Stock": name,
            "Current Price": round(current, 2),

            "52W High": round(high_52w, 2),
            "52W Low": round(low_52w, 2),
            "52W Score": round(score_52w, 2),

            "3M High": round(high_3m, 2),
            "3M Low": round(low_3m, 2),
            "3M Score": round(score_3m, 2),

            "1M High": round(high_1m, 2),
            "1M Low": round(low_1m, 2),
            "1M Score": round(score_1m, 2),

            "Overall Score": round(overall, 2)
        })

    except Exception as e:
        print(f"Error fetching {name}: {e}")

# Convert to DataFrame
df = pd.DataFrame(results)
print(df)

# Save to Excel
df.to_excel("assignment1_stocks.xlsx", index=False)

# --- Speedometer charts ---
for i, row in df.iterrows():
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=row["Overall Score"],
        title={'text': row["Stock"]},
        gauge={'axis': {'range': [0,100]}}
    ))
    fig.show()