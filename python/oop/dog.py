# my_dog - {'name':'Ted', 'age':15, 'breed': 'Border Collie'}

class Dog:
    def __init__(self, _name, _age=1):
        self.name = _name #we can assign 
        self.age = _age # 
        self.state = "sleeping" # we can set a default atribute that cannot be changed by parameter 
        print("didthiswoirk")


    def greet(self) :
        print(f"Hello, {self.name}!")  
        # print(self)
#    pass


