import random
import pygame
import graphics

class wandering_monster:
    '''
    A class for monsters. Has all monster data and some methods.

    Parameters (init):
        monster: if a monster should be loaded in, otherwise it will
        generate one
    '''
    # initiating the class
    def __init__(self, monster=None, mask=None):
        # if no monster is to be loaded
        if monster == None:
            monster = self.new_random_monster(mask=mask)

        # initiate all variables
        self.name = monster["name"]
        self.description = monster["description"]
        self.health = monster["health"]
        self.power = monster["power"]
        self.money = monster["money"]
        self.color = monster["color"]
        self.gridx = monster["gridx"]
        self.gridy = monster["gridy"]
        self.imagedir = monster.get("imagedir", None)
        # x/y 10 px grid conversion
        self.x = self.gridx * 32
        self.y = self.gridy * 32

        # loading the monster sprites/animations
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
        '''
        A function for moving the monsters.

        Parameters:
            None

        Returns:
            None. Sets init variables related to position/movement.
        '''
        direction = random.choice([(-1,0),(1,0),(0,-1),(0,1)])
        self.gridx += direction[0]
        self.gridy += direction[1]

        # Bounderies
        self.gridx = max(0, min(9, self.gridx))
        self.gridy = max(0, min(9, self.gridy))

        # update location
        self.x = self.gridx * 32
        self.y = self.gridy * 32
        self.rect.topleft = (self.x, self.y)

    def new_random_monster(self,mask = None):
        '''
        A function to randomly choose a monster with random stats.

        It randomly chooses the index for the lists of monsters,
        to fill out dictionary values for the returned monster.

        Parameters:
            mask: for the monster's map bounderies

        Returns:
            monster: a random monster with a correlated desctiption. The
            monster will have random stats (health, power, and money) within
            a certain range. Stored in a dictionary.
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
            '''
            A function to set the color of the monster, based on type.

            Parameters:
                choice: shows type of monster
            Returns:
                color: monster color
            '''
            color = (0,0,0)
            if choice == 0:
                color = (76,0,153)
            if choice == 1:
                color = (74,37,37)
            if choice == 2:
                color = (102,102,255)
            return color

        def setposition():
            '''
            A function to set the position of the monster.

            Loch Ness Monster can go in the lake, but not on land.
            The opposite is true for other monsters.

            Parameters:
                none
            Returns:
                grid and true (pixel) locations of monsters
            '''

            while True or (insea == None):
                gridx = random.randint(0, 9)
                gridy = random.randint(0, 9)
                x = gridx * 32
                y = gridy * 32
                insea = mask.get_at((x, y))
                if (((insea == True) and (choice == 2)) or
                    ((insea == False) and (choice != 2))):
                        return gridx, gridy, x, y
        gridx, gridy, x, y = setposition()

        # monster dictionary
        monster = {
            "name": names[choice],
            "description": descriptions[choice],
            "health": (healths[choice]),
            "power": (powers[choice]),
            "money": (moneys[choice]),
            "color": setcolor(choice),
            "gridx": gridx,
            "gridy": gridy,
            "x": x,
            "y": y,
            "imagedir": imagedirs[choice]
            }
        return monster

    # function to draw the monster
    def draw(self,screen):
        '''
        A function to draw the monsters' sprites

        Parameters:
            screen:
                surface to draw on

        Returns:
            none, just draws the sprites.
        '''
        if self.msprite == True:
            self.framenum = (self.framenum + 1) % 2
            screen.blit(self.spritef[self.framenum],self.rect)
        else:
            pygame.draw.rect(screen,(0,102,51),self.rect)
            pygame.draw.circle(screen, self.color,self.rect.center, 16)

    # monster data saving
    def saver(self):
        '''
        A function returning current/updated monster info in a dictionary.

        Parameters:
            none
        Returns:
            A dictionary with the monster's stats
        '''
        return {
            "name": self.name,
            "description": self.description,
            "health": self.health,
            "power": self.power,
            "money": self.money,
            "color": self.color,
            "gridx": self.gridx,
            "gridy": self.gridy,
            "x": self.x,
            "y": self.y,
            "imagedir": self.imagedir
        }
