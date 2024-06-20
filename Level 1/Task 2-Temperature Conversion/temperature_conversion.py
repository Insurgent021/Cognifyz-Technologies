def temperature_converter(unit):
    # Check if the unit is Fahrenheit
    if unit.upper() == "F":
        # Convert from Fahrenheit to Celsius
        converted_temp = (5/9) * (temp - 32)
        print(f"Converted temperature is {converted_temp:.2f} Celsius")
    # Check if the unit is Celsius
    elif unit.upper() == "C":
        # Convert from Celsius to Fahrenheit
        converted_temp = (9/5) * temp + 32
        print(f"Converted temperature is {converted_temp:.2f} Fahrenheit")
    # If the unit is neither Fahrenheit nor Celsius
    else:
        print("Invalid unit!")


temp = float(input("Enter temperature: "))
unit = input("C or F: ").strip().upper()

# Call the function to convert the temperature
temperature_converter(unit)
