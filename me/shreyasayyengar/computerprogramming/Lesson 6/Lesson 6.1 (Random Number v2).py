# First we import the random library so that python knows to what we are talking about when we reference one of its components
# We need to define some inputs as an either an int or a string
# We get an input as a string for a name on line 18
# We are also getting an input for the number of guesses, the guesser wishes to have
# We define the guesses as tries to make it simple.
# The loop condition I have entered is relative to how many tries they want to have
# while guesses (another input) < tries
# Everytime the player inputs a number, it add 1 (+=1 ) to the final number of tries,
# You could also do this with a list, but its far less efficient
# The loop basically just takes the answer, analyses it and throws a print, depending on the input.

import random

number = random.randint(1, 10)

player_name = input("Hello, What's your name?\n\n")
number_of_guesses = 0

tries = int(input("Hello " + player_name + ". I am picking a number from 1 to 10. Your job is to try to guess it! How many guesses do you want to have?\n\n"))

print(f'Ok! You will have ' + str(tries) + ' to guess the number! Good luck.')

while number_of_guesses < tries:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, in 5 tries :( | The number was ' + str(number))
