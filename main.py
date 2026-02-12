import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# PART A: DATA PREPARATION
# ==========================================

# 1. Load the files
sentiment_df = pd.read_csv('fear_greed_index.csv')
trader_df = pd.read_csv('historical_data.csv')

# Documentation: Rows/Columns and Missing Values
print("--- Data Documentation ---")
print(f"Sentiment Data: {sentiment_df.shape[0]} rows, {sentiment_df.shape[1]} columns")
print(f"Trader Data: {trader_df.shape[0]} rows, {trader_df.shape[1]} columns")
print(f"Missing Values in Trader Data:\n{trader_df.isnull().sum()}\n")

# 2. Convert Timestamps and Align (Normalization)
sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])
trader_df['date'] = pd.to_datetime(trader_df['Timestamp'], unit='ms').dt.normalize()

# 3. Merge Datasets
merged_df = pd.merge(trader_df, sentiment_df, on='date', how='left')
print(f"Successfully merged. Total records: {len(merged_df)}\n")

# ==========================================
# PART B: ANALYSIS & INSIGHTS
# ==========================================

# Insight 1: Average Trade Size by Sentiment
size_insight = merged_df.groupby('classification')['Size USD'].mean()

# Insight 2: Average Leverage by Sentiment
# Note: Ensure 'leverage' column exists in your historical_data.csv
if 'leverage' in merged_df.columns:
    lev_insight = merged_df.groupby('classification')['leverage'].mean()
else:
    lev_insight = None

# Insight 3: Win Rate (%) by Sentiment
merged_df['is_win'] = merged_df['Closed PnL'] > 0
win_rate_insight = merged_df.groupby('classification')['is_win'].mean() * 100

print("--- Data Insights ---")
print("Avg Trade Size:\n", size_insight)
print("\nWin Rate (%):\n", win_rate_insight)

# ==========================================
# PART B: VISUALIZATIONS
# ==========================================

# Set style for charts
sns.set_theme(style="whitegrid")

# Chart 1: Average Trade Size
plt.figure(figsize=(10, 5))
size_insight.sort_values().plot(kind='barh', color='teal')
plt.title('Avg Trade Size (USD) by Market Sentiment')
plt.xlabel('Size in USD')
plt.tight_layout()
plt.savefig('trade_size_chart.png')
print("\nSaved: trade_size_chart.png")

# Chart 2: Win Rate
plt.figure(figsize=(10, 5))
win_rate_insight.sort_values().plot(kind='bar', color='coral')
plt.title('Win Rate % by Market Sentiment')
plt.ylabel('Win Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('win_rate_chart.png')
print("Saved: win_rate_chart.png")

# ==========================================
# PART C: SEGMENTATION (Bonus Strategy Logic)
# ==========================================

# Segmenting High vs Low Leverage traders
if 'leverage' in merged_df.columns:
    merged_df['leverage_group'] = merged_df['leverage'].apply(lambda x: 'High Leverage' if x > 10 else 'Low Leverage')
    segment_performance = merged_df.groupby(['leverage_group', 'classification'])['Closed PnL'].mean()
    print("\n--- Segment Analysis (Leverage) ---")
    print(segment_performance.head(10))

print("\nAssignment complete.")

plt.show()


# --- BONUS: Clustering Traders into Archetypes ---
def categorize_trader(row):
    # We use Size USD and is_win since leverage is missing
    if row['Size USD'] > 5000 and row['is_win'] == True:
        return 'Profitable Whale'
    elif row['Size USD'] > 5000 and row['is_win'] == False:
        return 'High-Risk Speculator'
    elif row['Size USD'] < 1000 and row['is_win'] == True:
        return 'Consistent Small Trader'
    else:
        return 'Retail Participant'

# Apply the categorization
merged_df['archetype'] = merged_df.apply(categorize_trader, axis=1)

# Analyze archetype distribution
archetype_counts = merged_df['archetype'].value_counts()
print("\n--- Bonus: Trader Archetype Distribution ---")
print(archetype_counts)

# Save the Bonus Chart
plt.figure(figsize=(10, 6))
archetype_counts.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Distribution of Trader Archetypes')
plt.ylabel('')  # Hides the vertical label for a cleaner look
plt.tight_layout()
plt.savefig('trader_archetypes.png')

print("\nBonus Chart saved: trader_archetypes.png")
plt.show()
