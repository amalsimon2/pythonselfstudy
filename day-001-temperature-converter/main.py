def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

try:
    choice = input('Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ').upper()
    if choice == 'C':
        celsius = float(input('Enter temperature in Celsius: '))
        print(f'{celsius}°C is {celsius_to_fahrenheit(celsius)}°F')
    elif choice == 'F':
        fahrenheit = float(input('Enter temperature in Fahrenheit: '))
        print(f'{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C')
    else:
        print('Invalid input. Please enter C or F.')
except ValueError:
    print('Please enter a valid number.')
