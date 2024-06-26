import pytest
from main import calculate, main

def test_calculate_addition():
    assert calculate("20 5 +") == 25

def test_calculate_subtraction():
    assert calculate("4 2 + 3 -") == 3

def test_calculate_multiplication():
    assert calculate("3 5 8 * 7 + *") == 141

def test_calculate_complex_expression():
    assert calculate("3 5 8 * 7 + *") == 141

