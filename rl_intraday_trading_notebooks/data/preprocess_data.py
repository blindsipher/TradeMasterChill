"""
Data Preprocessing Script for Intraday Trading RL Notebooks
This script converts parquet files to CSV format and adds technical indicators
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

def add_technical_indicators(df):
    """
    Add technical indicators to the dataframe
    
    Args:
        df: DataFrame with OHLCV data
        
    Returns:
        DataFrame with added technical indicators
    """
    # Sort by datetime
    df = df.sort_values('datetime').reset_index(drop=True)
    
    # Adjusted close (for futures, we use close)
    df['adjcp'] = df['close']
    
    # Z-score normalization for OHLC
    for col in ['open', 'high', 'low', 'close', 'adjcp']:
        mean = df[col].rolling(window=20).mean()
        std = df[col].rolling(window=20).std()
        df[f'z{col}'] = (df[col] - mean) / (std + 1e-8)
    
    # Price difference indicators (zd_X represents X-period momentum)
    for period in [5, 10, 15, 20, 25, 30]:
        df[f'zd_{period}'] = df['close'].pct_change(period)
    
    # Fill NaN values at the beginning
    df = df.bfill()
    df = df.fillna(0)
    
    return df

def preprocess_parquet_to_csv(parquet_file, output_dir, train_ratio=0.7, valid_ratio=0.15):
    """
    Convert parquet file to train/valid/test CSV splits
    
    Args:
        parquet_file: Path to input parquet file
        output_dir: Directory to save CSV files
        train_ratio: Proportion of data for training
        valid_ratio: Proportion of data for validation
    """
    print(f"Processing {parquet_file}...")
    
    # Read parquet file
    df = pd.read_parquet(parquet_file)
    print(f"Loaded {len(df)} rows")
    
    # Add date column (extract date from datetime)
    df['date'] = pd.to_datetime(df['datetime']).dt.date.astype(str)
    
    # Add technical indicators
    df = add_technical_indicators(df)
    
    # Get unique dates for splitting
    unique_dates = sorted(df['date'].unique())
    n_dates = len(unique_dates)
    
    train_end = int(n_dates * train_ratio)
    valid_end = int(n_dates * (train_ratio + valid_ratio))
    
    train_dates = unique_dates[:train_end]
    valid_dates = unique_dates[train_end:valid_end]
    test_dates = unique_dates[valid_end:]
    
    # Split data
    train_df = df[df['date'].isin(train_dates)].copy()
    valid_df = df[df['date'].isin(valid_dates)].copy()
    test_df = df[df['date'].isin(test_dates)].copy()
    
    print(f"Train: {len(train_df)} rows ({len(train_dates)} days)")
    print(f"Valid: {len(valid_df)} rows ({len(valid_dates)} days)")
    print(f"Test: {len(test_df)} rows ({len(test_dates)} days)")
    
    # Create output directory
    contract_name = Path(parquet_file).stem.replace('_data_2020', '').replace('-1m_bk_2020', '')
    output_path = Path(output_dir) / contract_name
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Save to CSV
    train_df.to_csv(output_path / 'train.csv')
    valid_df.to_csv(output_path / 'valid.csv')
    test_df.to_csv(output_path / 'test.csv')
    
    print(f"Saved to {output_path}")
    print("-" * 50)
    
    return output_path

def main():
    """Main preprocessing function"""
    # Get all parquet files in the repository root
    repo_root = Path(__file__).resolve().parents[2]
    parquet_files = list(repo_root.glob('*.parquet'))
    
    if not parquet_files:
        print("No parquet files found!")
        return
    
    print(f"Found {len(parquet_files)} parquet files")
    print("=" * 50)
    
    # Output directory
    output_dir = Path(__file__).parent
    
    # Process each parquet file
    for parquet_file in parquet_files:
        try:
            preprocess_parquet_to_csv(parquet_file, output_dir)
        except Exception as e:
            print(f"Error processing {parquet_file}: {e}")
    
    print("\nPreprocessing complete!")

if __name__ == "__main__":
    main()
