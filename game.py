import gamefunctions
import time

name = " "
cash = 0
power = 100
health = 500
equipped = "disco ball"
discoballs = 0
lavalamps = 0
x = 85
y = 232

print("Would you like to start your journey anew or would you like to \
load an old adventure?")
load = input("1 - New game\n2 - Load saved game\nEnter choice: ")
while (load.isnumeric()) == False or (0>int(load)>3):
    load = input("1 - New game\n2 - Load saved game\nEnter choice: ")
if load == "2":
    name, cash, power, health, discoballs, lavalamps, x, y = gamefunctions.loadgame()
elif (load != "2"):
    time.sleep(1)
    print("New adventure ready!")
if name == " ":
    time.sleep(1)
    name = input("Hello... uh... what was your name \
again? \nenter name: ")


gamedata = {"Cash": cash, "Power": power, "Health":health,
    "Discoballs":discoballs, "Lava Lamps":lavalamps, "x":x, "y":y, "Name":name}

time.sleep(1)
gamefunctions.print_welcome(name)
time.sleep(1)
print("I am Kyler the merchant of magical wares! Welcome to my forest.")
time.sleep(2)
print("There are many creatures lurking here and many cool fun products \
to buy!")
time.sleep(1)

choice = gamefunctions.menu(cash, power, health)
while choice != "5":
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
    elif (choice) == "4":
        option = gamefunctions.gamewindow(gamedata)
        if option == 0:
            choice = gamefunctions.menu(cash, power, health)
        elif option == 1:
            choice = "1"
    elif  (choice.isnumeric() == False) or (int(choice) > 5):
        choice = gamefunctions.invalid(gamefunctions.menu(cash, power, health))
        choice = gamefunctions.menu(cash, power, health)
    else:
        break
if health > 0:
    gamefunctions.savegame(gamedata)
    print(f"Goodbye {name}! Game saved.")
else:
    print(f"Goodbye {name}!")
