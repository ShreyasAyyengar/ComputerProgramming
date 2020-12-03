from random import *



foods = ["Apple Slices", "Pizza", "Pasta", "Steak", "Bread", "Chocolate Bar"]
prices = [50, 150, 200, 250, 120, 80]
counter = 0

while counter < len(foods):
    print(f'{counter + 1} {foods[counter]} {prices[counter]}')
    counter += 1

done = len(foods) + 1
print(f'{done}  ----- Choose this number to finish your order.')

orders = [0] * len(foods)
choice = int(input('What food item would you like?\n\n'))
print(f'{done}  ----- Choose this number to finish your order.')

orders = [0] * len(foods)
choice = int(input('What food item would you like?\n\n'))

while choice != done:
    try:
        a = len(foods)
        print
        a[choice]
    except IndexError:
        print("You chose an invalid number!")

    # while choice <= 0 or choice > len(foods) + 1:
    #     print("Sorry, you have not entered a valid number. Please only choose valid food items. ")
    #     choice = int(input('What food item would you like?\n\n'))

    orders[choice - 1] += 1
    choice = int(input('What additional food item would you like?\n\n'))

total = 0
for x, y, z in zip(foods, orders, prices):
    total += y * z
    if y > 0:
        print(f' Excellent choice. You chose {y} x {x}.')

print(f' Your grand total is {total}. Bon appetit!')


done = len(foods) + 1
print(f'{done}  ----- Choose this number to finish your order.')

orders = [0] * len(foods)
choice = int(input('What food item would you like?\n\n'))
print(f'{done}  ----- Choose this number to finish your order.')

orders = [0] * len(foods)
choice = int(input('What food item would you like?\n\n'))

while choice != done:
    try:
        a = len(foods)
        print
        a[choice]
    except IndexError:
        print("You chose an invalid number!")

    # while choice <= 0 or choice > len(foods) + 1:
    #     print("Sorry, you have not entered a valid number. Please only choose valid food items. ")
    #     choice = int(input('What food item would you like?\n\n'))

    orders[choice - 1] += 1
    choice = int(input('What additional food item would you like?\n\n'))

total = 0
for x, y, z in zip(foods, orders, prices):
    total += y * z
    if y > 0:
        print(f' Excellent choice. You chose {y} x {x}.')

print(f' Your grand total is {total}. Bon appetit!')
