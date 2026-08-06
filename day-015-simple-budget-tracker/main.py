import datetime

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
current_month = months[datetime.datetime.now().month - 1]
income = float(input(f'Enter income for {current_month}: '))
expenses = float(input(f'Enter expenses for {current_month}: '))
savings = income - expenses
if savings < 0:
    print(f'Warning: You are running a deficit of ${abs(savings)}')
elif savings == 0:
    print('Congratulations! Your budget is balanced.')
else:
    print(f'Great job! You saved ${savings} for {current_month}.')

print(f'Total income for {current_month}: ${income}')
print(f'Total expenses for {current_month}: ${expenses}')
