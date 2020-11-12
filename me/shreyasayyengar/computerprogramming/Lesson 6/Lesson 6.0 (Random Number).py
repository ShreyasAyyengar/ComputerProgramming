# First we import the random library so that python knows to what we are talking about when we reference one of its components
#
# We are making a new variable
# ble called c_answer which means (correct answer)
# We are also making a new input (which we define as (int)) which creates a variable called answer
# If the input is equal (==) to the answer, then we close the program with a print and with exit code {0}
# If the input is not equal to the c_answer, rerun the program with a denial with a print



from random import *

c_answer = randint(1, 2)

answer = int(input("Please guess the number\n\n"))

if answer == c_answer:
    print("Wow! Well done!")

while answer != c_answer:

    print("Wrong! Try Again")

    answer = int(input("Please guess the number\n\n"))