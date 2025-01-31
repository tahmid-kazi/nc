class Account:
    # (1/31/25)(1111-1122am)(Fri)
    def __init__(self, title: str, balance: int):
        self.title = title
        self._balance = balance # protected
    
    def display_balance(self) -> None:
        print("Balance: $" + str(self._balance))


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
