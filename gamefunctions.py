#gamefunctions.py
#Olive Copple
#2/17/25

'''
This module has four functions for a game.

There is a purchasing items function, a random monster generator function,
a greeting function, and a function to print off a menu board with a list
of items. The 'random' and 'time'python modules are the only dependencies.
'''

import random # Needed for the random monster function
import time # Needed for text print timing
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
    cash = round(startingMoney - (quantityToPurchase * itemPrice),2)
    return quantityToPurchase, cash


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
        "health": (healths[choice]),
        "power": (powers[choice]),
        "money": (moneys[choice])
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

# Main Game Menu
def menu(cash, power, health):
    '''
    A function that prints the game's main menu options.

    Parameters:
        cash: player's current balence
        power: player's power
        health: player's health

    Returns:
        choice: the player's selection (string)
    '''
    print("What would you like to do?\
    \n 1 - Search for monsters\
    \n 2 - Buy my wares\
    \n 3 - Check stats\
    \n 4 - Exit")
    choice = (input ("Enter your choice: "))
    return choice

def statcheck(cash, power, health):
    '''
    A function to print monster/player stats.

    Parameters:
        cash: character's balence
        power: character's power
        health: character's health

    Returns:
        none
    '''
    print(f"Cash: ${cash}")
    print(f"Power: {power}")
    print(f"Health: {health}")
    time.sleep(2)

def fightmenu(cash, power, health, monster):
    '''
    A function displaying monster fight options.

    Parameters:
        cash: player's balence
        power: player's power
        health: player's health
        monster: monster stats

    Returns:
        monsterhealth: the monster's health after the move
        choice: player's selection in the menu
    '''
    powervar = (power + monster["health"])/2
    print("Your stats:")
    statcheck(cash, power, health)
    print(f"{monster["name"]}'s stats:")
    statcheck(monster["money"], monster["power"], monster["health"])
    print(f"What is your next move?\
    \n 1 - Criss-cross ({int(powervar/4)} damange)\
    \n 2 - The worm ({int(powervar/3)} damage)\
    \n 3 - Headspin ({int(powervar/2)} damage)\
    \n 4 - Leave dance battle")
    choice = (input("Enter your choice: "))
    while choice != "4":
        if choice == "1":
            damage = int(powervar/4)
            print(f"You did {damage} damage with the criss-cross!")
            break
        elif choice == "2":
            damage = int(powervar/3)
            print(f"You did {damage} damage with the worm!")
            break
        elif choice == "3":
            damage = int(powervar/2)
            print(f"You did {damage} damage with the headspin!")
            break
        elif ( choice.isnumeric() == False) or (int(choice) > 3):
            print("Invalid input, try again.")
        choice = (input("Enter your choice: "))
    if int(choice) == 4:
        menu(cash, power, health)
    time.sleep(2)
    monsterhealth = monster["health"] - damage
    #FIXME - unsure how to resolve possibly unbound error, will solve soon
    return monsterhealth, choice

def monstermove(power, health, monster):
    '''
    A function for the monster to deal damage.

    Parameters:
        power: player's power
        health: player's health
        monster: monster stats

    Returns:
        health: player's health after damage
    '''
    powervar = monster["power"] + health
    damage = int(powervar/random.randrange(5,8))
    print(f"{monster["name"]} did {damage} damage with their cool moves!")
    time.sleep(2)
    health = health - damage
    return health

def monsterwin(cash, power, health, monster):
    '''
    A function for if the player wins the battle.

    Parameters:
        cash: player's cash
        power: player's power
        health: player's health
        monster: monster stats

    Returns:
        cash: player's cash (plus cash earned from battle)
        power: player's power (plus power gained from battle)
        health: player's health after battle
    '''
    print("You expertly boogie and take your winnings!")
    time.sleep(2)
    cash = cash + monster["money"]
    power = power + ((monster["power"] + power)/4)
    time.sleep(1)
    statcheck(cash,power,health)
    return cash, power, health

