#!/usr/bin/python3
# -*-coding:utf-8 -

"""Program which Help MacGyver to escape from the maze after catching the tree items!"""
from constantes import *
from maze import *
from object import *
from  player import *

# Open window of the game
pygame.display.set_icon(Guardian)
pygame.display.set_caption(screen_TITLE)

# MAIN_LOOP
running = 1
while running:

    # Load home screen
    screen.blit(BACKGROUND, (30, 30))
    screen.blit(ACCUEIL, (100, 100))
    # Reload display
    pygame.display.flip()

    # main boucle
    running_welcome = 1
    while running_welcome:


        # delay boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Quit the program
            if event.type == QUIT:
                print("See you next Time!")
                running = 0
                running_welcome = 0
                running_game = 0

            # Quit home loop to enter in game loop with taping any key
            if event.type == KEYDOWN :
                #Welcome to the game

                screen.blit(BACKGROUND, (30, 30))
                screen.blit(WELCOME, (75, 100))
                pygame.display.flip()
                time.sleep(2)
                ####################################

                running_welcome = 0
                running_game = 1

                # Load the game's maze from file
                FILE = "level_game"

    if FILE != "":  # We make sure that the file really exists and is not empty

        # loading the background
        screen.blit(BACKGROUND, (30, 30))

        # generation of the maze
        maze = Maze(FILE)
        maze.generate()
        maze.display(screen)

        # Get the 3 items in the maze

        seringue = Items("seringue", SERINGUE, maze)
        seringue.position_items()
        seringue.pin_items()

        ether = Items("ether", ETHER, maze)
        ether.position_items()
        ether.pin_items()

        tube = Items("tube", TUBE, maze)
        tube.position_items()
        tube.pin_items()

        # And God create an Heroe
        MacGyver = Player(maze)

    # la boucle du jeu

    # Initialization de chaque boucle du jeu dans un liste vide pour y mettre les items
    box = []
    while running_game:

        pygame.time.Clock().tick(30)
        for event in pygame.event.get():

            # Quit the program
            if event.type == QUIT:
                print("Bye bye!")
                running = 0
                running_game = 0

            if event.type == KEYDOWN:

                # Quit the game and go back Home
                if event.key == K_ESCAPE:
                    running_game = 0

                # Move our heroe!
                if event.key == K_RIGHT:
                    MacGyver.move("right")
                if event.key == K_LEFT:
                    MacGyver.move("left")
                if event.key == K_DOWN:
                    MacGyver.move("bottom")
                if event.key == K_UP:
                    MacGyver.move("up")

                    # Display the game board
        screen.blit(BACKGROUND, (0 + 30, 0 + 30))
        maze.display(screen)

        # Add the hero MacGyver in the Labyrinth with his position
        screen.blit(MG, (MacGyver.x + 30, MacGyver.y + 30))  # + 30 for the offset of the black outline

        # conditionnal add display of each items in the maze

        tube.display_items(screen, MacGyver, box)
        seringue.display_items(screen, MacGyver, box)
        ether.display_items(screen, MacGyver, box)

        pygame.display.flip()

        if maze.structure[MacGyver.sprite_y][MacGyver.sprite_x] == "a":

            # The game user wins if he gets the tree items
            if len(box) < 3:
                #DISPLAY GAME OVER
                screen.blit(GAMEOVER, (150 + 30, 150 + 30))
                pygame.display.flip()
                time.sleep(2)
                ######
                print("You loose ! Try again later")
                running_game = 0

            if len(box) == 3:
                #DISPLAY that you have won
                screen.blit(WIN, (-100 , -100 ))
                pygame.display.flip()
                time.sleep(2)
                ###
                print("You win! congratulations !")
                running_game = 0