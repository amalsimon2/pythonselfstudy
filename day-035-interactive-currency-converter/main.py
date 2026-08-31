import forex_python.converter as fc

def currency_converter(amount, from_currency, to_currency):
    converter = fc.CurrencyRates()
    try:
        converted_amount = converter.convert(from_currency, to_currency, amount)
        return converted_amount
    except Exception as e:
        return str(e)

def main():
    print("Welcome to the Currency Converter")
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency code to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency code to convert to (e.g., EUR): ").upper()
    result = currency_converter(amount, from_currency, to_currency)
    if isinstance(result, float):
        print(f"{amount} {from_currency} is {result} {to_currency}")
    else:
        print(result)

if __name__ == '__main__':
    main()
