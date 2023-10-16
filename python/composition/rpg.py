#----------------------------------------------------------------------|
class Character():
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.copper = 0
        self.inv = Inventory([], 0, 0, 0)




class Chest():
    def __init__(self, items, gold, silver, copper):
        self.inv = Inventory(items, gold, silver, copper)
        
class Inventory():
    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.set_currency(gold, silver, copper) #delegation

    def transfer(self, to_inv):
        # Add items from self to to_inv
        to_inv.items.extend(self.items)
        # Delete items from self
        self.items = []
        # Add self copper to to_inv copper
        to_inv.copper += self.copper
        # Delete self copper
        self.copper = 0


    # This is a "Setter" - setters set attribute values
    def set_currency(self, gold,silver,copper):
        self.copper = gold *10000 + silver *100 + copper


    # A Getter method returns the value of atrributes - returns the values needed in the format needed
    def get_currency(self):
        gold = self.copper // 10000
        silver = (self.copper % 10000) // 100
        copper = self.copper % 100
        return (gold, silver, copper)


        
