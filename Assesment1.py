import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import os

# Create output directory for graphs
output_dir = "stock_graphs"
os.makedirs(output_dir, exist_ok=True)

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
print("\n" + "="*50)
print("STOCK ANALYSIS RESULTS")
print("="*50)
print(df.to_string(index=False))
print("="*50 + "\n")

# Save to Excel
df.to_excel("assignment1_stocks.xlsx", index=False)
print(f"✓ Excel file saved: assignment1_stocks.xlsx")

# --- Create and save speedometer charts ---
print(f"\nGenerating speedometer charts...")

for i, row in df.iterrows():
    # Create speedometer figure
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=row["Overall Score"],
        title={'text': f"{row['Stock']}<br><span style='font-size:0.8em'>Overall Score</span>", 
               'font': {'size': 24}},
        delta={'reference': 50, 'increasing': {'color': "green"}, 'decreasing': {'color': "red"}},
        number={'suffix': "%", 'font': {'size': 40}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkgray"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 33], 'color': '#ffcccc'},
                {'range': [33, 66], 'color': '#ffffcc'},
                {'range': [66, 100], 'color': '#ccffcc'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': row["Overall Score"]
            }
        }
    ))
    
    # Update layout for better appearance
    fig.update_layout(
        width=600,
        height=450,
        margin=dict(l=20, r=20, t=80, b=20),
        font={'family': "Arial", 'size': 14}
    )
    
    # Save as HTML (interactive)
    html_filename = f"{output_dir}/{row['Stock'].replace(' ', '_')}_speedometer.html"
    fig.write_html(html_filename)
    
    # Save as PNG (static image) - requires kaleido package
    try:
        png_filename = f"{output_dir}/{row['Stock'].replace(' ', '_')}_speedometer.png"
        fig.write_image(png_filename)
        print(f"✓ Saved: {png_filename}")
    except Exception as e:
        print(f"⚠ PNG save failed for {row['Stock']} (install kaleido: pip install kaleido)")
        print(f"  HTML version saved: {html_filename}")
    
    # Show the figure
    fig.show()

print(f"\n✓ All graphs saved in '{output_dir}' folder")
print(f"✓ Analysis complete!")