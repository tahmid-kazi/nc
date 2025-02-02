class BankAccount: 

    # 2/2/25) Sun) 125-140pm)
    # sk left to 26F, doesn't know HDD vs SSD 

    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

# TODO: Create two accounts
# TODO: Print the information using the mentioned format

rb1 = BankAccount("Alice", 1000)
rb2 = BankAccount("Bob", 2000)

print(f"{rb1.name}'s balance: ${rb1.balance}")
print(f"{rb2.name}'s balance: ${rb2.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")