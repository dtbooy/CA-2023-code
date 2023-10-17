#----------------------------------------------------------------------|
class BankAccount():
   
    #Initialise account with accountholder name and initial deposit
    def __init__(self, ac_details, deposit = 0):
        self.account_holder = Customer(ac_details)
        self.account_balance = deposit
        
    #balance() returns the current balance of the account
    def balance(self):
        return self.account_balance
    
    # deposit(): accepts an amount and deposits that into the account
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        else:
            self.account_balance += amount
        return amount

    # withdraw() accepts an amount and attempts to withdraw it. If 
    # there is enought to cover withdrawal remove from account_balance 
    # & return witdrawal amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        elif self.account_balance < amount:
            raise ValueError("Insufficient funds")
        else:
            self.account_balance -= amount
            return amount
        
    # transfer() accepts bankac object & amount, transfer if balance 
    # covers it, otherwise do nothing and return 0
    def transfer(self, to_account, amount):
        return to_account.deposit(self.withdraw(amount))
        

    # def valid_number_input(self, amount):

    #     else:
    #         return True
    
        # if not isinstance(amount, int) | isinstance(amount, float):
        #     #  if value is not an integer or a float raise a type error
        #     try:
        #         raise TypeError("Invalid input: Amount must be a number")
        #     except TypeError as message:
        #         print(message)

# Extend the BankAccount class from last lesson so that, instead 
# of a string name, it stores an instance of a Customer class that 
# stores the name, address and date of birth of the customer. Also 
# abstract Address into it's own class, storing the components of 
# an address as separate attributes.

class Customer:
    def __init__(self, ac_details):
        self.name = ac_details[0]
        self.address = ac_details[1]
        self.date_of_birth = ac_details[2]


class Address:
    def __init__(self, st_num, street, st_type, suburb, pcode):
        self.number = st_num
        self.street_name = street
        self.street_type = st_type
        self.suburb = suburb
        self.post_code = pcode

    def __str__(self):
        return f"{self.number} {self.street_name} {self.street_type}, {self.suburb}, {self.post_code}"
