import random
import pygame
import graphics

class wandering_monster:

    def __init__(self, monster=None):
        if monster == None:
            monster = self.new_random_monster()
        self.name = monster["name"]
        self.description = monster["description"]
        self.health = monster["health"]
        self.power = monster["power"]
        self.money = monster["money"]
        self.color = monster["color"]
        self.grid_x = monster["grid_x"]
        self.grid_y = monster["grid_y"]
        self.imagedir = monster.get("imagedir", None)

        self.x = self.grid_x * 32
        self.y = self.grid_y * 32

        if graphics.framesloader(self.imagedir) != None:
            self.spritef = list(graphics.framesloader(self.imagedir))
            self.rect = pygame.Rect(self.x, self.y,
            self.spritef[0].get_width(), self.spritef[0].get_height())
            self.msprite = True
            self.framenum = 1
        else:
            self.rect = pygame.Rect(self.x,self.y,32,32)
            self.msprite = False

    def move(self):
        direction = random.choice([(-1,0),(1,0),(0,-1),(0,1)])

        self.grid_x += direction[0]
        self.grid_y += direction[1]

        # Bounderies
        self.grid_x = max(0, min(9, self.grid_x))
        self.grid_y = max(0, min(9, self.grid_y))

        self.x = self.grid_x * 32
        self.y = self.grid_y * 32

        self.rect.topleft = (self.x, self.y)

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

        imagedirs = [ "mm","bf","lnm" ]

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
            "grid_x": random.randint(0, 9),
            "grid_y": random.randint(0, 9),
            "x": random.randrange(20, 300),
            "y": random.randrange(10, 140),
            "imagedir": imagedirs[choice]
            }

        return monster

    def draw(self,screen):
        if self.msprite == True:
            self.framenum = (self.framenum + 1) % 2
            screen.blit(self.spritef[self.framenum],self.rect)
        else:
            pygame.draw.rect(screen,(0,102,51),self.rect)
            pygame.draw.circle(screen, self.color,self.rect.center, 16)

    def saver(self):
        return {
            "name": self.name,
            "description": self.description,
            "health": self.health,
            "power": self.power,
            "money": self.money,
            "color": self.color,
            "x": self.x,
            "y": self.y,
            "imagedir": self.imagedir
        }
