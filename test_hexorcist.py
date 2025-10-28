# Import your functions from your main file
from hexorcist import to_decimal, from_decimal

# --- to_decimal tests ---
def test_to_decimal_binary():
    assert to_decimal("1011", 2) == 11

def test_to_decimal_hex():
    assert to_decimal("C7", 16) == 199

def test_to_decimal_octal():
    assert to_decimal("123", 8) == 83

def test_to_decimal_lowercase():
    assert to_decimal("c7", 16) == 199

def test_to_decimal_base36():
    assert to_decimal("ZZ", 36) == 1295

def test_to_decimal_zero():
    assert to_decimal("0", 10) == 0


# --- from_decimal tests ---
def test_from_decimal_binary():
    assert from_decimal(11, 2) == "1011"

def test_from_decimal_hex():
    assert from_decimal(199, 16) == "C7"

def test_from_decimal_octal():
    assert from_decimal(83, 8) == "123"

def test_from_decimal_base36():
    assert from_decimal(1295, 36) == "ZZ"

def test_from_decimal_zero():
    assert from_decimal(0, 16) == "0"


# --- Round-trip tests (any base → decimal → target base) ---
def test_round_trip_hex_to_binary():
    decimal_value = to_decimal("C7", 16)
    converted_value = from_decimal(decimal_value, 2)
    assert converted_value == "11000111"

def test_round_trip_binary_to_hex():
    decimal_value = to_decimal("11000111", 2)
    converted_value = from_decimal(decimal_value, 16)
    assert converted_value == "C7"
