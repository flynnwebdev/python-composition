# from person import Person

# p1 = Person(age=40, name='John')
# p2 = Person('Mary', 25)

# # p1.name = 'John'
# # p2.name = 'Mary'

# # p1.greet('Hello')
# # p2.greet('Goodbye')
# print(p1.age)

import rpg

aragorn = rpg.Character('Aragorn', 'Human', 100, 50)
galadriel = rpg.Mage('Galadriel', 'Elf', 120, 75, 200)
frodo = rpg.Burglar('Frodo', 'Hobbit', 50, 25)

galadriel.wallet.value = 10, 5, 2
aragorn.wallet.value = 20, 50, 80
frodo.wallet.value = 5, 25, 20
# # galadriel.gold = 10
# # galadriel.silver = 5
# # galadriel.copper = 2

chest = rpg.Chest(['longsword', 'iron helm'], 2, 50, 10)

print(galadriel.__dict__)
chest.loot(galadriel)
print(galadriel.__dict__)
print(galadriel.wallet)
print(chest.cash.__dict__)

galadriel.battle(frodo)
frodo.battle(aragorn)
galadriel.portal('Minas Tirith') # The beacons are lit!


# del galadriel.wallet.gold
# galadriel.wallet.add(10, 5, 1)
# galadriel.wallet.__gold = 'Hello'
# _, y, _ = galadriel.wallet.value
# print(y)
# galadriel.show_gold()

aragorn.wallet += 42
print(aragorn.wallet)
print(frodo.wallet)
