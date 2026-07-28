import os

# Function to clear the screen
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
	return (celsius * 9/5) + 32

# Function to convert temperature from Celsius to Kelvin
def celsius_to_kelvin(celsius):
	return celsius + 273.15

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5/9

# Function to convert temperature from Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
	celsius = fahrenheit_to_celsius(fahrenheit)
	return celsius_to_kelvin(celsius)

# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(kelvin):
	return kelvin - 273.15

# Function to convert temperature from Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
	celsius = kelvin_to_celsius(kelvin)
	return celsius_to_fahrenheit(celsius)

# Main function to handle user input and display results
def main():
	while True:
		clear_screen()
		print("Temperature Converter")
		print("1. Celsius to Fahrenheit")
		print("2. Celsius to Kelvin")
		print("3. Fahrenheit to Celsius")
		print("4. Fahrenheit to Kelvin")
		print("5. Kelvin to Celsius")
		print("6. Kelvin to Fahrenheit")
		print("7. Exit")
		choice = input("Enter your choice (1-7): ")

		if choice == '1':
			celsius = float(input("Enter temperature in Celsius: "))
			fahrenheit = celsius_to_fahrenheit(celsius)
			print(f"{celsius}°C is {fahrenheit}°F")
			input("Press Enter to continue...")
		elif choice == '2':
			celsius = float(input("Enter temperature in Celsius: "))
			kelvin = celsius_to_kelvin(celsius)
			print(f"{celsius}°C is {kelvin}K")
			input("Press Enter to continue...")
		elif choice == '3':
			fahrenheit = float(input("Enter temperature in Fahrenheit: "))
			celsius = fahrenheit_to_celsius(fahrenheit)
			print(f"{fahrenheit}°F is {celsius}°C")
			input("Press Enter to continue...")
		elif choice == '4':
			fahrenheit = float(input("Enter temperature in Fahrenheit: "))
			kelvin = fahrenheit_to_kelvin(fahrenheit)
			print(f"{fahrenheit}°F is {kelvin}K")
			input("Press Enter to continue...")
		elif choice == '5':
			kelvin = float(input("Enter temperature in Kelvin: "))
			celsius = kelvin_to_celsius(kelvin)
			print(f"{kelvin}K is {celsius}°C")
			input("Press Enter to continue...")
		elif choice == '6':
			kelvin = float(input("Enter temperature in Kelvin: "))
			fahrenheit = kelvin_to_fahrenheit(kelvin)
			print(f"{kelvin}K is {fahrenheit}°F")
			input("Press Enter to continue...")
		elif choice == '7':
			break
		else:
			print("Invalid choice. Please try again.")
			input("Press Enter to continue...")

if __name__ == '__main__':
	main()