import gamefunctions
import time

cash = 0
power = 100
health = 500
name = input("Hello... uh... what was your name \
again? \nenter name: ")
#time.sleep(1)
#gamefunctions.print_welcome(name)
#time.sleep(1)
#print("I am Kyler the merchant of magical wares! Welcome to my forest.")
#time.sleep(2)
#print("There are many creatures lurking here and many cool fun products \
#to buy!")
#time.sleep(3)

choice = gamefunctions.menu(cash, power, health)
while choice != "4":
    if (choice) == "1":
        cash, power, health = gamefunctions.findmonster(cash, power, health)
        if health <= 0:
            break
    elif (choice) == "2":
        cash = gamefunctions.shopping(cash, power, health)
    elif (choice) == "3":
        gamefunctions.statcheck(cash, power, health)
    elif  (choice.isnumeric() == False) or (int(choice) > 3):
        choice = gamefunctions.invalid(gamefunctions.menu(cash, power, health))
    choice = gamefunctions.menu(cash, power, health)
if choice == 4:
    print(f"Goodbye {name}!")
print(f"Goodbye {name}!")
