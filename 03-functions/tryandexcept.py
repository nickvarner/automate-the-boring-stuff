# def div42by(divideBy):
#     return 42 / divideBy

# print(div42by(2))
# print(div42by(12))
# #error is thrown when divided by 0, which results in the program ending early
# print(div42by(0))
# print(div42by(1))

#now lets handle the error with a try and except statement

def div42by(divideBy):
    try:
        return 42 / divideBy
        #not required to name the error like we did below with 'ZeroDivisionError'
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
#error is thrown when divided by 0, which results in the program ending early
print(div42by(0))
print(div42by(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print("That's not that many cats.")
except:
    print('You must enter a number.')