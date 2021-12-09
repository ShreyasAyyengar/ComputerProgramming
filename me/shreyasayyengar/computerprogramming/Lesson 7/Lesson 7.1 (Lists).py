# FIRST WE NEED TO IMPORT ALL THE LIBRARIES THAT WE PLAN TO USE
# FOR OUR PROJECT, HERE I AM THE random LIBRARY IMPORTED
# SO THAT PYTHON KNOWS TO USE THAT LIBRARY WHEN WE USE ITS METHODS

from random import *


# FOR THIS PROJECT LISTS ARE ESSENTIAL. OUR FIRST LIST [] IS A LIST OF TOPPINGS THAT
# ARE APPENDED IN THE STRING FORMAT. TAKE NOTE OF THE ORDER OF THE ENTRIES
toppings = ['plain cheese', 'peperoni', 'olive', 'mushrooms', 'garlic']


# THIS IS ANOTHER SET OF NUMBERS (int) WHICH DEFINE THE PRICE OF THE CORRESPONDING
# TOPPING ABOVE, THESE LISTS ARE DEFINED AS INTEGERS.
price = [10 , 15, 20, 13, 14]


# THIS IS DATA HOLDER WHICH ACTS AS A COUNTER FOR EACH TOPPING AND PRICE.
counter = 0  # Lists(Int)

# THIS DONE VARIABLE ACTS AS A FINISHING NUMBER TO YOUR ORDER. SINCE
# WE CANNOT SAY, "we are done" OR "I am finished" DURING THE ORDER
# PROCESS WE NEED TO HAVE A WAY TO SAY THAT WE ARE FINISHED. HERE
# THE NUMBER CALLED {done} IS ALL THE NUMBERS OF TOPPINGS +1
# FOR EX. Mushrooms, Olives, Garlic. (that is 3 + 1, done = 4)
done = len(toppings) + 1
print(f'Please type {done} to complete your order!')


# THIS COUNTER IS JUST KEEPING TRACK OF HOW MANY TOPPINGS WE ARE ORDERING
# IT DOES THIS BY CHECKING IF IT'S VALUE IS HIGHER THAT THE len(toppings) (length of toppings)
while counter < len(toppings):
    print(f'{counter + 1}. {toppings[counter]} {price[counter]}')
    counter += 1


orders = [0] * len(toppings)

# HERE IS WHERE MOST OF OUR USER INPUT HAPPENS HERE, WHICH
# IS WHY YOU CAN SEE A LOT OF (input) WHICH MEANS WE WANT TO USE THAT VARIABLE
# FOR SOMETHING LATER. HERE WE ARE ASKING FOR A INTEGER (int) TO BE THE RESPONSE
# SINCE THE TOPPINGS ARE GOING TO BE ORDERED USING NUMBERS.
# THERE ARE A FEW CHECKS TO SEE IF THE NUMBER THEY PUT IS VALID, FOR EX IF ITS MORE
# THAN THE LENGTH OF toppings OR MORE THEN 7 AS WE DEFINED IT

choice = int(input('What topping would you like on your pizza?\n\n'))
while choice != done:
    while choice <= 0 or choice > 7:
        print('That was not an option! Please enter a number from the list.')
        choice = int(input('What topping would you like on your pizza?\n\n'))
    orders[choice - 1] += 1
    choice = int(input('Would you like an additional Pizza topping?\n\n'))

total = 0

# ZIPPING ESSENTIALLY JUST COMBINES THE ORDER THAT OUR LISTS ARE IN
# SINCE WE WANT TOPPINGS TO MATCH THE PRICE WE WANT, ZIPPING ALLOWS
# THOSE TO BE MATCHED! ITS BASICALLY SETTING THOSE THAT ARE APPENDED
# TO MATCH WHAT WE WANT IT TO BE MATCHED WITH
for x, y, z in zip(toppings, orders, price):
    total += y * z
    grand_total = y * z
    if y > 0:
        print(f'You chose {y} x {x} as a topping')

print(f'and you total price is {total} USD.')


# HERE WE ARE JUST ASKING FOR USER INPUT LIKE ADDRESS AND A CONFIRMATION
# NOTE THAT FOR OUR DELIVERY TIME, FOR FUN, WE ADDED A RANDINT
# TO MAKE A RANDOM INT FOR A DELIVERY TIME, I USED THE random LIBRARY
# THE REST IS JUST USING THE INPUT AND REPEATING IT FOR CONFIRMATION!
address = input("What is your address?\n\n")
random_delivery_time = randint(30, 60)  # Chooses random int (will be used for time for delivery)
confirm = input(f'Please confirm that this is your address. {address} (Y/N)\n\n')
if confirm == 'Y':
    print(f'Thank you for your address. Please be ready with ${total} in about {random_delivery_time} minutes.')
if confirm == 'N':
    address = input("What is you address?\n\n")