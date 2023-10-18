class NegativeNumberError(Exception):
    pass


q=0

while not q:
    try:
        n = int(input("Enter a numerator: "))
        d = int(input("Enter a denominator: "))

        #Raise an error if values are negative
        if n < 0 or d < 0:
            raise NegativeNumberError()


        q = n / d

        print(q)

    # Catch ZeroDivision errors
    except ZeroDivisionError:
        print("Denominator cannot be Zero!")

    # catch ValueError
    except ValueError as e:
        print(e)
        print("Inputs must be integers!")

    except NegativeNumberError:
        print("Inputs must be positive integers!")
        

    # catch any other errors - This must be last or will trigger before 
    # other  other excepts
    except Exception as e: 
        # "as e" recieves the Exception error msg as a string
        print(f"Something went wrong: {e}")