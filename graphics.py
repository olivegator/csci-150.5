import pygame
import os # Needed for saving position
import wanderingMonster
import json # Needed for loading files
import time


# function for loading character animations
def framesloader(fold):
    if not os.path.exists(fold):
        return None
    frames = []
    for file in sorted(os.listdir(fold)):
        frame = pygame.image.load(os.path.join(fold, file))
        frames.append(frame)
    return frames

def gamewindow(gamedata):

    # initiate game
    pygame.init()

    window = (320,320)
    running = True
    screen = pygame.display.set_mode(window)
    fpsclock = pygame.time.Clock()
    spritespeed = 450
    framenum = 1


    # monster variables:
    monsterdict = {} # to rememdy a "possibly unbound" error
    # load existing monsters
    if os.path.exists("monsters.json"):
        with open("monsters.json", "r") as file:
            monsters = json.load(file)

        # if both monsters are dead, make 2 more.

        if ((monsters[0])["health"] <= 0 and
            (monsters[1])["health"] <= 0):
            monsters = [
                wanderingMonster.wandering_monster().new_random_monster(),
                wanderingMonster.wandering_monster().new_random_monster()
            ]

            # save monster data
            with open("monsters.json", "w") as file:
                json.dump(monsters, file)

    else:
        # if no data exists / first run
        monsters = [
            wanderingMonster.wandering_monster().new_random_monster(),
            wanderingMonster.wandering_monster().new_random_monster()
        ]
        # save monster data
        with open("monsters.json", "w") as file:
            json.dump(monsters, file)

    mclasslist = []
    for monster in monsters:
        if monster["health"] > 0:
            mclasslist.append(wanderingMonster.wandering_monster(monster))

    # player variables
    if os.path.exists("savefile.json"):
           with open("savefile.json", "r") as file:
               gamedict = json.load(file)
               gridx = gamedict["gridx"]
               gridy = gamedict["gridy"]

    else:
        gridx = 2
        gridy = 8
    speed = 1
    option = 0
    playerx = gridx * 32
    playery = gridy * 32
    starttown = True
    if framesloader("char") != None:
        pspritef = framesloader("char")
        player = pygame.Rect(playerx, playery, pspritef[0].get_width(),
        pspritef[0].get_height())
        psprite = True
    else:
        player = pygame.Rect(playerx,playery,32,32)
        psprite = False

    # town variables
    town = pygame.Rect(50,200,100,100)

    # managing movement
    playerturn = False
    endplayerturn = False
    endmonsterturn = False

    while running:

        # quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # stop lagging / graphics issues
        pygame.display.update()
        time.sleep(.01)

        # Bounderies - player
        gridx = max(0, min(9, gridx))
        gridy = max(0, min(9, gridy))


        # controls
        key = pygame.key.get_pressed()

        playerturn = key[pygame.K_UP] or key[pygame.K_DOWN] or\
        key[pygame.K_LEFT] or key[pygame.K_RIGHT]
        if playerturn == True:
            if key[pygame.K_UP]:
                gridy -= speed
            elif key[pygame.K_DOWN]:
                gridy += speed
            elif key[pygame.K_LEFT]:
                gridx -= speed
            elif key[pygame.K_RIGHT]:
                gridx += speed
            # monster moves after player moves
            endplayerturn = True
            endmonsterturn = False
        elif (endplayerturn == True) and (endmonsterturn == False):
            for mclass in mclasslist:
                mclass.move()
            endmonsterturn = True
            endplayerturn = False
        playerx = gridx * 32
        playery = gridy * 32

        player.topleft = (playerx, playery)

        # player enters the town again
        entertown = player.colliderect(town)
        if (entertown == False) and (starttown == True):
            starttown = False
        if (entertown == True) and (starttown == False):
            option = 0
            running = False

        # player encounters a monster
        for i, mclass in enumerate(mclasslist):
            if player.colliderect(mclass.rect):
                with open("monsters.json", "w") as file:
                    json.dump(mclass.saver(), file)
                option = 1
                running = False
                break

        # Drawing
        screen.fill((0,102,51))
        pygame.draw.rect(screen, (76,153,0), town)
        pygame.draw.circle(screen, (102,204,0), (100,250), 44)

        if psprite == True:
            screen.blit(pspritef[framenum], player.topleft)

        else:
            pygame.draw.rect(screen, (255, 205, 229), player)

        for mclass in mclasslist:
            mclass.draw(screen)

        if (mclass.msprite == True) and (psprite==True):
            pygame.display.flip()
            framenum = (framenum + 1) % 2
            fpsclock.tick(4)
        else:
            fpsclock.tick(60)

        # saving the player's position
        with open ("savefile.json", "w") as file:
            gamedata["x"] = player.x
            gamedata["y"] = player.y
            gamedata["gridx"] = gridx
            gamedata["gridy"] = gridy
            json.dump(gamedata, file)



    # Exit
    pygame.quit()
    return option, monsterdict
