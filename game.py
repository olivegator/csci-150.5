import gamefunctions
import time

cash = 0
power = 100
health = 500
equipped = "disco ball"
discoballs = 0
lavalamps = 0

name = input("Hello... uh... what was your name \
again? \nenter name: ")
time.sleep(1)
gamefunctions.print_welcome(name)
time.sleep(1)
print("I am Kyler the merchant of magical wares! Welcome to my forest.")
time.sleep(2)
print("There are many creatures lurking here and many cool fun products \
to buy!")
time.sleep(1)
print("Would you like to start your journey anew or would you like to \
load an old adventure?")
load = int(input("1 - New game\n2 - Load saved game\nEnter choice: "))
if load == 2:
    cash, power, health, discoballs, lavalamps\
= gamefunctions.loadgame()

choice = gamefunctions.menu(cash, power, health)
while choice != "4":
    if (choice) == "1":
        cash, power, health, equipped, discoballs, lavalamps\
= gamefunctions.findmonster(cash, power, health, equipped,\
 discoballs, lavalamps)
        if health <= 0:
            break
        choice = gamefunctions.menu(cash, power, health)
    elif (choice) == "2":
        cash, discoballs, lavalamps = gamefunctions.shopping(cash, power,\
 health, discoballs, lavalamps)
        choice = gamefunctions.menu(cash, power, health)
    elif (choice) == "3":
        gamefunctions.statcheck(cash,power,health,equipped,discoballs,lavalamps)
        choice = gamefunctions.menu(cash, power, health)
    elif  (choice.isnumeric() == False) or (int(choice) > 4):
        choice = gamefunctions.invalid(gamefunctions.menu(cash, power, health))
        choice = gamefunctions.menu(cash, power, health)
    else:
        break
gamefunctions.savegame(cash, power, health, discoballs, lavalamps)
print(f"Goodbye {name}! Game saved.")
