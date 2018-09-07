#Creating a Bank Automated Teller Machine
import pdb

class Atm():

    def __init__(self):
        self.balance = float()
        self.transaction_history = []
        self.password = ''

    def  __str__(self):
        return f'Your balance is #{self.balance}'

    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        return self.balance


    def customer_pin(self):
        chance = 3
        password = 1234
        while self.password != password:
            try:
                self.password = int(input("Please Enter your four digit pin:  "))
            except ValueError:
                print('Please Enter the correct password')
                chance -= 1
                print('You have two attempt left')
                continue

            else:
                return f'Your password is correct'


customer1 = Atm()
print(customer1.deposit(111))
