toppings = ['plain cheese', 'peperoni', 'olive', 'mushrooms', 'garlic'] #Lists(str)
price = [10, 5, 4, 8, 2]  # List (Int)
counter = 0 # Lists(Int)

done = len(toppings) + 1
print(f'{done} ----- Choose this number to finish your order.')

while counter < len(toppings):
    print(f'{counter + 1} {toppings[counter]} {price[counter]}')
    counter += 1

orders = [0] * len(toppings)
choice = int(input('what topping would you like on your pizza?'))
while choice != done:
    while choice <= 0 or choice > 7:
        print('That was not an option. Please enter a number from the list.')
        choice = int(input('what topping would you like on your pizza? Cheese costs '))
    orders[choice - 1] += 1
    choice = int(input('Would you like an aditional pizza topping?'))

total = 0
for x, y, z in zip(toppings, orders, price):
    total += y * z
    grand_total = y * z
    if y > 0:
        print(f'You chose {y} x {x} as a topping.')

print(f'And you total price is {total}')
