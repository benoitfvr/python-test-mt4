import pytest
from main import calculate, main

def test_should_calculate_addition():
    assert calculate("20 5 +") == 25

def test_should_calculate_subtraction():
    assert calculate("4 2 + 3 -") == 3

def test_should_calculate_multiplication():
    assert calculate("3 5 8 * 7 + *") == 141

def test_should_calculate_complex_expression():
    assert calculate("3 5 8 * 7 + *") == 141
    
def test_should_raise_error_invalid_expression():
    with pytest.raises(IndexError):
        calculate("4 +")

def test_should_raise_error_non_integer():
    with pytest.raises(ValueError):
        calculate("4 a +")

def test_should_raise_error_empty_expression():
    with pytest.raises(IndexError):
        calculate("")
        
def test_should_capture_input_and_output(monkeypatch, capsys):
    inputs = iter(["3 5 8 * 7 + *", "exit"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))

    main()
    
    captured = capsys.readouterr()
    assert "Résultat : 141" in captured.out
    assert "Entrez un calcul (ou tapez 'exit' pour quitter) :" in captured.out