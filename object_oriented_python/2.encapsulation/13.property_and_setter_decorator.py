class BankAccount:
    
    # (1/31/25)(119-138pm)(Fri)
    def __init__(self, balance: int): 
        self.__balance = balance # Don't modify this line
    
    # Getter
    @property  
    def balance(self) -> int: # TODO: Convert this method to use the @property decorator
        return self.__balance
    
    # Setter
    @balance.setter
    def balance(self, value: int) -> None: # TODO: Convert this method to use the @property decorator
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative!")


# Don't modify the code below this line
account = BankAccount(1000)
print(account.balance)
account.balance = -100
