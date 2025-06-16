import pytest

from hatchlor_demo.core import fib


def test_fib():
    """API Tests"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(RuntimeError):
        fib(-10)
