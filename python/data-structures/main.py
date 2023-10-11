#--------------------------------------------------|

import my_module
# don't need to declare path, python will 
# automatically search for .py files in the 
# following order
    #1. local directory
    #2. standard library
    #3. Global package cache

def other_import_options():
    pass
    #we can import multiple modules on one line
    import my_module, random

    # we can import specific symbols into the local
    # name space
    from my_module import foo, person
    # this means to use these they don't need to use
    # my_module.person or my_module.foo() - can just 
    # use person and foo()
    foo(person)
    # this means if functions / variables have the 
    # same name as one in this file, one will over-
    # ride the other 

    from my_module import foo as bar, person
    # using "as" will change the name of the function
    # imported. in the example above instead of 
    # foo(person) we will use:
    bar(person)


# now we can access the functions and variables 
# in my_module
my_module.foo(my_module.person)

# and we can pass new parameters into functions in my_module
my_module.foo({"name":"Matt", "Age":51})

# prints list of the modules, variables etc seclared 
# in current file. we can see my_module appears here
print(dir()) 

# this will show everything in my module
print(dir(my_module))


