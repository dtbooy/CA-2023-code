#----------------------------------------------------------------------|
import bank


#Need to define a function to select accounts
acc1 = bank.BankAccount(["John Smith", "9 some pl", "21/06/1986"], 1000)
acc2 = bank.BankAccount(["Mary Jones", "2 Penny ln", "18/05/1984"], 500)
print(f"Hello {acc1.account_holder.name}, what would you like to do?")
while True:
    try:
        match input("""
        [N]ew account, 
        [B]alance check, 
        [D]eposit, 
        [W]ithdraw, 
        [T]ransfer money, 
        [Q]uit
    """
            ).lower():
            
            #Create a new account
            case "n" | "new account":
                # try:
                    acc_details = [input("Enter acountholder name: ")]
                    acc_details.append(input("Enter acountholder address: "))
                    acc_details.append(input("Enter acountholder date of birth: "))
                    new_deposit = int(input("Enter intial deposit: "))
                    acc3 = bank.BankAccount(acc_details, new_deposit)
                    print(acc3.__dict__)
                # except ValueError as error_msg:
                    # print(f"Error creating account: {error_msg}.")
            #check balance
            case "b" | "balance":
                print(f"your account balance is: ${acc1.balance()}")
            #deposit
            case "d" | "deposit":
                # try:
                    acc1.deposit(int(input("How much would you like to deposit? $")))
                    print(f"your new account balance is {acc1.balance()}")
                # except ValueError as error_msg:
                    # print(f"Error creating account: {error_msg}.")
            #Withdraw
            case "w" | "withdraw":
                acc1.withdraw(int(input("How much would you like to withdraw? $")))
                print(f"your new account balance is {acc1.balance()}")
            #Transfer 
            case "t" | "transfer" | "transfer money":
                # need to add a selection method to assign acc2
                # try:
                    acc1.transfer(acc2, int(input(f"How much would you like to transfer to {acc2.account_holder.name}?")))
                    print(f"your new account balance is {acc1.balance()}")
                # except ValueError:
                    # print("Error Transferring Amount: deposit must be a positive number.")
            #quit function        
            case "q" | "quit":
                print("Thank you for Banking!!! Goodbye!")
                break
            #invalid selection
            case _:
                print("invalid selection, please try again")
                continue
             
    except ValueError as err_msg:
        print(f"Error: {err_msg}.")
    input("Press Enter to continue:")
      
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
