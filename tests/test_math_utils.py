import sys
sys.path.append('../PYTHON-BAZEL-CI')
from src.math_utils import *

def test_add():
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(4, 2) == 2
    assert divide(-1, 1) == -1
    assert divide(0, 1) == 0
    assert divide(1.5, 2) == 0.75

test_add()
test_subtract()
test_multiply()
test_divide()