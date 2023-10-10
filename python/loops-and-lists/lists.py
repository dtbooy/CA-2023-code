spam = ["cat", "dog", "bird"] # a list of strings
eggs = [12, 78, 100, 54, 42] # a list of integers
foo = ["Dirk", 37, 190] #can have non-homogenius datatypes in a list - not really reccomended

# a list of lists
tic_tac_toe = [
    ["","O",""],
    ["X","O",""],
    ["X","O",""],
]
def loops_with_lists():
    #ENUMERATE() gives an index for the for loop 
    for index, animal in enumerate(spam):
        print(f"{index+1}.{animal}")

def adding_to_lists():
    spam.append("kangaroo") #this will add a new element
    print(spam)
    print(spam.append(foo)) # this appends the list as a new element (does not extewend list)
    print(spam)
    print(spam.extend(eggs)) # this adds the lists together
    print(spam)
    eggs += foo #or we could add them together to extend them
    print (eggs)

def searching_lists():
    x = spam.index("dog")
    print(x)
    #x = spam.index("sadsadssagd") #this will cause an error
    #print(x)
    x = "dog" in spam
    print(x)
    x = "dasfdasgfasdg" in spam
    print(x)

def display_person(person):
    print(f"{person[0]} is {person[1]} years old and {person[2]}cm tall")
    # this is unclear what person[x] are
    # we could go:
    # name = person[0]
    # age = person[1]
    # height = person[3]
    # or do this in 1 line
    [name, age, height] = person # this is called destructuring
    print(f"{name} is {age} years old and {height}cm tall")

def list_functions():
    spam.insert(1, "kangaroo") # inserts an element ("kangaroo") at the index provided (1)
    print(spam)

    x= spam.pop() #removes the last element in list
    print(spam)
    print(x) #pop also returns the removed element

    spam.sort() #sorts list - acending order by default
    print(spam)
    spam.sort(reverse=True) #sorts list in decending order
    print(spam)
    spam.clear() #deletes everythign in list - packup your toys and go home
    print(spam)
list_functions()