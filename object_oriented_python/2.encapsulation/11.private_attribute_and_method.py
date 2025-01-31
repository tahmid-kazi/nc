class PasswordManager:
    
    # (1/31/25)(Fri)(1127-1136am)
    def __init__(self, password: str):
        self.__password = password # private attribute
    
    # TODO: Implement the verify_password method
    def verify_password(self, input_pwd: str):
        return self.__password == input_pwd

# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
