
#function with required parameter
def hello(name, age):
    print(f"Hello {name}, you are {age} years old!")

#we can add a default value which allows parameters to be optional (if none given default value is used)
def goodbye(name="user"):
    print("Goodbye!")


def fn_inputs():
    #pass multiple parameters into function
    hello("Cat", 7)

    #order IS IMPORTANMT!@!!
    hello(7, "Cat") #this outputs garbage

    #we can name the parameters, then order doesn't matter
    hello(age=7, name="Cat")

    #we don't need to specify name for goodbye()
    goodbye()
    # but we can
    goodbye("Dirk")

