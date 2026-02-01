"""
Fake News Clean - A script to clean and preprocess the FakeNewsNet dataset.
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_script_dir():
    """Get the directory where the script is located."""
    return os.path.dirname(os.path.abspath(__file__))


def load_data(filepath: str) -> pd.DataFrame:
    """Load the FakeNewsNet dataset from a CSV file."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records from {filepath}")
    print(f"Columns: {list(df.columns)}")
    return df


def explore_data(df: pd.DataFrame) -> None:
    """Explore the dataset and print summary statistics."""
    print("\n--- Dataset Summary ---")
    print(f"Shape: {df.shape}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    print(f"\nLabel distribution (real=1, fake=0):\n{df['real'].value_counts()}")
    print(f"\nSource domain distribution (top 10):\n{df['source_domain'].value_counts().head(10)}")


def plot_data(df: pd.DataFrame, output_dir: str) -> None:
    """Create visualizations for the dataset."""
    print("\n--- Generating Plots ---")
    
    # Set style
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Fake News Dataset Analysis', fontsize=16, fontweight='bold')
    
    # 1. Label Distribution (Pie Chart)
    ax1 = axes[0, 0]
    label_counts = df['real'].value_counts()
    colors = ['#ff6b6b', '#4ecdc4']
    labels = ['Fake (0)', 'Real (1)']
    ax1.pie(label_counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax1.set_title('Label Distribution', fontsize=12, fontweight='bold')
    
    # 2. Label Distribution (Bar Chart)
    ax2 = axes[0, 1]
    label_counts.plot(kind='bar', ax=ax2, color=colors, edgecolor='black')
    ax2.set_title('Real vs Fake News Count', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Label (0=Fake, 1=Real)')
    ax2.set_ylabel('Count')
    ax2.set_xticklabels(['Fake', 'Real'], rotation=0)
    for i, v in enumerate(label_counts):
        ax2.text(i, v + 200, str(v), ha='center', fontweight='bold')
    
    # 3. Top 10 Source Domains
    ax3 = axes[1, 0]
    top_sources = df['source_domain'].value_counts().head(10)
    top_sources.plot(kind='barh', ax=ax3, color='#6c5ce7', edgecolor='black')
    ax3.set_title('Top 10 News Sources', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Article Count')
    ax3.invert_yaxis()
    
    # 4. Tweet Count Distribution by Label
    ax4 = axes[1, 1]
    df[df['real'] == 0]['tweet_num'].hist(alpha=0.7, label='Fake', color='#ff6b6b', 
                                           bins=30, edgecolor='black', ax=ax4)
    df[df['real'] == 1]['tweet_num'].hist(alpha=0.7, label='Real', color='#4ecdc4', 
                                           bins=30, edgecolor='black', ax=ax4)
    ax4.set_title('Tweet Count Distribution', fontsize=12, fontweight='bold')
    ax4.set_xlabel('Number of Tweets')
    ax4.set_ylabel('Frequency')
    ax4.legend()
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plot_path = os.path.join(output_dir, 'fake_news_analysis.png')
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    print(f"Saved plot to {plot_path}")
    plt.close()
    
    # Create additional plot for top sources breakdown by label
    fig2, ax = plt.subplots(figsize=(12, 6))
    top_5_sources = df['source_domain'].value_counts().head(5).index.tolist()
    source_label_data = df[df['source_domain'].isin(top_5_sources)].groupby(
        ['source_domain', 'real']).size().unstack(fill_value=0)
    source_label_data.plot(kind='bar', ax=ax, color=['#ff6b6b', '#4ecdc4'], edgecolor='black')
    ax.set_title('Top 5 Sources: Real vs Fake News', fontsize=12, fontweight='bold')
    ax.set_xlabel('Source Domain')
    ax.set_ylabel('Article Count')
    ax.legend(['Fake', 'Real'])
    ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plot_path2 = os.path.join(output_dir, 'sources_real_vs_fake.png')
    plt.savefig(plot_path2, dpi=150, bbox_inches='tight')
    print(f"Saved plot to {plot_path2}")
    plt.close()


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess the FakeNewsNet dataset."""
    # Remove duplicates
    df = df.drop_duplicates()
    print(f"\nAfter removing duplicates: {len(df)} records")
    
    # Handle missing values
    df = df.dropna()
    print(f"After removing missing values: {len(df)} records")
    
    # Clean text data - remove leading/trailing whitespace
    df['title'] = df['title'].str.strip()
    df['news_url'] = df['news_url'].str.strip()
    df['source_domain'] = df['source_domain'].str.strip()
    
    # Ensure tweet_num is numeric
    df['tweet_num'] = pd.to_numeric(df['tweet_num'], errors='coerce').fillna(0).astype(int)
    
    # Ensure real is binary (0 or 1)
    df['real'] = df['real'].astype(int)
    
    # Reset index
    df = df.reset_index(drop=True)
    
    return df


def save_data(df: pd.DataFrame, filepath: str) -> None:
    """Save the cleaned dataset to a CSV file."""
    df.to_csv(filepath, index=False)
    print(f"\nSaved {len(df)} records to {filepath}")


def main():
    """Main function to run the fake news data cleaning pipeline."""
    # Get script directory for relative paths
    script_dir = get_script_dir()
    
    # Configuration
    input_file = os.path.join(script_dir, "FakeNewsNet.csv")
    output_file = os.path.join(script_dir, "FakeNewsNet_clean.csv")
    
    # Load data
    df = load_data(input_file)
    
    # Explore data
    explore_data(df)
    
    # Plot original data
    plot_data(df, script_dir)
    
    # Clean data
    df_clean = clean_data(df)
    
    # Save cleaned data
    save_data(df_clean, output_file)
    
    print("\nData cleaning completed!")


if __name__ == "__main__":
    main()
