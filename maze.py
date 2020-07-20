#!/usr/bin/python3
# -*-coding:utf-8 -
"""Place where Classes are """
import random
import time

from constantes import *


class Maze():
    """class Maze which define the labyrinth.
    It has one attribut : an empty grid.
    and takes as parameter the file which contains the map.
    This class has two methods: one to generate the structure : a list of list
    and one to display the grid over the pygame window."""

    def __init__(self, file):
        self.file = file
        self.structure = []

    def generate(self):
        """Method which generate the structure from the file.txt"""
        frame = []
        # let generate the list of lists
        with open(self.file, "r") as file:
            for line in file:
                line = line.strip()  # be careful to cut the line break
                frame.append(list(line))
        self.structure = frame  # we get the list of lists in the attribut

    def display(self, screen):
        """from the grid we display each sprite match with a code :
        "m" for picture of a wall , "a" for the guardian. Each sprite have
        x and y coordinates and a size in pixel."""
        number_line = 0  # we begin with the first list so the fist line
        for line in self.structure:
            number_sprite = 0  # we begin with the first square
            for sprite in line:
                X = number_sprite * SPRITE_SIZE
                Y = number_line * SPRITE_SIZE
                if sprite == "m":
                    screen.blit(WALL, (X + 30, Y + 30))  # we load a wall image over the screen
                if sprite == "a":  # we add 30 for the offset of the black outline
                    screen.blit(ARRIVAL, (X + 30, Y + 30))  # we load a arrival picture over the window
                number_sprite += 1
            number_line += 1


