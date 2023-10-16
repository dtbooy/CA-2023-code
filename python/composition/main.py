#----------------------------------------------------------------------|
import rpg

aragorn = rpg.Character("Aragorn", "human")
galadriel = rpg.Character("Galadriel", "Elf")
frodo = rpg.Character("Frodo", "Hobbit")

frodo.inv.set_currency(5, 10, 900 )

chest = rpg.Chest(["longsword", 'iron helm'], 2, 25, 50)

# print(aragorn.__dict__)
# print(galadriel.__dict__)
# print(frodo.__dict__)
# print(chest.inv.__dict__)

print(chest.inv.__dict__)
print(frodo.inv.__dict__)
chest.inv.transfer(frodo.inv)
print(chest.inv.__dict__)
print(frodo.inv.__dict__)
