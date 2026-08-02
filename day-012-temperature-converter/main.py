def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def celsius_to_kelvin(c): return c + 273.15
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k): return k - 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32
try:
    temp = float(input("Enter temperature: "))
    scale = input("Enter scale (C, F, K): ").upper()
    if scale == 'C':
        print(f"{temp} C is {celsius_to_fahrenheit(temp)} F and {celsius_to_kelvin(temp)} K")
    elif scale == 'F':
        print(f"{temp} F is {fahrenheit_to_celsius(temp)} C and {fahrenheit_to_kelvin(temp)} K")
    elif scale == 'K':
        print(f"{temp} K is {kelvin_to_celsius(temp)} C and {kelvin_to_fahrenheit(temp)} F")
    else:
        print("Invalid scale")
except ValueError:
    print("Please enter a valid number")
