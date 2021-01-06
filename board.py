import pygame
from constants import SQUARE_SIZE, MARGIN, GRID_SIZE
from character import Character


class Board:
    def __init__(self):
        self.grid = [[0 for x in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]

        self.grid[0][int(GRID_SIZE[1] / 2)] = Character("swordsman", 0, int(GRID_SIZE[1] / 2))

    def draw(self, win):
        for row in range(GRID_SIZE[0]):
            for column in range(GRID_SIZE[1]):
                color = (204, 202, 202)
                pygame.draw.rect(
                    win,
                    color,
                    [(MARGIN + SQUARE_SIZE[0]) * column + MARGIN, (MARGIN + SQUARE_SIZE[1]) * row + MARGIN, SQUARE_SIZE[0], SQUARE_SIZE[1]],
                )
                if self.grid[row][column] == 1:
                    color = (150, 202, 202)
                    pygame.draw.rect(
                        win,
                        color,
                        [(MARGIN + SQUARE_SIZE[0]) * column + MARGIN, (MARGIN + SQUARE_SIZE[1]) * row + MARGIN, SQUARE_SIZE[0], SQUARE_SIZE[1]],
                    )
                elif self.grid[row][column] != 0:
                    self.grid[row][column].draw(win)
