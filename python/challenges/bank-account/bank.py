#----------------------------------------------------------------------|
class BankAccount():
   
    #Initialise account with accountholder name and initial deposit
    def __init__(self, _name, _deposit):
        self.account_name = _name
        self.account_balance = _deposit
        
    #balance() returns the current balance of the account
    def balance(self):
        return self.account_balance
    
    # deposit(): accepts an amount and deposits that into the account
    def deposit(self, amount):
        self.account_balance += amount

    # withdraw() accepts an amount and attempts to withdraw it. If 
    # there is enought to cover withdrawal remove from account_balance 
    # & return witdrawal amount
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return amount
        return 0
    
    # transfer() accepts bankac object & amount, transfer if balance 
    # covers it, otherwise do nothing and return 0
    def transfer(self, to_account, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            to_account.account_balance += amount
            return amount
        return 0
