import random
import pygame

class wandering_monster:

    def __init__(self, color = (0,0,0), x=200, y=50,
    speed = 1):
        self.monster = {}
        self.x = random.randrange(20,300)
        self.y = random.randrange(10,140)
        self.speed = speed
        self.rect = pygame.Rect(self.x,self.y, 32, 32)

    def move(self):
        direction = random.choice([(-1,0),(1,0),(0,-1),(0,1)])
        self.rect.move_ip((direction[0]*20),(direction[1]*20))
        self.x = self.rect.x
        self.y = self.rect.y

        # Bounderies

        if self.rect.left < 0:
            self.rect.left = 0
            direction = (1,0)
        if self.rect.top < 0:
            self.rect.top = 0
            direction = (0,1)
        if self.rect.right > 320:
            self.rect.right = 320
            direction = (-1,0)
        if self.rect.bottom > 150:
            self.rect.bottom = 150
            direction = (0,-1)


    def new_random_monster(self):
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
            random.randrange(400,551,50)]


        def setcolor(choice):
            color = (0,0,0)
            if choice == 0:
                color = (76,0,153)
            if choice == 1:
                color = (74,37,37)
            if choice == 2:
                color = (102,102,255)
            return color

        monster = {
            "name": names[choice],
            "description": descriptions[choice],
            "health": (healths[choice]),
            "power": (powers[choice]),
            "money": (moneys[choice]),
            "color": setcolor(choice),
            "x": self.x,
            "y": self.y,
            "defeated": False
            }
        return monster
