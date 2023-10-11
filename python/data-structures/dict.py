
my_dog = {"name":"Bingo", "age": 7000, "breed": "no thanks!"}

def dict_basics():
    #empty dictionary
    empty = {}
    #change a value or add a key value pair if key doesn't exist
    empty["name"] = 3
    print(empty) # now dictionaryu "empty" has a value
    empty.clear() #delete everything in dictionary
    print(empty) # empty is now empty again

def my_dog_dictionary():
    print(my_dog["name"]) #prints value 
    print(my_dog)
    #export dictionary elements:
    print(my_dog.keys()) #exports key elements
    print(my_dog.values()) #exports value elements
    print(list(my_dog.items())) #exports key/value pairs in tuple elements

    #what if we try to get a value not in dictionary?
    #my_dog["colour"] #this will cause a key error

    #test if colour is in my_dog - note only searches keys
    print("colour" in my_dog) # False
    print("name" in my_dog) #True

def dict_iteration():
    #iterate over dictionary

    for k in  my_dog: # will iterate over keys
        print(k) #prints out keys

    for k, v in my_dog.items():
        print(f"The value of {k} is {v}")

def stop_dict_errors():
    #to stop python crashing if no key exists use .get()
    print(my_dog.get("weight")) # returns None
    #We can make get return a default value if key doesn't exist
    print(my_dog.get("weight", "Unknown"))#returns Unknown
    print(my_dog.get("name", "Unknown"))#returns Bingo

for v in my_dog.values():
    print(v)

