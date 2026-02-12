# Executive Summary: Trader Performance vs. Market Sentiment

## 1. Methodology
To analyze the relationship between market sentiment and trading performance, I performed the following steps:
* **Data Cleaning:** Converted Unix timestamps in the trader dataset to normalized UTC dates to match the daily resolution of the Fear & Greed Index.
* **Data Integration:** Merged the two datasets on the 'date' column using a left-join to ensure every trade was categorized by a sentiment classification (Fear, Greed, Neutral, etc.).
* **Metric Calculation:** Developed logic to calculate Win Rate (Total Wins / Total Trades), Average Position Size (USD), and Average Leverage.

## 2. Key Data Insights
* **The "Greed" Surge:** Traders show a clear emotional response to bullish sentiment. The average trade size during **Extreme Greed ($5,660)** is nearly double that of **Neutral ($3,058)** days.
* **Profitability Paradox:** While traders are most aggressive during Extreme Greed, their Win Rate is also at its peak (~49%). Conversely, **Neutral sentiment** proved to be the "danger zone," yielding the lowest win rate of **31.8%**.
* **Segment Behavior:** High-leverage traders (segmentation) were found to be more active during extreme sentiment shifts, indicating that sentiment is a primary driver for risk-taking behavior in this cohort.

## 3. Strategy Recommendations
Based on these findings, I propose the following "Rules of Thumb" for trading operations:

### Rule 1: The Neutral Sentiment Filter
Traders should reduce their trade frequency or switch to a "wait-and-see" approach when the index is Neutral (45-55). The data suggests that without a clear sentiment driver, the probability of a winning trade drops by nearly 17% compared to Greed phases.

### Rule 2: Dynamic Sizing Cap
Implement an automated cap on position sizes when the Fear & Greed Index exceeds 75. While win rates are currently high in this zone, the massive increase in trade size suggests "herd behavior," which often precedes a sharp market reversal (liquidation cascade).

---
**Analysis performed by:** [Vipin Nishad]
**Tools used:** Python (Pandas, Matplotlib, Seaborn)
