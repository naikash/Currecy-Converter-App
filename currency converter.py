#Overview:
#A Currency Converter application that fetches real-time exchange rates and converts amounts between different currencies using the ExchangeRate-API.
#Features:
#Fetch real-time exchange rates
#Convert amounts between different currencies
#User-friendly command-line interface

#Here we Go...

import requests
# currency converter.py
API_KEY = '00e8a56c7c91f22b8723fb2b'  
BASE_URL = 'https://v6.exchangerate-api.com/v6/'

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"{BASE_URL}{api_key}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rate']
    else:
        return None

def main():
    print("Currency Converter")
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., INR): ").upper()
    amount = float(input(f"Enter the amount in {base_currency}: "))

    exchange_rate = get_exchange_rate(API_KEY, base_currency, target_currency)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Failed to retrieve exchange rate. Please check your currencies or try again later.")

if __name__ == "__main__":
    main()
