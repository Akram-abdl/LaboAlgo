import pygame
from constants import SQUARE_SIZE, MARGIN, GRID_SIZE


class Board:
    def __init__(self):
        self.grid = []

        for row in range(GRID_SIZE[0]):
            self.grid.append([])
            for column in range(GRID_SIZE[1]):
                self.grid[row].append(0)  # Append a cell

    def draw_grid(self, win):
        for row in range(GRID_SIZE[0]):
            for column in range(GRID_SIZE[1]):
                color = (255, 255, 255)
                if self.grid[row][column] == 1:
                    color = (204, 202, 202)
                pygame.draw.rect(
                    win,
                    color,
                    [(MARGIN + SQUARE_SIZE[0]) * column + MARGIN, (MARGIN + SQUARE_SIZE[1]) * row + MARGIN, SQUARE_SIZE[0], SQUARE_SIZE[1]],
                )
