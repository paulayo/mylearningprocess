#Creating a Bank Automated Teller Machine
import pdb

class Atm():

    def __init__(self,balance):
        self.balance = float(10,000)
        self.transaction_history = []

  
    def deposit(self,deposit_amount):
        self.deposit_amount += self.balance
        return self.deposit_amount


    def customer_pin(self):
        self.chance = 3
        self.password[:4] = ''
        while True:
            try:
                self.password = int(input("Please Enter your four digit pin:  "))
            except ValueError:
                print('Please Enter the correct password')
                self.chance -= 1
                print('You have two attempt left')
                continue
            else:
                break
    
    

customer1 = Atm()

print(customer1.deposit_amount(200))