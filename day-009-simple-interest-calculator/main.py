def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

try:
    principal = float(input('Enter principal amount: '))
    rate = float(input('Enter interest rate: '))
    time = float(input('Enter time in years: '))
    interest = calculate_simple_interest(principal, rate, time)
    print(f'Simple Interest: {interest:.2f}')
except ValueError:
    print('Invalid input. Please enter numeric values.')
