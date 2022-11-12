# create set variable with items
ak_set = {'shops', 'ports', 'church', True, 'hotels', 76}
print(ak_set)
print(type(ak_set))
print()

# create variable with list of planets in solar system
ram_1 = {'mars', 'venus', 'earth', 'jupiter', 'mecury', 'mars'}     # duplicate of mars added for testing
print(len(ram_1))
print(ram_1)
print()
print("Add planet Saturn to ram_1")
print(ram_1)
print(len(ram_1))
# use add() method to add items to a set
ram_1.add('Saturn'.lower())     # The lower() methond used to change Saturn to saturn
print(ram_1)
print(len(ram_1))
print()
# create new variable with all the 9 planets in solar system
ssm = {'mecury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'urainus', 'neptune', 'pluto'}
print(len(ssm))
print(ssm)
print()
print("Add items from set ssm to set ram_1 with update() method.")
print(ram_1)
print(ssm)
print()
print("Use update() method")
ram_1.update(ssm)
print(ram_1)
print(len(ram_1))
print()
# Add create list variable of galaxies
print("List of know galaxies in universe")
glx = ['milky way', 'sambrero', 'andromeda', 'black eye', 'coment', 'tadpole']
print(glx)
print(len(glx))
print(type(glx))
print(ram_1)
print()
ram_1.update(glx)
print(ram_1)
print(len(ram_1))
print(type(ram_1))
print()

# Use remove() method to remove item from set
# create new variable with ramdom items
setaux = {'planes', 'trains', 'ships', 'fish', 'helicopter', 'tanks'}
print(setaux)
print(len(setaux))
setaux.remove('fish')
print()
print(setaux)
print(len(setaux))
ret1 = {'lost', 'at', 'sea', 'air'}
print(ret1)
print()
print("Join two set with union() method.")
ter1 = setaux.union(ret1)      #Use union method to add sets
print(ter1)
print(len(ter1))


# Use inetrsection_update method
b4 = {'white', 'Olney', 'yellow', 'tree'}
b5 = {'red', 'blue', 'tree', 'Olney'}
print(b4)
print(b5)
print()
b4.intersection_update(b5)  # Use intersection_update method to keep items available in both sets
print(b4)
print(len(b4))

# # Use intersection() method needs new set of common items in two sets
b6 = {'pencil', 'pen', 'erasr'}
b7 = {'teacher', 'principal', 'pen'}
print(b6)
print(b7)
print()
# # use inetrsection method to get common items with new variable
b8 = b6.intersection(b7)
print(b8)
print()

# use symmetric_difference_update() to NOT common in b6 and b7
v1 = {'crabs', 'lobsters', 'coral', 'octopus'}
v2 = {'house', 'crabs', 'fish', 'pantry'}
print(v1)
print(len(v1))
print(v2)
print(len(v2))
print()
v1.symmetric_difference_update(v2)      # symmetric_difference_update method to retun uncommon items in v1 and v2
print(v1)
print(len(v1))

