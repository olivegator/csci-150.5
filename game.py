import gamefunctions
import time

cash = 0
name = input("Hello... uh... what was your name \
again? \nenter name: ")
time.sleep(1)
gamefunctions.print_welcome(name)
time.sleep(1)
print("I am Kyler the merchant of magical wares! Welcome to my forest.")
time.sleep(2)
print("There are many creatures lurking here and many cool fun products \
to buy!")
time.sleep(3)

def menu(cash):
    print("What would you like to do?\
    \n 1 - Search for monsters\
    \n 2 - Buy my wares\
    \n 3 - Check balence\
    \n anything else to exit")
    choice = int(input ("Enter your choice: "))
    if choice == 1:
        print("You venture into the forest in search of a monster...")
        time.sleep(1)
        print("You found one!")
        time.sleep(1)
        monster = gamefunctions.new_random_monster()
        print(monster["name"])
        print(monster["description"])
        print("Health: ",monster["health"])
        print("Power: ",monster["power"])
        print("Cash: ",monster["money"])
        time.sleep(4)
        choice2 = int(input("Would you like to beat them in a dance battle\
? \n 1 - yes \n 2 - no \n enter: "))
        if choice2 == 1:
            print("You expertly boogie and take your winnings!")
            time.sleep(2)
            cash = cash + monster["money"]
            time.sleep(1)
            print(f"You have ${cash}")
            time.sleep(2)
            menu(cash)
        elif choice == 2:
            print("oh well...")
            menu(cash)
        else:
            menu(cash)

    elif choice == 2:
        gamefunctions.print_shop_menu("disco ball", 250, "lava lamp", 500)
        choice3 = int(input("What would you like to purchase? \n 1 - \
disco ball \n 2 - lava lamp \n 3 - never mind \nenter: "))
        if choice3 == 1:
            total,cash = gamefunctions.purchase_item(300,cash,int(input("How many?\
 enter number: ")))
            print(f"You were able to buy {total} and you have {cash} left.")
            time.sleep(2)
            menu(cash)
        elif choice3 == 2:
            total, cash = gamefunctions.purchase_item(500,cash,int(input("How many?\
 enter number: ")))
            print(f"You were able to buy {total} and you have {cash} left.")
            time.sleep(2)
            menu(cash)
        else:
            menu(cash)
    elif choice == 3:
        print(f"You have ${cash}.")
        time.sleep(2)
        menu(cash)
    else:
        print(f"Goodbye {name}!")

menu(cash)
