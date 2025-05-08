import pygame
import random
import os
import wanderingMonster
import json
import time

# function for loading character animations
def framesloader(fold):
    '''
    A function for loading frames in a folder to animate an object.

    Parameters:
        fold: the folder where the images are
    Returns:
        frames: a list of the images to switch between
    Dependancies:
        os, pygame, time, random, wanderingMonster
    '''
    if not os.path.exists(fold):
        return None
    frames = []
    for file in sorted(os.listdir(fold)):
        frame = pygame.image.load(os.path.join(fold, file))
        frames.append(frame)
    return frames

# main loop
def gamewindow(gamedata):
    '''
    My main game graphics.

    Parameters:
        gamedata: player's info
    Returns:
        option: used for initiating fight or going to the menu
        monsterdict: dictonary of an encountered monster to fight
    Dependencies:
        pygame, os, json,
    '''
    # initiate game
    pygame.init()

    window = (320,320)
    running = True
    screen = pygame.display.set_mode(window)
    fpsclock = pygame.time.Clock()
    spritespeed = 450
    framenum = 1

    # town/map variables
    townimg = pygame.image.load("home.png").convert_alpha()
    map = pygame.image.load("map.png")
    treeimg = pygame.image.load("tree.png")
    seaf = framesloader("sea")
    town = townimg.get_rect()
    town.topleft = (250,5)
    seamask = pygame.mask.from_surface(seaf[0]) # for bounderies

    # tree list - 6 random trees are generated on the dark green land.
    trees= []
    for i in range(6):
        for t in range(10):
            treex = random.randint(0, 9) * 32
            treey = random.randint(0, 9) * 32
            if map.get_at((treex, treey))[:3] == (111, 143, 68):
                trect = pygame.Rect(treex, treey, 32, 32)
                trees.append(trect)
                break



    # monster variables
    monsterdict = {} # to rememdy a "possibly unbound" error

    # load existing monsters
    if os.path.exists("monsters.json"):
        with open("monsters.json", "r") as file:
            monsters = (json.load(file))

        # if both monsters are dead, make 2 more.
        if ((monsters[0])["health"] <= 0 and
            (monsters[1])["health"] <= 0):
            monsters = [
                wanderingMonster.wandering_monster(mask=seamask)
                .new_random_monster(mask=seamask),
                wanderingMonster.wandering_monster(mask=seamask)
                .new_random_monster(mask=seamask)
            ]

            # save monster data
            with open("monsters.json", "w") as file:
                json.dump(monsters, file)

    else:
        # if no data exists / first run
        monsters = [
            wanderingMonster.wandering_monster(mask=seamask)
            .new_random_monster(mask=seamask),
            wanderingMonster.wandering_monster(mask=seamask)
            .new_random_monster(mask=seamask)
        ]
        # save monster data
        with open("monsters.json", "w") as file:
            json.dump(monsters, file)

    # monster class list, only living monsters
    mclasslist = []
    for monster in monsters:
        if monster["health"] > 0:
            mclasslist.append(wanderingMonster
            .wandering_monster(monster,seamask))

    # player variables
    if os.path.exists("savefile.json"):
        # loads in saved location data
        with open("savefile.json", "r") as file:
            gamedict = json.load(file)
            gridx = gamedict["gridx"]
            gridy = gamedict["gridy"]
    else: # default location
        gridx = 2
        gridy = 8
    speed = 1
    option = 0
    playerx = gridx * 32
    playery = gridy * 32
    starttown = True

    # player sprite animations
    if framesloader("char") != None:
        pspritef = framesloader("char")
        player = pygame.Rect(playerx, playery, pspritef[0].get_width(),
        pspritef[0].get_height())
        psprite = True
    else:
        player = pygame.Rect(playerx,playery,32,32)
        psprite = False

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
        oldx, oldy = player.x, player.y # stores position for collisions
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
                # monster movement variables
                oldmx, oldmy = mclass.x,mclass.y
                insea = seamask.get_at((mclass.x, mclass.y))

                # monster movement and bounderies
                mclass.move()
                if mclass.name == "Loch Ness Monster" and not insea:
                    # bounderies for Nessie
                    trys = 0
                    mclass.move()
                    while (not seamask.get_at((mclass.x, mclass.y))
                    and trys !=10):
                        mclass.move()
                        trys+=1

                elif mclass.name != "Loch Ness Monster" and insea:
                    # bounderies for other monsters
                    trys = 0
                    mclass.move()
                    while (seamask.get_at((mclass.x, mclass.y))
                    and trys != 10):
                        mclass.move()
                        trys +=1

                for tree in trees: # tree collisions for monsters
                    if mclass.rect.colliderect(tree):
                        mclass.x, mclass.y = oldmx, oldmy
                        mclass.rect.topleft = (oldmx, oldmy)
                        break
                if mclass.rect.collidrect(town): # monsters cannot go in the town
                    mclass.x, mclass.y = oldmx, oldmy
                    mclass.rect.topleft = (oldmx, oldmy)
            endmonsterturn = True
            endplayerturn = False

        # update player location
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

        # player encounters a tree
        for tree in trees:
            if player.colliderect(tree):
                player.x, player.y = oldx, oldy
                break

        # player encounters a monster
        for i, mclass in enumerate(mclasslist):
            if player.colliderect(mclass.rect):
                monsterdict = mclass.saver()
                option = 1
                running = False
                break

        # Drawing
        screen.fill((0,0,0))
        screen.blit(map,(0,0)) # background
        screen.blit(seaf[framenum],(0,0)) # lake/sea
        for tree in trees: # trees
            screen.blit(treeimg, tree.topleft)
        screen.blit(townimg,(250,5)) # town
        screen.blit(pspritef[framenum], player.topleft) # player's sprite
        for mclass in mclasslist: # monster sprites, if alive
            if mclass.health > 0:
                mclass.draw(screen)

        # animation timing
        pygame.display.flip()
        framenum = (framenum + 1) % 2
        fpsclock.tick(4)

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
