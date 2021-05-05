# lists are to python what arrays are to javascript
# index of lists also work the same as arrays
animalList = [['cat', 'bat', 'rat'], 'lizard', 'snake', 'rhino']

# will be the first list inside the list
print(animalList[0]) 
#evaluates to the nested array, the first array in the array and the third index of that list so rat
print(animalList[0][2]) 
#you can use negative integers and it will work its way backward
print(animalList[-1]) # will evaluate to rhino (doesn't start at 0, like it does in the beginning)
#what if we want cat?, first index [0] and first index of that list [0]
print('The ' + animalList[0][0] + ' hates water.')
# you can use a colon to slice the list, which will create a list up from one index up to another one
reptiles = animalList[1:3]
print(reptiles)
# returns lizard and snake
# if you want you can leave off the first or second argument and they default to the beginning for the first one and the end for the last one
lastThree = animalList[1:]
print(lastThree)
# if you want to delete values from a list, use the del statement
# let's say we want to delete the rhino from the lastThree variable
print("lets delete rhino because it doesn't match our other two animals")
del lastThree[2]
print(lastThree)
# the len command also works with lists
print(len(reptiles))
# the plus operator that concatenates also works with lists along with math operators
moreAnimals = ['monkey', 'ape', 'orangutan'] + ['giraffe', 'cheetah', 'wildebeast']
print(moreAnimals)

# there's also a list function, which will turn things into lists, just like turning integers with int() and string with str()
print(list('Hello'))

#you can use the in operator to see if a value is in the list or the not in and it will return a boolean value
print('hey' in ['hi', 'hello', 'whats up', 'hey'])
print('howdy' in ['hi', 'hello', 'whats up', 'hey'])
print('hey' not in ['hi', 'hello', 'whats up', 'hey'])
print('howdy' not in ['hi', 'hello', 'whats up', 'hey'])