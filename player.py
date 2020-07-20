
import pygame
from constantes import *


class Player():
    """ class which define a character to deplace with x and y position.
    This character moves inside a labyrinth so the class take one parameter: labyrinth object """

    def __init__(self, labyrinth):
        # Position in pixel:
        self.x = 0
        self.y = 0
        # Position in square:
        self.sprite_x = 0
        self.sprite_y = 0
        # Labyrinth
        self.labyrinth = labyrinth

    def move(self, direction):
        """Method whitch allows to move the character. This method takes in parmeter
        the direction where the heroes must go."""

        # Move to the right
        if direction == "right":
            if self.sprite_x < NB_SPRITE - 1:  # to avoid go out of the screen
                if self.labyrinth.structure[self.sprite_y][self.sprite_x + 1] != "m":  # not to go to a wall
                    # move of a sprite
                    self.sprite_x += 1
                    # Position in pixel:
                    self.x = self.sprite_x * SPRITE_SIZE

        # Move to the left
        if direction == "left":
            if self.sprite_x > 0:  # to avoid go out of the screen
                if self.labyrinth.structure[self.sprite_y][self.sprite_x - 1] != "m":  # not to go to a wall
                    # move of one sprite
                    self.sprite_x -= 1
                    # Position in pixel:
                    self.x = self.sprite_x * SPRITE_SIZE

                    # Move to the bottom
        if direction == "bottom":
            if self.sprite_y < NB_SPRITE - 1:  # to avoid go out of the screen
                if self.labyrinth.structure[self.sprite_y + 1][self.sprite_x] != "m":  # not to go to a wall
                    # move on one sprite
                    self.sprite_y += 1
                    # Position in pixel:
                    self.y = self.sprite_y * SPRITE_SIZE

        # Move to the top
        if direction == "up":
            if self.sprite_y > 0:  # to avoid go out of the screen
                if self.labyrinth.structure[self.sprite_y - 1][self.sprite_x] != "m":  # not to go to a wall
                    # move on one sprite
                    self.sprite_y -= 1
                    # Position in pixel:
                    self.y = self.sprite_y * SPRITE_SIZE