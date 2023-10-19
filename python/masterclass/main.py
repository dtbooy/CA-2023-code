# def my_decorator(func):
#     def inner_function():
#         print("--------------------")
#         func()
#         print("--------------------")
    
#     return inner_function

# @my_decorator
# def my_function():
#     print("this is my function")

# my_function()


def my_decorator(func):
    def inner_function():
        get_name = input("Enter name: ")
        func(get_name)
    return inner_function

@my_decorator
def greet(name):
    print(f"Hello {name}")


greet()