#!/usr/bin/python3
# -*-coding:utf-8 -
"""Place where constants are"""

import pygame
from pygame.locals import *

pygame.init()

#Constant for loops
running = 1
running_welcome = 1
running_game = 1

#Dimensions of game screen
NB_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIZE = ((NB_SPRITE +2 ) * SPRITE_SIZE, (NB_SPRITE +2) * SPRITE_SIZE)

#Display of window game
screen = pygame.display.set_mode(SCREEN_SIZE)
screen_TITLE = "Labyrinthe of MacGyver"
Guardian = pygame.image.load("pictures/Gardien.png").convert_alpha()

#Screen "home"
ACCUEIL = pygame.image.load("pictures/th.jpg").convert()

#Screen for "Welcome to the game"
WELCOME = pygame.image.load("pictures/welcome.png").convert_alpha()

#Screen for Pick-up Elements
PICKUP = pygame.image.load("pictures/pickup.png").convert_alpha()

#Screen Game-Over
GAMEOVER = pygame.image.load("pictures/game_over.png").convert_alpha()

#Screen if you You win
WIN = pygame.image.load("pictures/win.png").convert_alpha()

#Game background

BACKGROUND = pygame.image.load("pictures/fond.jpg").convert()

#kind of sprite
WALL = pygame.image.load("pictures/mur.png")
ARRIVAL = pygame.image.load("pictures/Gardien.png").convert_alpha()

#kind of tools
TUBE = pygame.image.load("pictures/small_tube.png").convert_alpha()
ETHER = pygame.image.load("pictures/small_ether.png").convert_alpha()
SERINGUE = pygame.image.load("pictures/small_seringue.png").convert_alpha()

#Display MacGyver
MG = pygame.image.load("pictures/MacGyver.png").convert_alpha()

#variable contain map
FILE = ""

