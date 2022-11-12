# create a variable with a list of items using tuple
tup_1 = ('sailfish', 'tuna', 'shark')
print(type(tup_1))
print(tup_1)
print()
# tuple with 1 item
tup_2 = ('grasshopper') # One item in a tuple without a comma is a sting
print(type(tup_2))
print()
tup_3 = ('grasshopper',)    # one item in a tuple SHOULD always end with a comma
print(type(tup_3))
print()

# create a tuple with multiple data types
print("Tuple with multiple data types as items")
tup_4 = (56, 'capricon', False, 'artic')
print(tup_4)
print(len(tup_4))
print(type(tup_4))
print()

# create a tuple with multiple items
print("List of some sharks in the ocean.")
tup_aux = ('mako shark', 'rugged tooth shark', 'blue shark', 'tiger shark', 'whale shark', 'whitetip shark', 'white shark', 'hammerhead shark')
print(tup_aux)
print(tup_aux[1:2])     # accessing tuples
print(tup_aux[1:3])
print(tup_aux[-2:-1])   #accessing tuples with negative indexing
print(len(tup_aux))

# # change tuple to list and add items
print()
print("Change tuple tup_aux tuple to list.")
tup_aux1 = list(tup_aux)    # use list method to change tup_aux to list
print(tup_aux1)
print(type(tup_aux))
print(type(tup_aux1))
print()

print("Append new item to tup_aux1")
tup_aux1.append('six gilled shark')     # append item to tup_aux1
print(tup_aux1)
print(len(tup_aux1))
tup_aux1.insert(2, 'lemon shark')
tup_aux1.insert(4, 'greenland shark')
print(tup_aux1)
print(len(tup_aux1))
tup_aux1.insert(5, 'bronze whaler shark')
print(tup_aux1)
print(len(tup_aux1))
tup_aux1.insert(5, 'bull shark')
tup_aux1.sort
print(tup_aux1)
print(len(tup_aux1))
print()

print("Change list tup_aux1 to tuple tup_aux2")
tup_aux2 = tuple(tup_aux1)  # create new tuple variable
print(tup_aux2)

# Joining Tuples
# add new tuple variable with 3 items

e5 = ('G65', 'A34', 'C87')
e6 = (78, 'bolts', 'chanins')

e7 = e5 + e6
print(e5)
print(e6)
print()
print("Add tuple e5 to tuple e6.")
print(e7)
print(len(e7))
print(type(e7))
print(e7[0])
print()
e8 = e7[2:5]
print(e8)