# password = 'swordfish'

# if password == 'swordfish':
#         print('access granted')
# else:
#         print('access denied')
print('enter a name')
name = input()
print('enter your age')
age = input()

if int(age) < 12:
    print("Hi " + name + ", it's nice to meet you. You sure are young.")
elif int(age) > 12 & int(age) < 30:
    print("Wow! " + name + ", did you know you're in the prime of your life? Enjoy it!")
elif int(age) > 30:
    print("I hate to be the one to tell you this " + name + ", but it's all downhill from here.")
