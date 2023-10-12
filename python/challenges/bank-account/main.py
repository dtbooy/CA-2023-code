#----------------------------------------------------------------------|
import bank


#tests
acc1 = bank.BankAccount('John Smith', 1000)
acc2 = bank.BankAccount('Mary Jones', 500)

match input(f""" 
        hello {acc1.account_name}, what would you like to do?
        [N]ew account
        Check [B]alance
        [W]ithdraw
        [T]ransfer money
        """).lower():
    #Create a new account
    case "n":
        new_name = input("Enter acount name: ")
        new_deposit = int(input("Enter intial deposit: "))
        acc3 = bank.BankAccount(new_name, new_deposit)
        print(acc3.__dict__)
    #check balance
    case "b":
        print(f"your account balance is: ${acc1.balance()}")
    #Withdraw
    case "w":
        acc1.withdraw(int(input("How much would you like to withdraw? $")))
        print(f"your new account balance is {acc1.balance()}")
    #Transfer 
    case "t":
        print("hi")
    case _:
        print("invalid selection")
      
# print(acc1.balance())    # 1000
# acc1.deposit(100)
# acc2.deposit(200)
# acc1.deposit(50)
# print(acc2.balance())    # 700
# print(acc1.balance())    # 1150
# print(acc1.account_name, acc1.balance())
# print(acc2.account_name, acc2.balance())
# print(acc1.transfer(acc2, 500))
# print(acc1.account_name, acc1.balance())
# print(acc2.account_name, acc2.balance())
# print(acc2.withdraw(400))
# print(acc2.account_name, acc2.balance())
# print(acc1.withdraw(4000))
# print(acc1.account_name, acc1.balance())
# print(acc1.transfer(acc2, 5000))
# print(acc1.account_name, acc1.balance())
# print(acc2.account_name, acc2.balance())
