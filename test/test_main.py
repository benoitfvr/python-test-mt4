import pytest
from main import calculate, main

def test_calculate_addition():
    assert calculate("20 5 +") == 25

def test_calculate_subtraction():
    assert calculate("4 2 + 3 -") == 3

