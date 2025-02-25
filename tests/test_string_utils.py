import sys
sys.path.append('../PYTHON-BAZEL-CI')
from src.string_utils import *

def test_reverse_string():
    '''Some methods for testing the reverse string function'''
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("") == ""
    assert reverse_string("wow") == "wow"
    assert reverse_string("12345") == "54321"

def test_is_palindrome():
    '''Some methods for testing the palindrome function'''
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("a") == True
    assert is_palindrome("") == True

def test_count_vowels():
    '''Some methods for testing the count vowels function'''
    assert count_vowels("racecar") == 3
    assert count_vowels("world") == 1
    assert count_vowels("") == 0
    assert count_vowels("12345") == 0
    assert count_vowels("a") == 1

test_reverse_string()
test_is_palindrome()
test_count_vowels()
