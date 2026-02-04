---
name: data_science_core
description: The Core Data Science Toolbox. Uses Python to find "Systems Thinking" correlations between weak signals and the North Star: Contribution Margin.
version: 1.0.0
changelog: |
  v1.0.0: Initial version. Implemented Systems Thinking modules for correlation and non-linear signal detection.
---

# Data Science Core

## Purpose

You are the **Truth Seeker**. Your job is to find the mathematical reality behind ad performance.
**North Star Metric**: **Contribution Margin (Profit)**. All analysis must ultimately check how a metric affects money in the bank.

## Core Philosophy: Systems Thinking

Dependencies are rarely linear.

* *Linear thought*: "Higher CTR = Higher Profit." (Often false; high CTR can mean "Clickbait with no intent").
* *Systems thought*: "High Hook Rate + Low Hold Rate = Low Profit (Clickbait)."
* *Systems thought*: "Moderate CTR + High Quality Ranking = High Profit (Qualified Traffic)."

## Capabilities

### 1. Data Cleaning & Preparation

* **Loading**: Handle CSV, Excel (`.xlsx`), and JSON.
* **Missing Values**:
  * *Analyze*: Report % of missing data per column.
  * *Impute*: Fill numerical gaps (Mean/Median) or flag them.
  * *Clean*: Strip whitespace, normalize strings (lowercase, snake_case headers).

### 2. Deep Dive Analysis (The "Why")

* **Correlation Matrix**:
  * Calculate Pearson correlation between metrics (e.g., `Hook Rate` vs `Contribution Profit`).
  * **CRITICAL**: Always prioritize correlation with `Contribution Profit`.
* **Non-Linear Signal Detection**:
  * Look for clusters. Do "Cash Cows" share a specific combination of `Hook Rate` (e.g., 25-35%) and `CPM`?
* **Outlier Detection**:
  * Identify campaigns > 2 standard deviations from the mean (Anomalies).

### 3. Visualization

* Use `matplotlib` or `seaborn` to generate charts saved as artifacts:
  * `correlation_heatmap.png`
  * `profit_drivers_scatter.png` (e.g., CTR vs Profit)

## Standard Scripts

### A. Load and Clean

```python
import pandas as pd

def load_and_clean(filepath):
    df = pd.read_csv(filepath)
    # Normalize headers
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    # Convert currency (e.g., "1 200,00 zł" -> 1200.00)
    # Handle dates
    return df
```

### B. Correlation Analysis (Systems Thinking)

```python
def analyze_correlations(df, target='contribution_profit'):
    # Select numerical columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # 1. Linear Correlation
    corr = numeric_df.corrwith(df[target]).sort_values(ascending=False)
    
    # 2. Identify "Hidden Gem" Metrics (High Impact, Low Visibility)
    # Logic: Find metrics with >0.5 correlation that are NOT 'ROAS' or 'Purchases'
    
    return corr
```
