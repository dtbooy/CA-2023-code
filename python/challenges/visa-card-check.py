# Credit card numbers have a specific structure which varies depending on the vendor (eg. Visa, Mastercard, Amex, etc...)

# The structure of a valid Visa card number is:
# First digit is a 4
# Length is either 13 or 16 digits in total
# Digits 2-6 are the bank number
# The remaining digits (except the last digit) are the account number
# The last digit is a check digit

# Write a program to get a CC number from the user. If it is a Visa card, check the structure and display 
#if it is valid or invalid. If it is valid, extract and display the bank number and account number. 
#If it is not a Visa card, display an appropriate message


def visa_test(number):
    # test if card starts with a 4 and is either 13 or 16 digits
    if number[0] == "4" and (len(number) == 13 or len(number)==16):
        #Bank number is digits 2-6 (index 1 to 5 inclusive)
        print(f"Bank Number: {number[1:6]}")
        #Account number is remaining digits excluding last digit
        print(f"Account Number {number[6:-1]}")
    else:
        #print error message
        print("Invalid card")
        #Display results of validity tests
        print(f"first digit test = {number[0] == '4'} \nCard length test = {(len(number)==13 or len(number)==16)}")

#get number from user input - remove any spaces 
visa_test(input("enter card number:  ").replace(" ",""))
