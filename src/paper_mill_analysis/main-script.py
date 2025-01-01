# src/paper_mill_analysis/__main__.py

from pathlib import Path
import pandas as pd
from .data_retrieval import retrieve_paper_data
from .data_processing import clean_dataframe, extract_unique_titles, get_summary_statistics

def main():
    # Create data directory if it doesn't exist
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Retrieve raw data
    print("Retrieving paper mill data...")
    df_paper = retrieve_paper_data()
    df_paper.to_excel(data_dir / "raw_data.xlsx")
    
    # Process data
    print("Processing data...")
    df_cleaned = clean_dataframe(df_paper)
    df_titles = extract_unique_titles(df_cleaned)
    
    # Save processed data
    df_cleaned.to_excel(data_dir / "processed_data.xlsx")
    df_titles.to_excel(data_dir / "unique_titles.xlsx")
    
    # Generate and print summary statistics
    stats = get_summary_statistics(df_cleaned)
    print("\nSummary Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
