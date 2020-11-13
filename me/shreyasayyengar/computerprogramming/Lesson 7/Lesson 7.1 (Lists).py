foods = ["Apple Slices", "Pizza", "Pasta", "Steak", "Bread", "Chocolate Bar"]
prices = [50, 150, 200, 250, 120, 80]
counter = 0

while counter < len(foods):
    print(f"{counter + 1} {foods[counter]}: {prices[counter]}")
    counter += 1

foodchoice = int(input("\n\nWhat would you like to eat today? Please either give the food choice. \n\n"))

print(f'You chose {foods[foodchoice - 1]}. It will amount to {prices[foodchoice - 1]} PHP')
