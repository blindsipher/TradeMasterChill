# OHLCV Upscaler - Quick Reference Guide

## 📖 Quick Start

### Install Dependencies
```bash
pip install pandas pyarrow
```

### Basic Commands

```bash
# List available timeframes
python ohlcv_upscaler.py --list-timeframes

# Upscale single file
python ohlcv_upscaler.py --input MCL-1m_data_2020.parquet --timeframe 5m

# Upscale to multiple timeframes
python ohlcv_upscaler.py --input MCL-1m_data_2020.parquet --timeframes 5m 15m 1h

# Process all 1m files
python ohlcv_upscaler.py --all --timeframes 5m 1h
```

## 🎯 Common Use Cases

### 1. Quick Experimentation
```bash
# Create 5m data for quick testing
python ohlcv_upscaler.py --all --timeframe 5m --quiet
```

### 2. Multi-Timeframe Strategy
```bash
# Create multiple timeframes for analysis
python ohlcv_upscaler.py --input MCL-1m_data_2020.parquet --timeframes 5m 15m 1h 4h
```

### 3. Custom Output Location
```bash
# Save to specific directory
python ohlcv_upscaler.py --input MCL-1m_data_2020.parquet --timeframe 1h \
    --output /path/to/output/MCL_hourly.parquet
```

## 📊 Timeframe Reference

| Timeframe | Data Reduction | Best For |
|-----------|----------------|----------|
| 5m | ~5x | Scalping strategies |
| 15m | ~15x | Intraday trading |
| 30m | ~30x | Short-term swing |
| 1h | ~60x | Day trading |
| 4h | ~240x | Swing trading |
| 1d | ~1440x | Position trading |

## 🔧 Troubleshooting

### Problem: "Invalid frequency" error
**Solution**: Use newer pandas version or check timeframe spelling

### Problem: Script runs but no output
**Solution**: Check if input file exists, use absolute paths

### Problem: Output size unexpectedly large
**Solution**: This is normal for markets with 24/7 trading (futures, crypto)

## 💡 Best Practices

1. **Always validate output**: Check OHLC relationships after upscaling
2. **Use appropriate timeframes**: Match timeframe to your trading strategy
3. **Keep 1m data**: Don't delete original high-resolution data
4. **Batch processing**: Process all files at once with `--all` flag
5. **Quality over speed**: Don't skip validation for production use

## 📝 Python API Examples

### Basic Usage
```python
from ohlcv_upscaler import OHLCVUpscaler

upscaler = OHLCVUpscaler(verbose=True)
upscaler.upscale_file('MCL-1m_data_2020.parquet', '5m')
```

### DataFrame Processing
```python
import pandas as pd
from ohlcv_upscaler import OHLCVUpscaler

df = pd.read_parquet('MCL-1m_data_2020.parquet')
upscaler = OHLCVUpscaler()
df_5m = upscaler.upscale_ohlcv(df, '5m')
df_5m.to_parquet('MCL-5m.parquet')
```

### Batch Processing
```python
from pathlib import Path
from ohlcv_upscaler import OHLCVUpscaler

upscaler = OHLCVUpscaler(verbose=True)
input_files = list(Path('.').glob('*-1m*.parquet'))
timeframes = ['5m', '15m', '1h']

output_files = upscaler.upscale_multiple_files(input_files, timeframes)
print(f"Created {len(output_files)} files")
```

## 🔍 Data Validation Script

```python
import pandas as pd

def validate_upscaled_data(file_path):
    """Validate upscaled OHLCV data quality"""
    df = pd.read_parquet(file_path)
    
    checks = {
        'Sorted': df['datetime'].is_monotonic_increasing,
        'High >= Open': (df['high'] >= df['open']).all(),
        'High >= Close': (df['high'] >= df['close']).all(),
        'Low <= Open': (df['low'] <= df['open']).all(),
        'Low <= Close': (df['low'] <= df['close']).all(),
        'No NaNs': not df.isna().any().any(),
    }
    
    for check, passed in checks.items():
        print(f"{check}: {'✓' if passed else '✗'}")
    
    return all(checks.values())

# Usage
validate_upscaled_data('MCL-5m_data_2020.parquet')
```

## 📚 Additional Resources

- Full documentation: `README_UPSCALER.md`
- Example usage: `example_usage.py`
- Source code: `ohlcv_upscaler.py`

## 🆘 Getting Help

```bash
# Show help
python ohlcv_upscaler.py --help

# List timeframes
python ohlcv_upscaler.py --list-timeframes

# Run with verbose output
python ohlcv_upscaler.py --input file.parquet --timeframe 5m

# Suppress output
python ohlcv_upscaler.py --input file.parquet --timeframe 5m --quiet
```

---

**Quick Tip**: Start with 5m or 15m timeframes for initial testing, then move to 1h for production strategies.
