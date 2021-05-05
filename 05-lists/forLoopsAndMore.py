#lets talk for loops
#remember range object
range(4) # evaluates to range(0,4)
for i in range(4):
    print(i)

#is the same as this
for i in [0, 1, 2, 3]:
    print(i)

# you can also use the list function on the range
# this creates a list using the same numbers we were printing above
print(list(range(4)))
# lets make a list of even numbers up to 100
print(list(range(0, 100, 2)))
# one common python technique is to use the length of the list as the range number
officeSupplies = ['pen', 'staplers', 'binders']
for i in range(len(officeSupplies)):
    print('Index ' + str(i) + ' in supplies is: ' + officeSupplies[i])

# you can do multiple assignments as well
cat = ['black', 'timid', 'fat']
print(cat)
color, personality, size = cat
print(color)
print(personality)
print(size)
# we can also swap variables with a swapping operation
color, personality, size = 'orange', 'angry', 'skinny'
print(color)
print(personality)
print(size)
# another way to do this
a = 'AAA'
b = 'BBB'
a, b = b, a

# augmented assignment operators
spam = 42
print(spam)
# if we want to increment
spam = spam + 1
print(spam)
# or you can use math operators with an equal sign
spam += 1
print(spam)