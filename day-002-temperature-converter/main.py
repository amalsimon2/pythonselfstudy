def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

try:
    temp = float(input('Enter temperature: '))
    scale = input('Enter scale (C for Celsius, F for Fahrenheit): ').upper()

    if scale == 'C':
        print(f'{temp} C is {celsius_to_fahrenheit(temp)} F')
    elif scale == 'F':
        print(f'{temp} F is {fahrenheit_to_celsius(temp)} C')
    else:
        print('Invalid scale. Please enter C or F.')
except ValueError:
    print('Please enter a valid number for temperature.')
