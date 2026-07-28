def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

try:
    temp = float(input("Enter temperature: "))
    scale = input("Enter scale (C for Celsius, F for Fahrenheit): ").upper()
    if scale == 'C':
        result = celsius_to_fahrenheit(temp)
        print(f"{temp} C is {result} F")
    elif scale == 'F':
        result = fahrenheit_to_celsius(temp)
        print(f"{temp} F is {result} C")
    else:
        print("Invalid scale. Please enter C or F.")
except ValueError:
    print("Invalid input. Please enter a number.")
