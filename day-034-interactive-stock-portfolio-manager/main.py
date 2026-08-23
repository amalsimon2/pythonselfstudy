import os
import json
from datetime import datetime

def load_portfolio(filename='portfolio.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_portfolio(portfolio, filename='portfolio.json'):
    with open(filename, 'w') as file:
        json.dump(portfolio, file, indent=4)

def add_stock(portfolio, symbol, quantity):
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    save_portfolio(portfolio)

def remove_stock(portfolio, symbol, quantity):
    if symbol in portfolio:
        if portfolio[symbol] <= quantity:
            del portfolio[symbol]
        else:
            portfolio[symbol] -= quantity
        save_portfolio(portfolio)

def get_stock_value(symbol):
    try:
        response = os.popen(f'curl -s "https://api.iextrading.com/1.0/stock/{symbol}/quote"').read()
        data = json.loads(response)
        return data['latestPrice']
    except Exception as e:
        print(f'Error: {e}')
        return None

def calculate_total_value(portfolio):
    total_value = 0
    for symbol, quantity in portfolio.items():
        price = get_stock_value(symbol)
        if price is not None:
            total_value += price * quantity
    return total_value

def main():
    portfolio = load_portfolio()
    while True:
        print('\nPortfolio Manager Menu\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Exit\n')
        choice = input('Enter your choice: ')
        if choice == '1':
            symbol = input('Enter stock symbol: ').upper()
            quantity = int(input('Enter quantity: '))
            add_stock(portfolio, symbol, quantity)
        elif choice == '2':
            symbol = input('Enter stock symbol: ').upper()
            quantity = int(input('Enter quantity: '))
            remove_stock(portfolio, symbol, quantity)
        elif choice == '3':
            print('\nCurrent Portfolio:\n')
            for symbol, quantity in portfolio.items():
                price = get_stock_value(symbol)
                if price is not None:
                    print(f'{symbol}: {quantity} shares at ${price:.2f} each, total ${price * quantity:.2f}')
            print(f'\nTotal Portfolio Value: ${calculate_total_value(portfolio):.2f}\n')
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
