from random import *

toppings = ['Plain Cheese Pizza', 'Peperoni', 'Tomatoes', 'Garlic', 'Olives']
# HERE, I AM DEFINING THE VARIABLE "toppings" AS A LIST BY USING [] SYNTAX.
# ALL ENTRIES IN THIS LIST ARE TAKEN AS A STRING (hence the "")


price = [10 , 15, 20, 13, 14]
# THIS IS ANOTHER LIST THAT IS DEFINED AS "price" WHICH
# TAKES IN INTEGERS (int) AS VALUES. THESE SERVE AS A
# PRICE FOR THE TOPPINGS


counter = 0  # Lists(Int)

done = len(toppings) + 1
print(f'{done} ----- Choose this number to finish your order.')

while counter < len(toppings):
    print(f'{counter + 1}. {toppings[counter]} {price[counter]}')
    counter += 1

orders = [0] * len(toppings)
choice = int(input('What topping would you like on your pizza?\n\n'))
while choice != done:
    while choice <= 0 or choice > 7:
        print('That was not an option! Please enter a number from the list.')
        choice = int(input('What topping would you like on your pizza?\n\n'))
    orders[choice - 1] += 1
    choice = int(input('Would you like an aditional Pizza topping?\n\n'))

total = 0
for x, y, z in zip(toppings, orders, price):
    total += y * z
    grand_total = y * z
    if y > 0:
        print(f'You chose {y} x {x} as a topping')

print(f'and you total price is {total} USD.')

address = input("What is your address?\n\n")
random_delivery_time = randint(30, 60)  # Chooses random int (will be used for time for delivery)
confirm = input(f'Please confirm that this is your address. {address} (Y/N)\n\n')
if confirm == 'Y':
    print(f'Thank you for your address. Please be ready with ${total} in about {random_delivery_time} minutes.')
if confirm == 'N':
    address = input("What is you address?\n\n")