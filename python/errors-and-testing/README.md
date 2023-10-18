# Errors and Testing

Consider the following code
```py
n = int(input("Enter a numerator: "))
d = int(input("Enter a denominator: "))

q = n / d # exception was 

print(q)
```

If user inputs 0 for d, this will raise a ZeroDivisionError exception and stop the program
to catch an exception use try: /except


# Testing

write the acceptance criteria, then build the software until the test passes

keepss code dry, keeps the code focused on passing the test
reduces the temptation to add extras to functions

Convention for test file nameng:
test_modulename.py

## Pytest
run pytest in the terminal from the project folder
will check for test functions defined by the prefix ```test_``` eg:
```def test_foo():```

in test functions we assert something is True