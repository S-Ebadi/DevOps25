# Miles to Kilometers Converter

# Constants
MILES_TO_KILOMETERS = 1.60934
KILOMETERS_TO_MILES = 1 / MILES_TO_KILOMETERS

# User input
miles_input = 15
kilometers_input = 15

# Conversions
converted_to_km = miles_input * MILES_TO_KILOMETERS
converted_to_miles = kilometers_input * KILOMETERS_TO_MILES

# Display
print(f'{miles_input} miles is {converted_to_km:.2f} kilometers')
print(f'{kilometers_input} kilometers is {converted_to_miles:.2f} miles')
