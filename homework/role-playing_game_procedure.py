# the traditional way of creating the roles
# create hero 1
name = 'Elsa'
health = 50
magicPoints = 80
inventory = {'gold': 40, 'healing potion': 2, 'key': 1}

print('The hero %s has %s health.' % (name, health))

# method1 of creating monster 1
monsterName = 'Goblin'
monsterHealth = 20
monsterMagicPoints = 0
monsterInventory = {'gold': 12, 'dagger': 1}

# method2 of creating monster 2 and 3 with previous 1 in a way of list
monsterName = ['Goblin', 'Dragon', 'Goblin']
monsterHealth = [20, 300, 18]
monsterMagicPoints = [0, 200, 0]
monsterInventory = [{'gold': 12, 'dagger': 1}, {'gold': 890, 'magic amulet': 1}, {'gold': 15, 'dagger': 1}]

# method3 of creating monster 1,2,3 by dictionary
monsters = [{'name': 'Goblin', 'health': 20, 'magic points': 0, 'inventory': {'gold': 12, 'dagger': 1}},
            {'name': 'Dragon', 'health': 300, 'magic points': 200, 'inventory': {'gold': 890, 'magic amulet': 1}},
            {'name': 'Goblin', 'health': 18, 'magic points': 0, 'inventory': {'gold': 15, 'dagger': 1}}]

# delete a monster

def vanquishMonster(monsterIndex):
    del monsterName[monsterIndex]
    del monsterHealth[monsterIndex]
    del monsterMagicPoints[monsterIndex]

vanquishMonster(0)

