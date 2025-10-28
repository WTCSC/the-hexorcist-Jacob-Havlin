[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21234520)
# The Hexorcist: Base Converter

The Hexorcist is a Python-based utility designed to convert numbers between various numeral systems. It supports conversions across binary, octal, decimal, hexadecimal, and up to base-36, providing an accurate and reliable solution for numerical base conversions.

## Features

- **`to_decimal(number_string, original_base)`**: Converts a number from any base (2–36) to a decimal (base-10) integer.  
- **`from_decimal(decimal_number, target_base)`**: Converts a decimal integer to any base (2–36).  
- **Round-trip conversion**: Facilitates verification by converting a number from one base to decimal and then to another base.  
- **Interactive mode**: The program can be run directly to enter numbers via a prompt and see conversion results.

## Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/WTCSC/the-hexorcist-Jacob-Havlin.git
cd the-hexorcist-Jacob-Havlin
````

## Usage

### Interactive Mode

Run the main script directly:

```bash
python hexorcist.py
```

You will be prompted to enter:

* Your number string
* The original base
* The target base

The program will display the converted result.

### Programmatic Mode (Import Functions)

You can import the functions into another Python script:

```python
from hexorcist import to_decimal, from_decimal

# Convert from any base to decimal
decimal_value = to_decimal("C7", 16)
print(decimal_value)  # Output: 199

# Convert from decimal to any base
converted_value = from_decimal(decimal_value, 2)
print(converted_value)  # Output: "11000111"

# Round-trip conversion (any base to any base)
decimal_value = to_decimal("C7", 16)
converted_value = from_decimal(decimal_value, 36)
print(converted_value)  # Output: "5B"
```

## Testing

Automated tests have been implemented using pytest. To execute the tests:

```bash
pytest test_hexorcist.py
```

All tests validate both individual functions and full round-trip conversions.

## License

This project is licensed under the MIT License.


