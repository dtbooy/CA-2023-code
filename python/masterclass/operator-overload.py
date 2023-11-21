from typeguard import typechecked
#imports type hint valifation - will raise error if wrong type is used vs type hints

class Point:
    @typechecked 
    # typechecked will check  this block of code for typehint validation
    def __init__(self, x: int, y: int):  #int in this is type
        self.x = x
        self.y = y

    #define what the + operator does with the class
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y) # print (3, 5)
        return 

    #can define numberous operators ==, **, +, -, 

    #returns programmer friendly string format
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    #this returns what prints when you print object - user friendly return
    def __str__(self) ->str:
        return str((self.x, self.y))


p1 = Point(1,2)
p2 = Point(2,3)

#now we can add Points together!!
print((p1+p2))

# even += works!!!
p1 +=p2
print(p1.__dict__)

print(p1 == p2)
