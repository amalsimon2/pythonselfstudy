import re

def check_password_strength(password):
	if len(password) < 8:
		return 'Weak: Password is too short'
	if not any(char.isdigit() for char in password):
		return 'Weak: No digits present'
	if not any(char.isupper() for char in password):
		return 'Weak: No uppercase letters present'
	if not any(char.islower() for char in password):
		return 'Weak: No lowercase letters present'
	if re.search('[!@#$%^&*(),.?":{}|<>]', password) is None:
		return 'Weak: No special characters present'
	else:
		return 'Strong: Password meets all criteria'

if __name__ == '__main__':
	try:
		password = input('Enter a password to check its strength: ')
		strength = check_password_strength(password)
		print(strength)
	except Exception as e:
		print(f'Error: {e}')
