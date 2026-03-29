import os

print("Current working directory:", os.getcwd())
print("\nFiles in current directory:")
print(os.listdir('.'))

print("\nFiles in data folder:")
if os.path.exists('data'):
    print(os.listdir('data'))
else:
    print("❌ Data folder not found!")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

print("="*60)
print("ENTERTAINMENT DATA ANALYSIS")
print("="*60)

# LOAD YOUR DOWNLOADED CSV FILE
print("\n📥 Loading data...")
df = pd.read_csv(r"C:\Users\Bhuvana\Documents\Projects\data-analysis-project\data-analysis-project\data\tmdb_5000_movies.csv")
print("✅ Data loaded successfully!")

# 1. DATA EXPLORATION
print("\n📊 Dataset Shape:", df.shape)
print("\n📋 First 5 Rows:")
print(df.head())

print("\n📈 Column Names:")
print(df.columns.tolist())

print("\n📉 Statistical Summary:")
print(df.describe())

print("\n🔍 Missing Values:")
print(df.isnull().sum())

# 2. DATA CLEANING
print("\n" + "="*60)
print("DATA CLEANING")
print("="*60)

df_clean = df.dropna(subset=['vote_average', 'runtime'])
print(f"✅ Rows after cleaning: {len(df_clean)}")

# 3. DATA ANALYSIS
print("\n" + "="*60)
print("STATISTICAL ANALYSIS")
print("="*60)

print("\n⭐ Average Rating:", df_clean['vote_average'].mean())
print("🎬 Average Runtime:", df_clean['runtime'].mean(), "minutes")
print("📈 Total Movies:", len(df_clean))

# 4. VISUALIZATIONS
print("\n📊 Creating visualizations...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Entertainment Data Analysis Dashboard', fontsize=16, fontweight='bold')

# Plot 1: Rating Distribution
axes[0, 0].hist(df_clean['vote_average'], bins=20, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribution of Movie Ratings')
axes[0, 0].set_xlabel('Rating')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].grid(alpha=0.3)

# Plot 2: Runtime Distribution
axes[0, 1].hist(df_clean['runtime'], bins=20, color='coral', edgecolor='black')
axes[0, 1].set_title('Distribution of Movie Runtime')
axes[0, 1].set_xlabel('Runtime (Minutes)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].grid(alpha=0.3)

# Plot 3: Rating vs Runtime
axes[1, 0].scatter(df_clean['runtime'], df_clean['vote_average'], alpha=0.5, color='green', s=20)
axes[1, 0].set_title('Runtime vs Rating')
axes[1, 0].set_xlabel('Runtime (Minutes)')
axes[1, 0].set_ylabel('Rating')
axes[1, 0].grid(alpha=0.3)

# Plot 4: Budget vs Revenue (if available)
if 'budget' in df_clean.columns and 'revenue' in df_clean.columns:
    df_budget = df_clean[(df_clean['budget'] > 0) & (df_clean['revenue'] > 0)]
    axes[1, 1].scatter(df_budget['budget'], df_budget['revenue'], alpha=0.5, color='purple', s=20)
    axes[1, 1].set_title('Budget vs Revenue')
    axes[1, 1].set_xlabel('Budget')
    axes[1, 1].set_ylabel('Revenue')
else:
    axes[1, 1].text(0.5, 0.5, 'Budget/Revenue data not available', 
                    ha='center', va='center', transform=axes[1, 1].transAxes)
    axes[1, 1].set_title('Budget vs Revenue')

axes[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('analysis_dashboard.png', dpi=300, bbox_inches='tight')
print("✅ Dashboard saved as 'analysis_dashboard.png'")
plt.show()

print("\n✅ Analysis Complete!")