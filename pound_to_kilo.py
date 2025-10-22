# Pounds to Kilograms Converter

# Constants
POUNDS_TO_KILOGRAMS = 0.453592
KILOGRAMS_TO_POUNDS = 1 / POUNDS_TO_KILOGRAMS

# User input
pounds_input = 15
kilograms_input = 15

# Conversions
converted_to_kg = pounds_input * POUNDS_TO_KILOGRAMS
converted_to_pounds = kilograms_input * KILOGRAMS_TO_POUNDS

# Display
print(f'{pounds_input} pounds is {converted_to_kg:.2f} kilograms')
print(f'{kilograms_input} kilograms is {converted_to_pounds:.2f} pounds')

POUNDS_TO_KILOGRAMS = 0.453592
KILOGRAMS_TO_POUNDS = 1 / POUNDS_TO_KILOGRAMS

# Functions for conversion

def pounds_to_kilograms(pounds):
    return pounds * POUNDS_TO_KILOGRAMS

def kilograms_to_pounds(kilograms):
    return kilograms * KILOGRAMS_TO_POUNDS

def main():
    pounds_input = 15
    kilograms_input = 15

    converted_to_kg = pounds_to_kilograms(pounds_input)
    converted_to_pounds = kilograms_to_pounds(kilograms_input)

    print(f'{pounds_input} pounds is {converted_to_kg:.2f} kilograms')
    print(f'{kilograms_input} kilograms is {converted_to_pounds:.2f} pounds')