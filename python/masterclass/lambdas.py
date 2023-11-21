nums = [10, 14, 21, 50, 5, -6]
# create a new list with numbers in nums squared

def the_old_way():
    #we could do this:
    sq_nums =[]
    for num in nums:
        sq_nums.append(num **2)
    print(sq_nums)

#BuT tHEre mUsT bE a BEtTer wAy!!!
# --------------------- MAPPING --------------------|
def learning_about_maping():
    def square(value):
        return value **2

    def cube(value):
        return value ** 3

    sq_nums = list(map(square, nums))
    print(sq_nums)

#BuT WAiT tHerEs moRe!!!
# --------------------- Lambda --------------------|
def learning_about_lambda():
    sq_nums = list(map(lambda name_for_variable: name_for_variable ** 2, nums))

    even_numbers = list(filter(lambda num: num %2 == 0, nums))
    # Filter iterates through list and applies True/False function; 
    # elements resulting in True are added to the output list

    print(sq_nums)
    print(even_numbers)

    #you can store lambdas in functions
    square = lambda x: x **2
    print(square(10))

    #list comprehension - alternative to map & filter: 
    #sq_nums = list(map(lambda name_for_variable: name_for_variable ** 2, nums))
    # jsust do
    square_nums = [num ** 2 for num in nums]
    # can even add a filter
    square_nums2 = [num ** 2 for num in nums if num % 2 ==0]

# --------------------- Sorting --------------------|

def learning_about_sorting():
    sorted_values = sorted(nums, reverse = True)
    print(sorted_values)


    employees = [
        {"name": "John", "age" : 32 },
        {"name": "Mary", "age" : 27 },
        {"name": "Bob", "age" : 40 },
        ]
    sorted_employee = sorted(employees, key=lambda x: x["name"], reverse=True) 
    # in lambda [x] is list item (in this case a dictionary) so function is dict[key]:
    print(sorted_employee)
    oldest_employee = max(employees, key=lambda x: x["age"]) 
    print(oldest_employee)

def learning_about_list_comprehension():
    #list comprehension - alternative to map & filter: 
    #sq_nums = list(map(lambda name_for_variable: name_for_variable ** 2, nums))
    # jsust do
    square_nums = [num ** 2 for num in nums]
    # can even add a filter
    square_nums2 = [num ** 2 for num in nums if num % 2 ==0]

    students = [
        {"name": "Harry", "house" : "Gryffindor" },
        {"name": "Ron", "house" : "Gryffindor" },
        {"name": "Herman", "house" : "Gryffindor" },
        {"name": "Drake", "house" : "Slytherin" },
        ]
    names = [s["name"] for s in students if s["house"] == "Gryffindor"]
    print(students)
    print(names)

#main 
# learning_about_maping()
# learning_about_lambda()
# learning_about_sorting()
learning_about_list_comprehension()