class CurrencyConverter:

    # 245-300pm) looked at ovpn
    # 300 to 405pm) trip to bloomberg cafe + ate
    # (2/2/25)(Sun)(405-415pm, 423pm-425pm) finally done with this chapt

    rates = {  
        'EUR': 1.20,  # 1 EUR = 1.20 USD
        'JPY': 0.01   # 1 JPY = 0.01 USD
    } # Class attribute

    # TODO: Implement the static method `to_usd`
    @staticmethod
    def to_usd(amount: int, currency_name: str) -> int:
        bruh1 = CurrencyConverter.rates[currency_name] * amount
        return bruh1
    
    

print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")     # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")     # 1 USD
