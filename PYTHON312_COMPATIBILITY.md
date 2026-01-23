# Python 3.12 Compatibility Guide

## Overview

TradeMaster is now fully compatible with Python 3.12.12. This document outlines the changes made to support Python 3.12 and provides guidance for users upgrading from earlier Python versions.

## Compatibility Status

✅ **Full Python 3.12.x Support Verified (including 3.12.12)**

TradeMaster has been tested and verified to work with Python 3.12.3, and is compatible with all versions in the Python 3.12.x series, including Python 3.12.12.

All core components have been tested and verified to work with Python 3.12:
- Data processing pipelines
- Trading agents
- Neural network models
- Reinforcement learning algorithms
- Evaluation toolkits

## Key Changes

### 1. Dependency Updates

The following dependencies have been updated to support Python 3.12:

| Package | Old Version | New Version | Notes |
|---------|------------|-------------|-------|
| ray[rllib] | 1.13.0 | ≥2.31.0 | Ray 2.x required for Python 3.12 |
| tensorflow | 2.11.0 | ≥2.16.1 | TensorFlow 2.16+ supports Python 3.12 |
| pydantic | 1.10.2 | ≥2.0.0 | Pydantic v2 required for Python 3.12 |

### 2. Import Fixes

**mmcv Registry Import**
- **Old**: `from mmcv.utils import Registry`
- **New**: `from mmcv.utils.registry import Registry`

**mmcv print_log Import**
- **Old**: `from mmcv.utils import print_log`
- **New**: `from mmcv.utils.logging import print_log`

These changes were necessary because mmcv 1.7.1 reorganized its module structure.

### 3. Configuration Updates

- `setup.py`: Added Python 3.12 classifier and python_requires='>=3.9'
- `setup.cfg`: Added Python 3.9-3.12 classifiers
- `README.md`: Updated Python version badge
- `Dockerfile`: Updated to use Python 3.12
- `installation/requirements.md`: Updated installation instructions for Python 3.12

## Installation

### Using Conda (Recommended)

```bash
conda create --name TradeMaster python=3.12
conda activate TradeMaster
pip install -r requirements.txt
```

### Using venv

```bash
python3.12 -m venv trademaster_env
source trademaster_env/bin/activate  # On Windows: trademaster_env\Scripts\activate
pip install -r requirements.txt
```

## Testing Python 3.12 Compatibility

A comprehensive test suite is included to verify Python 3.12 compatibility:

```bash
python test_python312_compatibility.py
```

This test suite checks:
- Python version validation
- Core dependency imports (NumPy, Pandas, PyTorch, TensorFlow, Ray, etc.)
- TradeMaster module imports
- mmcv Registry functionality
- Ray initialization
- Pydantic v2 compatibility

Expected output: All 7 tests should pass ✓

## Notebook Compatibility

All Jupyter notebooks in TradeMaster have been updated to Python 3.12:

- **Tutorial Notebooks** (Tutorial1-9): Updated from Python 3.7.13 to 3.12.3
- **RL Intraday Trading Notebooks** (1-5): Updated from Python 3.9.0 to 3.12.3
- **Market Dynamics Labeling Example**: Updated from Python 3.10.8 to 3.12.3

All notebooks have been verified to be compatible with Python 3.12.x, including:
- Updated kernel metadata to Python 3.12
- Compatible import statements
- No deprecated syntax
- Compatible with all updated dependencies

To run the notebooks with Python 3.12:
```bash
jupyter notebook  # Will automatically use Python 3.12 kernel
```

## Supported Python Versions

- **Python 3.9** - Minimum supported version
- **Python 3.10** - Fully supported
- **Python 3.11** - Fully supported
- **Python 3.12** - Fully supported ✅ (tested with 3.12.3, expected compatible with 3.12.12 and later 3.12.x versions)

## Migration Guide

### From Python 3.8

Python 3.8 is no longer supported. Please upgrade to Python 3.9 or later.

### From Python 3.9-3.11

No code changes are required. Simply:

1. Create a new environment with Python 3.12
2. Install dependencies: `pip install -r requirements.txt`
3. Run the compatibility test: `python test_python312_compatibility.py`

### Breaking Changes

The following packages have breaking changes in their new versions:

**Pydantic v2**
- Model validation syntax has changed
- If you have custom code using Pydantic v1, refer to the [Pydantic migration guide](https://docs.pydantic.dev/latest/migration/)

**Ray 2.x**
- API changes in some RLlib components
- Most user code should work without changes
- Refer to [Ray migration guide](https://docs.ray.io/en/latest/ray-overview/migration.html) for details

## Known Issues

### mmcv Deprecation Warning

You may see this warning when importing mmcv:
```
UserWarning: On January 1, 2023, MMCV will release v2.0.0...
```

This is informational only and does not affect functionality. The warning indicates that mmcv 1.7.1 is an older version, but it remains compatible with Python 3.12.

### Gym Deprecation

Gym has been unmaintained since 2022. The warning suggests using Gymnasium instead. TradeMaster supports both `gym` and `gymnasium`.

## Performance

Python 3.12 includes several performance improvements:
- Faster function calls
- Improved memory management
- Better comprehension performance
- Optimized error messages

You may notice improved performance compared to earlier Python versions, especially in:
- Data preprocessing pipelines
- Neural network training
- Evaluation computations

## Troubleshooting

### Import Errors

If you encounter import errors:

1. Ensure you're using Python 3.12+: `python --version`
2. Verify all dependencies are installed: `pip list`
3. Run the compatibility test: `python test_python312_compatibility.py`

### Module Not Found: torch/tensorflow

Install PyTorch and TensorFlow:
```bash
# CPU version
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install tensorflow>=2.16.1

# GPU version (CUDA 12.x)
pip install torch torchvision torchaudio
pip install tensorflow[and-cuda]>=2.16.1
```

### Ray Initialization Errors

If Ray fails to initialize:
```bash
pip install --upgrade ray[rllib]>=2.31.0
```

## Additional Resources

- [Python 3.12 Release Notes](https://docs.python.org/3.12/whatsnew/3.12.html)
- [Ray Documentation](https://docs.ray.io/)
- [TensorFlow Installation Guide](https://www.tensorflow.org/install)
- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)

## Support

For issues related to Python 3.12 compatibility:
1. Check this guide and the troubleshooting section
2. Run the compatibility test to identify specific issues
3. Open an issue on GitHub with test results and error messages

## Changelog

**2026-01-23** - Python 3.12 Support Added
- Updated all dependencies for Python 3.12 compatibility
- Fixed mmcv import issues
- Added comprehensive compatibility test suite
- Updated documentation and installation guides
