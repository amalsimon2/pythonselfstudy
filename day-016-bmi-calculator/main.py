def calculate_bmi(weight, height):
    return weight / (height ** 2)

try:
    weight = float(input('Enter your weight in kilograms: '))
    height = float(input('Enter your height in meters: '))
    bmi = calculate_bmi(weight, height)
    print(f'Your BMI is: {bmi:.2f}')
except ValueError:
    print('Please enter valid numerical values for weight and height.')
