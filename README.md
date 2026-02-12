# Trader Performance vs. Market Sentiment Analysis
**Round-0 Assignment | Primetrade.ai**

## 📌 Project Overview
This repository contains a data-driven analysis of how Bitcoin market sentiment (Fear & Greed Index) influences trader behavior and profitability on the Hyperliquid platform. 

The objective of this study was to uncover patterns in position sizing, win rates, and emotional bias to inform actionable trading strategies.

## 📊 Key Insights & Findings
After cleaning and merging the datasets on a daily level, the following insights were identified:

1. **Emotional Position Sizing:** Traders exhibit a strong emotional bias toward "Greed." The average trade size during **Extreme Greed** is **$5,660**, which is approximately **85% higher** than the average trade size during **Neutral** periods ($3,058).
2. **The "Neutral" Performance Gap:** The analysis revealed that **Neutral** market sentiment is the most difficult for traders to navigate, yielding the lowest win rate of **31.8%**. 
3. **Sentiment-Correlation to Success:** Profitability (Win Rate) actually peaks during **Extreme Greed (~49.0%)** and **Greed (~44.6%)**. This suggests that the current cohort of traders finds more success in high-momentum, trend-driven environments than in sideways/neutral markets.

## 💡 Actionable "Rules of Thumb" (Part C)
* **The Neutral Filter:** Data shows a significant drop in success during Neutral days. Traders should reduce their trade frequency by at least 50% when the Fear & Greed index is between 45-55 to preserve capital.
* **Momentum Sizing:** Since win rates are higher during Greed phases, traders can maintain standard sizing there but should implement a "Volatility Cap" during Extreme Greed to protect against the high-impact reversals that often follow sentiment peaks.

## 🛠️ Technical Setup & Execution

### Data Access
Due to the large file size (>25MB), the `historical_data.csv` isn't added here:
* **Download Trader Dataset first**
* Place the downloaded file in the root folder before running the script.

### Requirements
This project requires Python 3.x and the following libraries:
```bash
pip install pandas matplotlib seaborn
