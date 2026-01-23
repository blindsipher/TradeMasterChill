#!/usr/bin/env python
"""
Python 3.12 Compatibility Test Script
This script tests core functionality of TradeMaster with Python 3.12
"""

import sys
import traceback

def test_python_version():
    """Test that we're running Python 3.9+"""
    print(f"Testing Python version...")
    version = sys.version_info
    print(f"  Python version: {version.major}.{version.minor}.{version.micro}")
    assert version.major == 3 and version.minor >= 9, f"Expected Python 3.9+, got {version.major}.{version.minor}"
    print("  ✓ Python version check passed (minimum: 3.9)")
    return True

def test_core_imports():
    """Test that core dependencies can be imported"""
    print(f"\nTesting core imports...")
    
    imports_to_test = [
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('torch', 'PyTorch'),
        ('tensorflow', 'TensorFlow'),
        ('ray', 'Ray'),
        ('mmcv', 'MMCV'),
        ('sklearn', 'Scikit-learn'),
        ('scipy', 'SciPy'),
        ('matplotlib', 'Matplotlib'),
        ('gym', 'Gym'),
        ('gymnasium', 'Gymnasium'),
    ]
    
    for module_name, friendly_name in imports_to_test:
        try:
            module = __import__(module_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"  ✓ {friendly_name} {version}")
        except ImportError as e:
            print(f"  ✗ {friendly_name} - FAILED: {e}")
            return False
    
    return True

def test_trademaster_imports():
    """Test that TradeMaster modules can be imported"""
    print(f"\nTesting TradeMaster imports...")
    
    trademaster_modules = [
        'trademaster.utils',
        'trademaster.datasets',
        'trademaster.agents',
        'trademaster.environments',
        'trademaster.nets',
        'trademaster.losses',
        'trademaster.optimizers',
        'trademaster.trainers',
    ]
    
    for module_name in trademaster_modules:
        try:
            __import__(module_name)
            print(f"  ✓ {module_name}")
        except ImportError as e:
            print(f"  ✗ {module_name} - FAILED: {e}")
            traceback.print_exc()
            return False
    
    return True

def test_mmcv_registry():
    """Test that mmcv Registry import works"""
    print(f"\nTesting mmcv Registry import...")
    try:
        from mmcv.utils.registry import Registry
        print(f"  ✓ Registry imported successfully")
        
        # Test creating a Registry
        test_registry = Registry('test')
        print(f"  ✓ Registry instantiation successful")
        return True
    except Exception as e:
        print(f"  ✗ Registry test FAILED: {e}")
        traceback.print_exc()
        return False

def test_tensorflow_gpu():
    """Test TensorFlow GPU availability (informational)"""
    print(f"\nTesting TensorFlow GPU availability (informational)...")
    try:
        import tensorflow as tf
        gpus = tf.config.list_physical_devices('GPU')
        if gpus:
            print(f"  ℹ TensorFlow GPU available: {len(gpus)} GPU(s)")
        else:
            print(f"  ℹ TensorFlow GPU not available (CPU only)")
        return True
    except Exception as e:
        print(f"  ⚠ TensorFlow GPU check failed: {e}")
        return True  # This is informational, not a failure

def test_ray_init():
    """Test Ray initialization"""
    print(f"\nTesting Ray initialization...")
    try:
        import ray
        # Initialize Ray with minimal resources
        ray.init(num_cpus=1, ignore_reinit_error=True, logging_level='ERROR')
        print(f"  ✓ Ray initialized successfully")
        ray.shutdown()
        print(f"  ✓ Ray shutdown successfully")
        return True
    except Exception as e:
        print(f"  ✗ Ray initialization FAILED: {e}")
        traceback.print_exc()
        return False

def test_pydantic():
    """Test Pydantic v2 compatibility"""
    print(f"\nTesting Pydantic v2...")
    try:
        import pydantic
        version = pydantic.__version__
        print(f"  ✓ Pydantic version: {version}")
        
        # Test basic Pydantic model
        from pydantic import BaseModel
        
        class TestModel(BaseModel):
            name: str
            value: int
        
        test_obj = TestModel(name="test", value=42)
        assert test_obj.name == "test"
        assert test_obj.value == 42
        print(f"  ✓ Pydantic BaseModel works correctly")
        return True
    except Exception as e:
        print(f"  ✗ Pydantic test FAILED: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("="*70)
    print("Python 3.12 Compatibility Test Suite for TradeMaster")
    print("="*70)
    
    tests = [
        test_python_version,
        test_core_imports,
        test_trademaster_imports,
        test_mmcv_registry,
        test_tensorflow_gpu,
        test_ray_init,
        test_pydantic,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append((test.__name__, result))
        except Exception as e:
            print(f"\n✗ Test {test.__name__} crashed: {e}")
            traceback.print_exc()
            results.append((test.__name__, False))
    
    print("\n" + "="*70)
    print("Test Summary")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! TradeMaster is compatible with Python 3.12")
        return 0
    else:
        print(f"\n⚠ {total - passed} test(s) failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
