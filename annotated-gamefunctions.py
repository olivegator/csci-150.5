#gamefunctions.py
#Olive Copple
#2/17/25
import random # Needed for the random monster function

# Purchasing items function
def purchase_item(itemPrice,startingMoney,quantityToPurchase=1):
    quantityToPurchase = int(quantityToPurchase) # Change to integer, if it isn'talready
    if startingMoney < (itemPrice * quantityToPurchase): # Limits purchased items by the amount in startingMoney
        quantityToPurchase = int((startingMoney // itemPrice))
    return quantityToPurchase, f'{(startingMoney - (quantityToPurchase *itemPrice)):.2f}'

# Examples
totalItems,moneyLeft = purchase_item(10.00,60.00) # Shows default value of items to purchase is 1
print(totalItems,moneyLeft)
totalItems,moneyLeft = purchase_item(5.99,105.80,8)
print(totalItems,moneyLeft)
totalItems,moneyLeft = purchase_item(2.50,12.00,10) # Shows that the functions properly limits the items purchased
print(totalItems,moneyLeft)

# Random Monster Function
def new_random_monster():
    choice = random.randint(0,2) # Randomly chooses the index for the lists of monsters below, to fill out dictionary values
    names = ["Mothman", "Bigfoot", "Loch Ness Monster"]
    descriptions = [
        "Part moth, part man; this frightful beast terrorizes Point Pleasent, West Virginia. \nWith his red eyes and fearsome wings, he is sure to send even the bravest explorer running.",
        "With a whopping size 22 sneaker, this big fellow elusively roams the forests of America. \nThey say he isn't violent... at least when he's not hungry....",
        "This Scottish lass is as old as the dinosaurs! Or, maybe she is one? \nEither way, best be careful when you are fishing..."
    ]
    healths = [random.randrange(100,201,25), random.randrange(200,401,50), random.randrange(500,701,25)]
    powers = [random.randrange(300,401,50),random.randrange(100,201,25),random.randrange(50,101, 10)]
    moneys = [random.randrange(300,401,25),random.randrange(100,251,25),random.randrange(400,551 ,50)]
    monster = { #Dictionary with values from lists with a random index between 0 and 2
        "name": names[choice],
        "description": descriptions[choice],
        "health": healths[choice],
        "power": powers[choice],
        "money": moneys[choice]
        }
    return monster

#Examples
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

# Welcome
def print_welcome(name,width=20):
    welcome = (f"Hello, {name}!")
    print(f"{welcome:^{width}}") #prints welcome message with a width of 20
print_welcome("Olive")
print_welcome("Alligator")

# Menu Shop
def print_shop_menu(item1Name,item1Price,item2Name,item2Price):
    item1Price=f'${item1Price:.2f}' #formats floating numbers
    item2Price=f"${item2Price:.2f}"
    print("_"*25)
    print(('|'),(f'{item1Name:<12}'),(f'{item1Price:>8}'),('|'))
    print("|"," "*21,"|")
    print(('|'),(f'{item2Name:<12}'),(f'{item2Price:>8}'),('|'))
    print("-"*25)
print_shop_menu("emerald",1003.987,"bread",5)
print_shop_menu("bag",13.9,"axe",20.5)
