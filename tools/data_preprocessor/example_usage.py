"""
Example Usage of OHLCV Upscaler

This script demonstrates common use cases for the OHLCV upscaling tool.
"""

import pandas as pd
from pathlib import Path
import sys

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent))
from ohlcv_upscaler import OHLCVUpscaler


def example_1_basic_upscaling():
    """Example 1: Basic upscaling of a single file"""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic Upscaling")
    print("=" * 70)
    
    upscaler = OHLCVUpscaler(verbose=True)
    
    # Find a 1m data file
    repo_root = Path(__file__).resolve().parents[2]
    input_file = repo_root / 'MCL-1m_data_2020.parquet'
    
    if not input_file.exists():
        print(f"File not found: {input_file}")
        return
    
    # Upscale to 5 minutes
    output_file = upscaler.upscale_file(input_file, '5m')
    print(f"\n✓ Created: {output_file}")


def example_2_dataframe_upscaling():
    """Example 2: Work directly with DataFrames"""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: DataFrame Upscaling")
    print("=" * 70)
    
    upscaler = OHLCVUpscaler(verbose=True)
    
    # Load 1m data
    repo_root = Path(__file__).resolve().parents[2]
    input_file = repo_root / 'MGC-1m_data_2020.parquet'
    
    if not input_file.exists():
        print(f"File not found: {input_file}")
        return
    
    df_1m = pd.read_parquet(input_file)
    print(f"\nOriginal 1m data shape: {df_1m.shape}")
    
    # Upscale to different timeframes
    df_15m = upscaler.upscale_ohlcv(df_1m, '15m')
    df_1h = upscaler.upscale_ohlcv(df_1m, '1h')
    
    print(f"15m data shape: {df_15m.shape}")
    print(f"1h data shape: {df_1h.shape}")
    
    # Save results
    output_dir = repo_root / 'examples_output'
    output_dir.mkdir(exist_ok=True)
    
    df_15m.to_parquet(output_dir / 'MGC-15m_example.parquet')
    df_1h.to_parquet(output_dir / 'MGC-1h_example.parquet')
    
    print(f"\n✓ Saved to: {output_dir}")


def example_3_compare_timeframes():
    """Example 3: Compare statistics across timeframes"""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Compare Timeframes")
    print("=" * 70)
    
    repo_root = Path(__file__).resolve().parents[2]
    
    # Load different timeframes
    files = {
        '1m': repo_root / 'MCL-1m_data_2020.parquet',
        '5m': repo_root / 'MCL-5m_data_2020.parquet',
        '1h': repo_root / 'MCL-1h_data_2020.parquet',
    }
    
    print("\nTimeframe comparison for MCL (Micro Crude Oil):")
    print("-" * 70)
    print(f"{'Timeframe':<12} {'Rows':>10} {'Date Range':>25} {'Avg Volume':>15}")
    print("-" * 70)
    
    for tf, file in files.items():
        if not file.exists():
            continue
        
        df = pd.read_parquet(file)
        date_range = f"{df['datetime'].min().date()} to {df['datetime'].max().date()}"
        avg_volume = df['volume'].mean()
        
        print(f"{tf:<12} {len(df):>10,} {date_range:>25} {avg_volume:>15,.0f}")


def example_4_multi_contract_analysis():
    """Example 4: Analyze multiple contracts at same timeframe"""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Multi-Contract Analysis")
    print("=" * 70)
    
    repo_root = Path(__file__).resolve().parents[2]
    
    # Load 1h data for all contracts
    contracts = ['MCL', 'MGC', 'mes']
    
    print("\n1-hour timeframe comparison:")
    print("-" * 70)
    print(f"{'Contract':<12} {'Rows':>10} {'Avg Close':>15} {'Volatility %':>15}")
    print("-" * 70)
    
    for contract in contracts:
        file = repo_root / f'{contract}-1h_data_2020.parquet'
        if not file.exists():
            continue
        
        df = pd.read_parquet(file)
        avg_close = df['close'].mean()
        volatility = (df['close'].std() / df['close'].mean() * 100)
        
        print(f"{contract:<12} {len(df):>10,} {avg_close:>15,.2f} {volatility:>14,.2f}%")


def example_5_validate_upscaling():
    """Example 5: Validate upscaling quality"""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Validate Upscaling Quality")
    print("=" * 70)
    
    upscaler = OHLCVUpscaler(verbose=False)
    
    repo_root = Path(__file__).resolve().parents[2]
    df_1m = pd.read_parquet(repo_root / 'MCL-1m_data_2020.parquet')
    
    print("\nValidating upscaling to 5m...")
    df_5m = upscaler.upscale_ohlcv(df_1m, '5m')
    
    # Check OHLC relationships
    checks = {
        'High >= Open': (df_5m['high'] >= df_5m['open']).all(),
        'High >= Close': (df_5m['high'] >= df_5m['close']).all(),
        'Low <= Open': (df_5m['low'] <= df_5m['open']).all(),
        'Low <= Close': (df_5m['low'] <= df_5m['close']).all(),
        'Volume > 0': (df_5m['volume'] > 0).all(),
        'No NaN values': not df_5m.isna().any().any(),
        'Sorted datetime': df_5m['datetime'].is_monotonic_increasing,
    }
    
    print("\nQuality checks:")
    print("-" * 70)
    for check, passed in checks.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{check:<25} {status}")
    
    all_passed = all(checks.values())
    print("-" * 70)
    print(f"\n{'✓ All checks passed!' if all_passed else '✗ Some checks failed!'}")


def main():
    """Run all examples"""
    print("\n" + "=" * 70)
    print("OHLCV UPSCALER - USAGE EXAMPLES")
    print("=" * 70)
    
    examples = [
        example_1_basic_upscaling,
        example_2_dataframe_upscaling,
        example_3_compare_timeframes,
        example_4_multi_contract_analysis,
        example_5_validate_upscaling,
    ]
    
    for i, example in enumerate(examples, 1):
        try:
            example()
        except Exception as e:
            print(f"\n✗ Example {i} failed: {e}")
    
    print("\n" + "=" * 70)
    print("Examples complete!")
    print("=" * 70 + "\n")


if __name__ == '__main__':
    main()
