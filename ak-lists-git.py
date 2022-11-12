# # create a variable fruit with a list of fruits
fruits = ['apple', 'banana', 'orange']
print(fruits)
print(len(fruits))  # check how many items are in fruits
print()

fruits.append('grapes') # add grapes to the list of fruits
print(fruits)
print(len(fruits))  # check how many items are in fruits
print()

fruits.insert(2, 'lemon')   # add 
print(fruits)
print(len(fruits))  # check how many items are in fruits
print()

print(type(fruits))     # check data type for fruits
fruits_tuple = tuple(fruits)    # convert fruits to a tuple
print(fruits_tuple)
print(type(fruits_tuple))   # check data type fruits_tuple
print()

print(fruits)
fruits_sort = fruits.sort(reverse=False)    # sort fruits decending
print(fruits)
print()

print(fruits)
fruits_sort = fruits.sort(reverse=True) # sort fruits ascending
print(fruits)
print()

print(fruits)
print(fruits[0])
print(fruits[4])

# variable list of verbs
rse = ['make', 'take', 'run', 'taste', 'eat', 'walk', 'climb', 'drive', 'wade']
print(rse)
print()

# get index on rse with enumerate
rse_idx = enumerate(rse)
print(list(rse_idx))

rse[-1] = ['call']  # change the last word to call
print(rse)

rse.pop(-1) # remove last verb from list
print(rse)
print()

rse.append('call')  # add call to end of list
print(rse)

rse[-1] = 'break'   # change last work to break
print(rse)

# # create new variable with list of names
cac = ['Max', 'Tom', 'Angela', 'May', 'Andrea']
rse.extend(cac)     # use extend to add cac list to rse list
print(rse)
rse_idx = enumerate(rse)
print(list(rse_idx))

print(rse[0], rse[2])     # print multiple elements in a list

# add a variable with a list within a list
aca_1 = ['book', 'town', 'car', 'shirt']
aca_2 = ['abide', 'tommorow', 'April', 'trains', 'airport']
print(aca_1)
print(len(aca_1))
print(aca_2)
print(len(aca_2))
print()
aca_3 = ['mountain', 'river']   # add new variable to see how to have list within a list
print(len(aca_3))
print(type(aca_3))
print(aca_3)
print()
aca_3.append(aca_1)
print(aca_3)
aca_3 = aca_1 + aca_2
print(len(aca_3))
print(aca_3)
print("Adding aca_1 variable to aca_3 variable!")   # How to add comment to actual output
aca_3.append(aca_1) 
print(len(aca_3))
print(aca_3)
print()
print("Adding aca_2 variable to aca_3 variable!") 
aca_3.append(aca_2) # add aca_2 variable to aca_3
print(len(aca_3))
print(aca_3)
print(type(aca_3))
print()
print(aca_3[2])     # trying to access list 
print(aca_3[2][2])
print(aca_3[2][2][1])

aca3_idx2 = aca_3.index(['book', 'town', 'car', 'shirt'])   # trying to access an index
print(aca3_idx2)

# Trying to print elemnts in a list
# add variable with list of items
a4 = ['forest', 'rivers', 'lakes']
print(a4)
print(a4[0])
print(a4[0], a4[1])
a5 = ['boats', 'ships', 'trawlers']
print(a5)
a4.append(a5)
print(len(a4))
print(a4)
print(a4[3][0])
print(a4)

# add multiple elements to list
a4.extend(['tug boat', 'catapilar'])
print(a4)

# change elenent in list variable
a4[2] = 'streams'   # change rivers to streams in a4 variable
print(a4)
print("Add lakes to a4 variable.")
a4.append('lakes')
print(a4)
print("Add 'oil tanker' to second position in variable a4.")
a4.insert(1, 'oil tanker')
print(a4)
a4.remove('oil tanker')
print(a4)
print()
a4[3].insert(1, 'oil tanker')
print(a4)
print()
print("Change variable a4 to a tuple.")
a6 = tuple(a4)
print(a4)
print(type(a4))
print(len(a4))
print()
print(a6)
print(type(a6))
print(len(a6))