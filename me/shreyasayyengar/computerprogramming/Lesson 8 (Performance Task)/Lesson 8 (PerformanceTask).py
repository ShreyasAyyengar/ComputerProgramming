from random import *
from time import *

num_pizzas = 0
allPizza = []

order = input("Would you like to order a pizza? Yes/No \n\n")

while order != "No":
    toppings = []
    prices = []
    topping = input("What do you want on your pizza?\n\n")
    toppings.append(topping)
    prices.append(randint(20, 200))
    moreTopping = input("Would you be interested in another topping? Yes/No")


    while moreTopping != "No":
        topping = input("What do you want on your pizza?")
        toppings.append(topping)

        price = randint(20, 200)
        if price not in prices:
            prices.append(price)

        moreTopping = input("Would you be interested in another topping? Yes/No")

    allPizza.append(toppings)
    order = input("Would you like to order another pizza? Yes/No\n\n")

num = 0
pricenum = 0


for t, p in zip(toppings, prices):
    print(f'Your pizza ' + str(num+1) + f' with {t} which costs {p}')

delivery = randint(30, 60)
sleep(1)

while 1 == 1:
    creditcard = int(input("What is your credit card information?"))
    confirm = input("Are you sure that your credit card information is correct? (Y/N) \n\n " + creditcard)
    if confirm == 'Y':
        print(f'Please be ready with {total} in {delivery}')
    if confirm == 'N':
        creditcard = int(input("What is your credit card information?"))