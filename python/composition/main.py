#----------------------------------------------------------------------|
import rpg

aragorn = rpg.Ranger("Aragorn", "human", 100, 15)
galadriel = rpg.Mage("Galadriel", "Elf", 100, 20)
frodo = rpg.Thief("Frodo", "Hobbit", 5, 1)
sauruman = rpg.Wizard("Sauroman", "Maiar", 500, 50)

frodo.inv.set_currency(5, 10, 900 )

chest = rpg.Chest(["longsword", 'iron helm'], 2, 25, 50)

# print(aragorn.__dict__)
# print(galadriel.__dict__)
# print(frodo.__dict__)
# print(chest.inv.__dict__)

# print(chest.inv.__dict__)
# print(frodo.inv.__dict__)
# chest.inv.transfer(frodo.inv)
# print(chest.inv.__dict__)
# print(frodo.inv.__dict__)

frodo.battle(aragorn)