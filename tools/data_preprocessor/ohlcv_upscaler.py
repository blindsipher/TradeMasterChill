"""
OHLCV Data Upscaling Script for TradeMaster

This script upscales 1-minute OHLCV (Open, High, Low, Close, Volume) data to higher timeframes.

Best Practices for OHLCV Upscaling:
1. Open: First value in the period
2. High: Maximum value in the period
3. Low: Minimum value in the period
4. Close: Last value in the period
5. Volume: Sum of all volumes in the period

Supported Timeframes:
- 5m: 5 minutes
- 15m: 15 minutes
- 30m: 30 minutes
- 1h: 1 hour
- 4h: 4 hours
- 1d: 1 day

Usage:
    python ohlcv_upscaler.py --input MCL-1m_data_2020.parquet --timeframe 5m
    python ohlcv_upscaler.py --input MCL-1m_data_2020.parquet --timeframe 1h --output MCL-1h_data_2020.parquet
    python ohlcv_upscaler.py --all --timeframes 5m 15m 1h
"""

import pandas as pd
import numpy as np
import argparse
from pathlib import Path
from typing import List, Optional
import sys


class OHLCVUpscaler:
    """
    Class for upscaling OHLCV data from 1-minute to higher timeframes.
    
    Attributes:
        VALID_TIMEFRAMES: Dictionary mapping timeframe strings to pandas offset aliases
    """
    
    VALID_TIMEFRAMES = {
        '5m': '5min',    # 5 minutes
        '15m': '15min',  # 15 minutes
        '30m': '30min',  # 30 minutes
        '1h': '1h',      # 1 hour (also accepts '1H')
        '2h': '2h',      # 2 hours
        '4h': '4h',      # 4 hours
        '1d': '1D',      # 1 day
    }
    
    def __init__(self, verbose: bool = True):
        """
        Initialize the upscaler.
        
        Args:
            verbose: If True, print progress messages
        """
        self.verbose = verbose
    
    def _log(self, message: str):
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(message)
    
    def validate_timeframe(self, timeframe: str) -> str:
        """
        Validate and return the pandas offset alias for a timeframe.
        
        Args:
            timeframe: Timeframe string (e.g., '5m', '1h')
            
        Returns:
            Pandas offset alias
            
        Raises:
            ValueError: If timeframe is not valid
        """
        if timeframe not in self.VALID_TIMEFRAMES:
            raise ValueError(
                f"Invalid timeframe '{timeframe}'. "
                f"Valid options: {list(self.VALID_TIMEFRAMES.keys())}"
            )
        return self.VALID_TIMEFRAMES[timeframe]
    
    def upscale_ohlcv(
        self,
        df: pd.DataFrame,
        timeframe: str,
        datetime_col: str = 'datetime'
    ) -> pd.DataFrame:
        """
        Upscale OHLCV data to a higher timeframe.
        
        Args:
            df: DataFrame with columns [datetime, open, high, low, close, volume]
            timeframe: Target timeframe (e.g., '5m', '1h')
            datetime_col: Name of the datetime column
            
        Returns:
            DataFrame with upscaled OHLCV data
        """
        # Validate timeframe
        freq = self.validate_timeframe(timeframe)
        
        # Make a copy to avoid modifying original
        df = df.copy()
        
        # Ensure datetime column is datetime type
        if not pd.api.types.is_datetime64_any_dtype(df[datetime_col]):
            df[datetime_col] = pd.to_datetime(df[datetime_col])
        
        # Sort by datetime
        df = df.sort_values(datetime_col).reset_index(drop=True)
        
        # Set datetime as index for resampling
        df.set_index(datetime_col, inplace=True)
        
        self._log(f"Upscaling from 1m to {timeframe}...")
        self._log(f"Original shape: {df.shape}")
        
        # Define aggregation rules following best practices
        # OHLCV aggregation:
        # - Open: first value in period
        # - High: maximum value in period
        # - Low: minimum value in period
        # - Close: last value in period
        # - Volume: sum of volumes in period
        agg_dict = {
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        }
        
        # Resample to target timeframe
        upscaled = df.resample(freq).agg(agg_dict)
        
        # Remove rows with NaN values (incomplete periods)
        upscaled = upscaled.dropna()
        
        # Reset index to make datetime a column again
        upscaled = upscaled.reset_index()
        
        self._log(f"Upscaled shape: {upscaled.shape}")
        self._log(f"Reduction factor: {len(df) / len(upscaled):.2f}x")
        
        return upscaled
    
    def upscale_file(
        self,
        input_path: Path,
        timeframe: str,
        output_path: Optional[Path] = None
    ) -> Path:
        """
        Upscale a parquet file to a higher timeframe.
        
        Args:
            input_path: Path to input parquet file (1m data)
            timeframe: Target timeframe (e.g., '5m', '1h')
            output_path: Path for output file (auto-generated if None)
            
        Returns:
            Path to the output file
        """
        # Read input file
        self._log(f"\nReading {input_path}...")
        df = pd.read_parquet(input_path)
        
        # Upscale data
        upscaled = self.upscale_ohlcv(df, timeframe)
        
        # Generate output path if not provided
        if output_path is None:
            # Replace -1m with -<timeframe> in filename
            filename = input_path.stem
            if '-1m' in filename:
                new_filename = filename.replace('-1m', f'-{timeframe}')
            else:
                # If no -1m suffix, add timeframe before extension
                new_filename = f"{filename}_{timeframe}"
            
            output_path = input_path.parent / f"{new_filename}{input_path.suffix}"
        
        # Save to parquet
        self._log(f"Saving to {output_path}...")
        upscaled.to_parquet(output_path, index=False)
        
        self._log(f"✓ Successfully created {output_path}")
        return output_path
    
    def upscale_multiple_files(
        self,
        input_files: List[Path],
        timeframes: List[str]
    ) -> List[Path]:
        """
        Upscale multiple files to multiple timeframes.
        
        Args:
            input_files: List of input parquet files
            timeframes: List of target timeframes
            
        Returns:
            List of output file paths
        """
        output_files = []
        
        total = len(input_files) * len(timeframes)
        current = 0
        
        for input_file in input_files:
            for timeframe in timeframes:
                current += 1
                self._log(f"\n{'='*60}")
                self._log(f"Processing {current}/{total}: {input_file.name} -> {timeframe}")
                self._log(f"{'='*60}")
                
                try:
                    output_file = self.upscale_file(input_file, timeframe)
                    output_files.append(output_file)
                except Exception as e:
                    self._log(f"✗ Error processing {input_file.name}: {e}")
        
        return output_files


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(
        description='Upscale 1-minute OHLCV data to higher timeframes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Upscale a single file to 5 minutes
  python ohlcv_upscaler.py --input MCL-1m_data_2020.parquet --timeframe 5m
  
  # Upscale with custom output name
  python ohlcv_upscaler.py --input MCL-1m_data_2020.parquet --timeframe 1h --output MCL-1h.parquet
  
  # Upscale all 1m parquet files in current directory to multiple timeframes
  python ohlcv_upscaler.py --all --timeframes 5m 15m 1h
  
  # Upscale specific files to multiple timeframes
  python ohlcv_upscaler.py --input MCL-1m_data_2020.parquet MGC-1m_data_2020.parquet --timeframes 5m 1h
        """
    )
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=False)
    input_group.add_argument(
        '--input', '-i',
        type=str,
        nargs='+',
        help='Input parquet file(s) with 1m OHLCV data'
    )
    input_group.add_argument(
        '--all',
        action='store_true',
        help='Process all *-1m*.parquet files in repository root'
    )
    
    # Timeframe options
    parser.add_argument(
        '--timeframe', '-t',
        type=str,
        help='Target timeframe (use --timeframes for multiple)'
    )
    parser.add_argument(
        '--timeframes',
        type=str,
        nargs='+',
        help='Multiple target timeframes'
    )
    
    # Output options
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output file path (only for single file input)'
    )
    
    # Other options
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Suppress progress messages'
    )
    
    parser.add_argument(
        '--list-timeframes',
        action='store_true',
        help='List available timeframes and exit'
    )
    
    args = parser.parse_args()
    
    # List timeframes and exit
    if args.list_timeframes:
        print("Available timeframes:")
        for tf, freq in OHLCVUpscaler.VALID_TIMEFRAMES.items():
            print(f"  {tf:6s} - {freq}")
        return
    
    # Validate that input is provided if not listing timeframes
    if not args.input and not args.all:
        print("Error: Either --input or --all must be specified")
        parser.print_help()
        sys.exit(1)
    
    # Validate timeframe arguments
    timeframes = []
    if args.timeframe:
        timeframes = [args.timeframe]
    elif args.timeframes:
        timeframes = args.timeframes
    else:
        print("Error: Either --timeframe or --timeframes must be specified")
        parser.print_help()
        sys.exit(1)
    
    # Get input files
    if args.all:
        # Find all *-1m*.parquet files in repository root
        # Assuming script is in tools/data_preprocessor/
        repo_root = Path(__file__).resolve().parents[2]
        input_files = sorted(repo_root.glob('*-1m*.parquet'))
        
        if not input_files:
            print(f"Error: No *-1m*.parquet files found in {repo_root}")
            sys.exit(1)
    else:
        input_files = [Path(f) for f in args.input]
        
        # Validate input files exist
        for f in input_files:
            if not f.exists():
                print(f"Error: File not found: {f}")
                sys.exit(1)
    
    # Validate output option
    if args.output and (len(input_files) > 1 or len(timeframes) > 1):
        print("Error: --output can only be used with single file and single timeframe")
        sys.exit(1)
    
    # Create upscaler
    upscaler = OHLCVUpscaler(verbose=not args.quiet)
    
    # Process files
    if args.output:
        # Single file, single timeframe with custom output
        output_path = Path(args.output)
        upscaler.upscale_file(input_files[0], timeframes[0], output_path)
    elif len(input_files) == 1 and len(timeframes) == 1:
        # Single file, single timeframe with auto output
        upscaler.upscale_file(input_files[0], timeframes[0])
    else:
        # Multiple files/timeframes
        output_files = upscaler.upscale_multiple_files(input_files, timeframes)
        
        if not args.quiet:
            print(f"\n{'='*60}")
            print(f"Summary: Created {len(output_files)} upscaled files")
            print(f"{'='*60}")


if __name__ == '__main__':
    main()
