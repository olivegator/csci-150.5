#gamefunctions.py
#Olive Copple
#2/17/25

'''
This module has four functions for a game.

There is a purchasing items function, a random monster generator function,
a greeting function, and a function to print off a menu board with a list
of items. The 'random' python module is the only dependency.
'''

import random # Needed for the random monster function

# Purchasing items function
def purchase_item(itemPrice,startingMoney,quantityToPurchase=1):
    '''
    Purchase a/an item(s).

    Parameters:
        itemPrice: price of the item
        startingMoney: amount the player starts with
        quantityToPurchase: amount of items to purchase (limited by
        starting money, default is 1)

    Returns:
        quantity to purchase and the money left formatted
        to 2 decimal spaces
    '''
    quantityToPurchase = int(quantityToPurchase)
    if startingMoney < (itemPrice * quantityToPurchase):
        quantityToPurchase = int((startingMoney // itemPrice))
    return quantityToPurchase,\
    f'{(startingMoney - (quantityToPurchase *itemPrice)):.2f}'


# Random Monster Function
def new_random_monster():
    '''
    A function to randomly choose a monster with random stats.

    It randomly chooses the index for the lists of monsters,
    to fill out dictionary values for the returned monster.
    Parameters:
        None

    Returns:
        monster: a random monster with a correlated desctiption. The
        monster will have random stats (health, power, and money) within
        a certain range
    '''
    choice = random.randint(0,2)
    names = [
        "Mothman",
        "Bigfoot",
        "Loch Ness Monster"
    ]
    descriptions = [
        "Part moth, part man; this frightful beast terrorizes Point \
Pleasent, West Virginia.\nWith his red eyes and fearsome wings, \
he is sure to send even the bravest explorer running.",
        "With a whopping size 22 sneaker, this big fellow elusively roams \
the forests of America. \nThey say he isn't violent... at least \
when he's not hungry....",
        "This Scottish lass is as old as the dinosaurs! Or, maybe she is \
one? \nEither way, best be careful when you are fishing..."
    ]
    healths = [random.randrange(100,201,25), random.randrange(200,401,50),
        random.randrange(500,701,25)]
    powers = [random.randrange(300,401,50),random.randrange(100,201,25),
        random.randrange(50,101, 10)]
    moneys = [random.randrange(300,401,25),random.randrange(100,251,25),
        random.randrange(400,551 ,50)]
    monster = {
        "name": names[choice],
        "description": descriptions[choice],
        "health": healths[choice],
        "power": powers[choice],
        "money": moneys[choice]
        }
    return monster



# Welcome
def print_welcome(name,width=20):
    '''
    A function to print a welcome message with a name.

    Parameters:
        name: the name to greet
        width: width (in spaces) of the greeting message, used to center
        the message (default of 20 spaces)

    Returns:
        none, prints out welcome message
    '''
    welcome = (f"Hello, {name}!")
    print(f"{welcome:^{width}}")


# Menu Shop
def print_shop_menu(item1Name,item1Price,item2Name,item2Price):
    '''
    A function to print a menu board with items and prices listed.

    Parameters:
        item1Name: name of the first item for sale
        item1Price: price of the first item
        item2Name: name of the second item for sale
        item2Price: price of the second item

    Returns:
        none, prints out a menuboard using characters like _,-, and |, is
        25 spaces long
    '''
    item1Price=f'${item1Price:.2f}' #formats floating numbers
    item2Price=f"${item2Price:.2f}"
    print("_"*25)
    print(('|'),(f'{item1Name:<12}'),(f'{item1Price:>8}'),('|'))
    print("|"," "*21,"|")
    print(('|'),(f'{item2Name:<12}'),(f'{item2Price:>8}'),('|'))
    print("-"*25)


# Examples
def test_functions():
    # purchase_item function test
    totalItems,moneyLeft = purchase_item(10.00,60.00)
    print(totalItems,moneyLeft)
    totalItems,moneyLeft = purchase_item(5.99,105.80,8)
    print(totalItems,moneyLeft)
    totalItems,moneyLeft = purchase_item(2.50,12.00,10)
    print(totalItems,moneyLeft)

    # random_monster function test
    monster1 = new_random_monster()
    print(monster1["name"])
    print(monster1["description"])
    print(monster1["health"])
    print(monster1["power"])
    print(monster1["money"])
    monster2 = new_random_monster()
    print(monster2["name"])
    print(monster2["description"])
    print(monster2["health"])
    print(monster2["power"])
    print(monster2["money"])
    monster3 = new_random_monster()
    print(monster3["name"])
    print(monster3["description"])
    print(monster3["health"])
    print(monster3["power"])
    print(monster3["money"])

    # print_welcome function test
    print_welcome("Olive")
    print_welcome("Alligator")

    # print_shop menu function test
    print_shop_menu("emerald",1003.987,"bread",5)
    print_shop_menu("bag",13.9,"axe",20.5)

if __name__ == "__main__":
    test_functions()
