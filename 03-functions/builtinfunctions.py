#theres built in modules to python, just need to import them and you'll be able to use built in functions that come with python

#random number module, requires you type random in front
import sys
import random
import pyperclip
#doesn't require the random. in front, but not recommended
# from random import *

#returns a random integer between 1 and 100
random.randint(1, 100)
# stops code from running
# sys.exit()
# pyperclip gives you access to the clipboard
pyperclip.copy('hello world')
pyperclip.paste()