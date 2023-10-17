#----------------------------------------------------------------------|
class Character():
    def __init__(self, name, race, health, attack):
        self.name = name
        self.race = race
        self.copper = 0
        self.inv = Inventory([], 0, 0, 0)
        self.attack = attack
        self.health = health

    def battle(self, other):
        print(f"{self.name} attacks {other.name}")
        # self.health -= other.attack
        # other.health -= self.attack
        # if self.health <= 0:
        #     print(f"{self.name} was killed by {other.name}")

class Ranger(Character):
    def battle(self, other):
        print(f"{self.name} throws a sword at {other.name}")

class Thief(Character):
    def battle(self, other):
        print(f"{self.name} stabs {other.name} like a beardless wuss")

class Mage(Character):
    def __init__(self, name, race, health, attack):
        # super Class 
        super().__init__(name, race, health, attack)
        self.mana = 100

    def battle(self, other):
        print(f"{self.name} attacks {other.name}")
        mana -= 20

class Wizard(Character):
    def battle(self, other):
        print(f"{self.name} blasts {other.name}")



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


    # A Getter method returns the value of atrributes - returns the 
    # values needed in the format needed
    def get_currency(self):
        gold = self.copper // 10000
        silver = (self.copper % 10000) // 100
        copper = self.copper % 100
        return (gold, silver, copper)


        
