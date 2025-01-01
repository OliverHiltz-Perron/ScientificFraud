import pandas as pd

def clean_dataframe(df: pd.DataFrame, exchange_rate: float = 0.014) -> pd.DataFrame:
    """Clean and process the paper mill data."""
    df = df.copy()
    
    # Clean text columns
    text_columns = ["Base_title", "First_title", "Suspected_second_title"]
    for col in text_columns:
        df[col] = df[col].str.replace('[^\w\s]', '', regex=True)
    
    # Filter invalid entries
    df = df[df['Base_title'].str.strip() != ""]
    df['title_length'] = df['First_title'].str.len()
    df = df[df['title_length'] > 20]
    df = df[df['Price_Ruble'] != '0']
    
    # Process price data
    df['Price_Ruble'] = df['Price_Ruble'].astype('float')
    df['USD'] = df['Price_Ruble'] * exchange_rate
    
    return df

def extract_unique_titles(df: pd.DataFrame) -> pd.DataFrame:
    """Extract unique titles from the dataset."""
    return (df.drop_duplicates(subset=['Base_title'])
              [['Contract_number', 'Base_title']]
              .reset_index(drop=True))

def get_summary_statistics(df: pd.DataFrame) -> dict:
    """Calculate summary statistics for the dataset."""
    return {
        'total_papers': len(df['Base_title'].unique()),
        'total_contracts': len(df),
        'avg_price_usd': df['USD'].mean(),
        'total_revenue_usd': df['USD'].sum(),
        'papers_per_journal': df.groupby('Scopus').size().to_dict(),
        'web_of_science_count': df['Web_of_science'].value_counts().to_dict()
    }