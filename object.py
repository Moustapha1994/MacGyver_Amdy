import random
import time
from constantes import *
import pygame

class Items():
    """Class which define the various elements.
    Takes in parameter: the element's name, the surface and the labyrinth.
    2 methods: locate with random choice the position,
    write the grid in order to get the element later"""

    def __init__(self, name, SURFACE, maze):
        # Position in pixel:
        self.x = 0
        self.y = 0
        # Position in square:
        self.sprite_x = 0
        self.sprite_y = 0
        # Name of the elements
        self.name = name
        # Labyrinth
        self.maze = maze
        # Surface
        self.surface = SURFACE

    def position_items(self):
        """To locate one element: we detecte empty cell. We catch the coordinate in a list of tuple
        (y,x), we choice one pair of co-ordinates"""
        position = []
        coordinates = ()
        num_line = 0
        while num_line < len(self.maze.structure):
            num_cell = 1  # We remove the first cell - the cell of departure
            while num_cell < len(self.maze.structure[0]):  # By default, the lenght of the first line
                if self.maze.structure[num_line][num_cell] == "0":
                    coordinates = (num_line, num_cell)
                    position.append(coordinates)
                num_cell += 1
            num_line += 1

        item_coordinates = random.choice(position)
        self.sprite_y = item_coordinates[0]
        self.sprite_x = item_coordinates[1]
        self.x = self.sprite_x * SPRITE_SIZE
        self.y = self.sprite_y * SPRITE_SIZE

    def pin_items(self):
        """Pin the name of the element to help MacGyver to find it"""
        self.maze.structure[self.sprite_y][self.sprite_x] = self.name

    def display_items(self, screen, MacGyver, TOOLS):
        """Conditional display of the element
        """

        if self.maze.structure[self.sprite_y][self.sprite_x] == self.name:
            screen.blit(self.surface, (self.x + 30, self.y + 30))  # + 30 for the offset of the black outline

        if self.maze.structure[MacGyver.sprite_y][MacGyver.sprite_x] == self.name:
            ######dysplay the pick-up of the elements#############
            screen.blit(PICKUP, (120, 120 ))  # + 30 for the offset of the black outline
            pygame.display.flip()
            # JINGLE.play()
            time.sleep(1)


            print(" You have caught the {}!".format(self.name))
            self.maze.structure[MacGyver.sprite_y][MacGyver.sprite_x] = "0"
            TOOLS.append(self.name)

        # display the scoreboard
        if self.name in TOOLS:
            screen.blit(self.surface, (TOOLS.index(self.name) * SPRITE_SIZE, 0))


