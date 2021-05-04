#This is a guess the number game.
import random

print('Hello! What is your name?')
userName = input()

print('Well ' + userName + ", I'm thinking of a number between 1-20.")
secretNum = random.randint(1,20)

for guessesTaken in range(1, 7):
    print('Take a guess!')
    guess = int(input())

    if guess < secretNum:
        print("You're guess is too low.")
    elif guess > secretNum:
        print("You're guess is too high.")
    elif guess == secretNum:
        print("You got it! The number was " + str(secretNum) + "! Nice Job.")
        break

print('You took ' + str(guessesTaken) + ' guesses.')

