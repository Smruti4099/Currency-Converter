import requests

def currency_converter(amount, from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    exchange_rate_data = response.json()
    exchange_rate = exchange_rate_data['rates'][to_currency]
    converted_amount = round(amount * exchange_rate, 2)
    return converted_amount

amount = float(input("Enter the amount: "))

from_currency = 'USD'
to_currency = 'EUR'
converted_amount = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

to_currency = 'INR'
converted_amount = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
