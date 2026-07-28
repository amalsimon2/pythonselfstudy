def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi

if __name__ == '__main__':
	try:
		weight = float(input('Enter your weight in kilograms: '))
		height = float(input('Enter your height in meters: '))
		bmi = calculate_bmi(weight, height)
		print(f'Your BMI is {bmi:.2f}')
		if bmi < 18.5:
			print('Underweight')
		elif 18.5 <= bmi < 24.9:
			print('Normal weight')
		elif 25 <= bmi < 29.9:
			print('Overweight')
		else:
			print('Obesity')
	except ValueError:
		print('Please enter valid numerical values for weight and height.')
