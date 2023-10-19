class House:
    def __init__(self, price):
        self.__price = price # dunder (__) makes atribute private



    @property #this lets you call the method as an attribute
    def price(self): #this lets you get price
        return float(self.__price) #require price to be a float
    
    @price.setter #to set a property setter to look like an attribute
    def price(self, price): # this lets you set price
        if price > 0: # make sure price is positive
            self.__price = price
        else:
            raise ValueError("price must be positive")


my_house = House(650000)

my_house.price = 500 #try to change price directly

print(my_house.price) # price hasn't changed