#----------------------------------------------------------------------|
def reading_files():
    # to use a file, first you need to open it
    # just a file name assumes current folder
    f = open('shopping.txt')

    # print(f)
    # output: 
    # <_io.TextIOWrapper name='shopping.txt' mode='r' encoding='UTF-8'>
    # mode = "r" means open as read only

    data = f.read()
    # read() reads every line in the file as a single string
    # print(data)
    # output:
    # Milk
    # Bread
    # Coffee
    # Butter
    # Pizza

    # the literal string is
    # print(repr(data))
    # output: 'Milk\nBread\nCoffee\nButter\nPizza\n'


    #read only a certain number of charaters
    data1 = f.read(10) # this will read teh first 10
    data2 = f.read(10)# this will read the next 10
    print("read(10 output 1: ", data1)
    print("read(10 output 2: ", data2)

    data3 = f.readline() #will read one line at a time

    # Need to close a file after we have read it into a variable
    # this unlocks the file in the system and frees up resources
    f.close()

    # alternatively you can use a with / as statement to do an action on 
    # a file. This automatically closes the file once the block is 
    # concluded
    with open("shopping.txt") as f:
        data = f.readline()
        print("readline output: ", repr(data))


    # you can loop over a file 
    with open("shopping.txt") as f:
        for line in f:
            print(line.strip()) 
    # note str().strip() will remove whitespace characters from ends of string

    #you could put the file into a list loop for large files (line by line)
    shopping_list = []
    with open("shopping.txt") as f:
        for line in f:
            shopping_list.append(line.strip()) 

    #alternatively read the whole file then split it into a list
    with open("shopping.txt") as f:
        shopping_list = f.read()
        shopping_list = shopping_list.split("\n")

def writing_files():
    # need to open file as writeable - otherwise get error
    # this will overwrite everything in the write file
    with open('tv-shows.txt', "w") as f:
        # can only write one string at a time - need to add \n between lines
        f.write("The X-files\nFringe\n")
        f.write("The Witcher")

    shows = [
        "The X-files",
        "Fringe",
        "The Witcher"
    ]
    # write items in list joined together in a string with line breaks between:
    
    with open('tv-shows.txt', "w") as f:
        # f.write('\n'.join(shows))
        for i, s in enumerate(shows):
            f.write(f"{i+1}. {s}\n")

# we can open as append with the "a" arguement
    item = input("What shall I add to the shopping-list?")
    with open('shopping.txt', "a") as f:
        f.write(f"\n{item}")

#Main
writing_files()