def monsterlose(cash, power, health, monster):
    '''
    A function for if the player loses the battle.

    Parameters:
        cash: player's cash
        power: player's power
        health: player's health
        monster: monster stats

    Returns:
      none, ends game if battle lost

    '''
    print(f"{monster["name"]}'s moves were too cool! You lost :(")
    print(f"Game over!")
    time.sleep(2)

def fightloop(cash,power,health,monster):
    '''
    A loop function for the dance battle, ends when either character loses

    Parameters:
        cash: player's cash
        power: player's power
        health: player's health
        monster: monster stats

    Returns:
        cash: player's cash
        power: player's power
        health: player's health
        monster["health"]: monster's health
    '''
    while (health > 0) and (monster["health"] > 0):
        monster["health"], choice = fightmenu(cash, power, health, monster)
        health = monstermove(power, health, monster)
        if int(choice) == 4:
            break
        if (int(choice) > 4) or choice.isnumeric()== False:
            invalid(fightmenu(cash, power, health, monster))
    if monster["health"] <= 0:
        cash, power, health = monsterwin(cash, power, health, monster)
    if health <= 0:
        monsterlose(cash, power, health, monster)
    return cash, power, health, monster["health"]

def findmonster(cash, power, health):
    '''
    A function for finding a monster to battle

    Parameters:
        cash: player's cash
        power: player's power
        health: player's health
        monster: monster stats

    Returns:
        cash: player's cash
        power: player's power
        health: player's health
    '''
    print("You venture into the forest in search of a monster...")
    time.sleep(1)
    monster = new_random_monster()
    print(f"You found {monster["name"]}!")
    time.sleep(2)
    print(monster["description"])
    statcheck(monster["money"], monster["power"], monster["health"])
    time.sleep(3)
    choice2 = input(f"Would you like to beat {monster["name"]} \
in a dance battle? \n 1 - yes \n 2 - no \n enter: ")
    while choice2 != "2":
        if choice2 == "1":
            cash, power, health, monster["health"]\
            = fightloop(cash, power, health, monster)
            break
        elif (choice2.isnumeric() == False) or (int(choice2) > 2):
            print("Invalid input, please try again.")
            time.sleep(1)
            choice2 = input(f"Would you like to beat {monster["name"]} \
in a dance battle? \n 1 - yes \n 2 - no \n enter: ")
    if choice2 == "2":
        print("Nevermind...")
        menu(cash, power, health)
    return cash, power, health

def shopping(cash, power, health):
    '''
    A function for shopping in the shop.

    Parameters:
        cash: player's cash
        power: player's power
        health: player's health

    Returns:
        cash: player's cash
    '''
    print_shop_menu("disco ball", 250, "lava lamp", 500)
    choice3 = input("What would you like to purchase? \n 1 - \
disco ball \n 2 - lava lamp \n 3 - never mind \nenter: ")
    while choice3 != "3":
        if choice3 == "1":
            total,cash = purchase_item(300,cash,int(input("How many? \
                Enter number: ")))
            print(f"You were able to buy {total} and you have {cash} left.")
            time.sleep(2)
            break
        elif int(choice3) == "2":
            total, cash = purchase_item(500,cash,int(input("How many?\
                enter number: ")))
            print(f"You were able to buy {total} and you have {cash} left.")
            time.sleep(2)
            break
        elif (choice3.isnumeric() == False) or (int(choice3) > 3):
            invalid(shopping(cash, power, health))
    if choice3 == "3":
        menu(cash, power, health)
    return cash

def invalid(menu_func):
    '''
    A function for invalid inputs in menus.

    Parameters:
        menu_func: function for a menu to be reprinted

    Returns:
        menu_func: function for a menu to be reprinted
    '''
    print("Invalid input, try again")
    time.sleep(2)
    return menu_func

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
