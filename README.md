# Fake News Detection Data Cleaning & Analysis

A Python project for cleaning, preprocessing, and analyzing the FakeNewsNet dataset for fake news detection research.

![Dataset Overview](fake_news_project/fake_news_analysis.png)

## Dataset Summary

| Metric | Value |
|--------|-------|
| **Total Records** | 23,196 |
| **Real News** | 17,441 (75.2%) |
| **Fake News** | 5,755 (24.8%) |
| **Features** | 5 |
| **After Cleaning** | 22,730 records |

## Features

- **Data Cleaning**: Removes duplicates and missing values
- **Text Preprocessing**: Cleans whitespace from text fields
- **Data Validation**: Ensures numeric and binary fields are properly typed
- **Visualization**: Generates plots for data analysis

## Files

```
fakenews/
├── README.md
├── fake_news_project/
│   ├── fake_news_clean.py       # Main script
│   ├── FakeNewsNet.csv          # Original dataset
│   ├── FakeNewsNet_clean.csv    # Cleaned dataset
│   ├── fake_news_analysis.png   # Main visualization
│   └── sources_real_vs_fake.png # Source breakdown
```

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/fakenews.git
cd fakenews

# Install dependencies
pip install pandas numpy matplotlib
```

## Usage

```bash
# Run from the project root
python fake_news_project/fake_news_clean.py
```

## Generated Outputs

### Main Analysis Dashboard
![Analysis Dashboard](fake_news_project/fake_news_analysis.png)

### Source Distribution
![Source Analysis](fake_news_project/sources_real_vs_fake.png)

## Top News Sources

| Rank | Source | Articles |
|------|--------|----------|
| 1 | people.com | 1,786 |
| 2 | dailymail.co.uk | 964 |
| 3 | wikipedia.org | 741 |
| 4 | usmagazine.com | 709 |
| 5 | etonline.com | 666 |

## Dataset Columns

| Column | Type | Description |
|--------|------|-------------|
| `title` | string | News article title |
| `news_url` | string | URL to the article |
| `source_domain` | string | Domain of the news source |
| `tweet_num` | integer | Number of tweets about the article |
| `real` | binary | 1 = Real news, 0 = Fake news |

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
