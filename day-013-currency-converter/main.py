import tkinter as tk

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        conversion_rate = 1.2 if from_currency == 'USD' and to_currency == 'EUR' else 0.85 if from_currency == 'EUR' and to_currency == 'USD' else None
        if conversion_rate is None:
            result_label.config(text='Invalid currency pair')
        else:
            result = amount * conversion_rate
            result_label.config(text=f'Result: {result:.2f} {to_currency}')
    except ValueError:
        result_label.config(text='Please enter a valid number')

root = tk.Tk()
root.title('Currency Converter')

amount_label = tk.Label(root, text='Amount:')
amount_label.grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

from_currency_var = tk.StringVar(value='USD')
from_currency_menu = tk.OptionMenu(root, from_currency_var, 'USD', 'EUR')
from_currency_menu.grid(row=0, column=2)

result_label = tk.Label(root, text='')
result_label.grid(row=1, columnspan=3)

to_currency_var = tk.StringVar(value='EUR')
to_currency_menu = tk.OptionMenu(root, to_currency_var, 'USD', 'EUR')
to_currency_menu.grid(row=2, column=0)

convert_button = tk.Button(root, text='Convert', command=convert_currency)
convert_button.grid(row=2, column=1, columnspan=2)

root.mainloop()
