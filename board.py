import pygame
from constants import SQUARE_SIZE, MARGIN, GRID_SIZE
from character import Character
from itertools import cycle


class Board:
    def __init__(self):
        self.grid = [[0 for x in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]

        self.grid[0][int(GRID_SIZE[1] / 2)] = Character("swordsman", 0, int(GRID_SIZE[1] / 2), 0)

        self.grid[GRID_SIZE[0] - 1][int(GRID_SIZE[1] / 2)] = Character("swordsman", GRID_SIZE[0] - 1, int(GRID_SIZE[1] / 2), 1)

        self.playerList = [0, 1]
        self.turn = 1

    def draw(self, win):
        for row in range(GRID_SIZE[0]):
            for column in range(GRID_SIZE[1]):
                color = (204, 202, 202)
                if self.grid[row][column] == 1:  # grid moves
                    color = (150, 202, 202)
                pygame.draw.rect(
                    win,
                    color,
                    [(MARGIN + SQUARE_SIZE[0]) * column + MARGIN, (MARGIN + SQUARE_SIZE[1]) * row + MARGIN, SQUARE_SIZE[0], SQUARE_SIZE[1]],
                )

                if isinstance(self.grid[row][column], Character):  # grid char
                    self.grid[row][column].draw(win)
