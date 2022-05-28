from enum import Enum

class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False
        
        
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self,amount):
        if amount>=0:
            self.balance+=amount
            self.success = True
        else:
            self.success = False
        return self.success
        

    def withdraw(self,amount):
        
        if amount<=self.balance:
            self.balance-=amount
            self.success = True
        else:
            self.success = False
        return self.success
        



    def process(self, command):
        if command.action == command.action.DEPOSIT:
            command.success = self.deposit(command.amount)
        
        if command.action == command.action.WITHDRAW:
            command.success = self.withdraw(command.amount)
            
    # def __str__(self):
    #     return (f'Balance = {self.balance}')






        # todo

    