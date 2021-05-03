# def hello():
#     print('howdy')
#     print('doody!')
#     print('hello there.')

def hello(name):
    print ('Hello ' + name)

hello('Nick')
hello('Alice')
hello('Bob')

def plusOne(num):
    return num + 1

newNum1 = plusOne(2)
newNum2 = plusOne(5)

print(newNum1)
print(newNum2)

print('hello', end='')
print('world')