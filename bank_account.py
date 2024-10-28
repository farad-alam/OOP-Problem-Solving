# 1. Building a Simple Banking System
# Create a BankAccount class with properties like account_number, balance, and owner_name.
# Add methods for deposit(amount), withdraw(amount), and display_balance().
# Ensure that withdrawals cannot exceed the current balance, and handle cases for insufficient funds.

import hashlib

class BankAccount:
    bank_name = "Green Bank LTD."
    def __init__(self, account_number, balance, owner_name, password):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.__password = self.__hash_password(password)
        print(self.__welcome())

    def __hash_password(self, password):
        return hashlib.sha256(str(password).encode()).hexdigest()

    
    def __welcome(self):
        '''
        welcome the user when created a account
        
        '''
        return f"Hi, {self.owner_name}. You Account successfully created"
    
    def chnage_password(self, current_pass, new_pass):
        '''
        Chnage user password with validation
        '''
        if self.__hash_password(current_pass) == self.__password:
            self.__password = self.__hash_password(new_pass)
            return f"Your password successfully reset!!!"
        else:
            return f"Your provided current password did not match"


    # TRANSITION METHODS
    def display_balance(self):
        '''
        Display the current balance
        '''
        print(self.__password)
        return f"Current balance: ${self.balance}"
    

    def deposit(self, deposit_amaount):
        '''
        Deposit amount when the amount it greater than 0
        '''
        if deposit_amaount > 0:
            self.balance += deposit_amaount
            return f"Successfully Deposit {deposit_amaount}$"
        else:
            # raise ValueError()
            return f"You can not deposit 0$"
        
    def withdraw(self, withdraw_amaount):
        '''
        withdrawl happned when the withdrawl amaount is less than the current balance and greater than 0
        '''
        if withdraw_amaount < self.balance and withdraw_amaount > 0:
            self.balance -= withdraw_amaount
            return f"Successfully withdrawl {withdraw_amaount}"
        else:
            return f"You can not withdrawl more than your current balence, current balance {self.balance}"
        
acc1 = BankAccount('2345', 3000, 'Farad Alam', 2090)

print(acc1.bank_name)
print(acc1.display_balance())
print(acc1.deposit(0))
print(acc1.display_balance())
print(acc1.withdraw(5000))
print(acc1.display_balance())
print(acc1.chnage_password(2090 ,5678))

print(acc1.chnage_password(2090 ,5678))



            
            

