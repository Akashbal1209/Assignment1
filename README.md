# Stock Analysis Tool

A Python-based tool for analyzing NSE (National Stock Exchange) stocks with visual speedometer charts showing stock performance scores.

## 📋 Overview

This tool fetches stock data from Yahoo Finance and calculates performance scores based on:
- 52-week high/low analysis
- 3-month high/low analysis
- 1-month high/low analysis
- Overall composite score

Results are exported to Excel and visualized using interactive speedometer charts.

## 🎯 Features

- ✅ Real-time stock data fetching from NSE
- ✅ Multi-timeframe analysis (52W, 3M, 1M)
- ✅ Performance scoring (0-100 scale)
- ✅ Excel export with detailed metrics
- ✅ Interactive speedometer visualizations
- ✅ Automatic graph saving (HTML & PNG formats)
- ✅ Color-coded performance zones (Red/Yellow/Green)

## 📦 Requirements

### Required Packages
```bash
pip install yfinance pandas plotly openpyxl
```

### Optional (for PNG image export)
```bash
pip install kaleido
```

## 🚀 Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install yfinance pandas plotly openpyxl kaleido
   ```
3. **Run the script**:
   ```bash
   python stock_analysis.py
   ```

## 📊 Default Stocks Analyzed

The tool analyzes these NSE stocks by default:
- **Idea** (IDEA.NS)
- **Adani Industries** (ADANIENT.NS)
- **Reliance Industries** (RELIANCE.NS)
- **Bajaj Auto** (BAJAJ-AUTO.NS)

## 🔧 How to Customize

### Adding More Stocks

Edit the `stocks` dictionary in the script:

```python
stocks = {
    "Your Stock Name": "TICKER.NS",
    "Tata Motors": "TATAMOTORS.NS",
    "HDFC Bank": "HDFCBANK.NS",
    # Add more stocks here
}
```

### Changing Analysis Period

Modify the period parameter:
```python
data = yf.Ticker(ticker).history(period="1y")  # Change to "2y", "6mo", etc.
```

## 📁 Output Files

After running the script, you'll get:

### 1. Excel File
**`assignment1_stocks.xlsx`**
- Current prices
- 52-week, 3-month, 1-month highs/lows
- Performance scores for each timeframe
- Overall composite score

### 2. Graph Files (in `stock_graphs/` folder)
- **HTML files** - Interactive speedometer charts
  - `Idea_speedometer.html`
  - `Adani_Industries_speedometer.html`
  - etc.
- **PNG files** - Static image exports (requires kaleido)
  - `Idea_speedometer.png`
  - `Adani_Industries_speedometer.png`
  - etc.

## 📈 Understanding the Scores

### Score Calculation
```
Score = ((Current Price - Period Low) / (Period High - Period Low)) × 100
```

### Score Interpretation
- **0-33** (Red Zone): Stock near its low for the period
- **34-66** (Yellow Zone): Stock in mid-range
- **67-100** (Green Zone): Stock near its high for the period

### Overall Score
Average of 52-week, 3-month, and 1-month scores

## 💡 Usage Examples

### Basic Usage
```bash
python Assesment1.py
```

### View Output
1. Check console for summary table
2. Open `assignment1_stocks.xlsx` for detailed data
3. View graphs in `stock_graphs/` folder
4. Open HTML files in browser for interactive charts

## 🐛 Troubleshooting

### Common Issues

**1. No data for stock**
- Verify ticker symbol is correct for NSE (should end with .NS)
- Check internet connection
- Stock might be delisted or suspended

**2. PNG files not generated**
- Install kaleido: `pip install kaleido`
- HTML files will still be created

**3. Module not found errors**
```bash
pip install --upgrade yfinance pandas plotly openpyxl
```

**4. Rate limiting**
- Yahoo Finance may limit requests
- Add delays between stocks if needed:
  ```python
  import time
  time.sleep(1)  # Add after each stock fetch
  ```

## 📝 Sample Output

### Console Output
```
==================================================
STOCK ANALYSIS RESULTS
==================================================
Stock               Current Price  52W Score  3M Score  1M Score  Overall Score
Idea                12.45         45.23      52.10     48.67     48.67
Reliance Industries 2456.30       72.45      68.90     75.20     72.18
...
==================================================

✓ Excel file saved: assignment1_stocks.xlsx
✓ Saved: stock_graphs/Idea_speedometer.png
✓ All graphs saved in 'stock_graphs' folder
✓ Analysis complete!
```

## 🔄 Update Frequency

- Stock data is fetched in real-time when script runs
- For automated updates, consider scheduling with:
  - **Windows**: Task Scheduler
  - **Linux/Mac**: Cron jobs
  - **Python**: Schedule library

## 📄 License

Free to use and modify for personal and commercial purposes.

## 🤝 Contributing

Feel free to:
- Add more technical indicators
- Improve visualization styles
- Add email alerts for score thresholds
- Create dashboard versions

## 📧 Support

For issues or questions:
1. Check troubleshooting section
2. Verify all dependencies are installed
3. Ensure internet connection is stable

## 🔮 Future Enhancements

Potential features to add:
- [ ] Multiple chart types (candlestick, line charts)
- [ ] Email notifications for price alerts
- [ ] Historical trend analysis
- [ ] Comparison with market indices
- [ ] Moving average calculations
- [ ] Volume analysis
- [ ] Web dashboard interface

---

**Last Updated**: November 2025  
**Version**: 1.0  
**Python Version**: 3.7+