from constants import CHAR_STATS
from constants import SQUARE_SIZE, MARGIN, GRID_SIZE
import pygame


class Character:
    def __init__(self, charClass, row, col):
        self.health = CHAR_STATS[charClass]["hp"]
        self.movePoint = CHAR_STATS[charClass]["movePoint"]
        self.mana = CHAR_STATS[charClass]["mana"]
        self.defense = CHAR_STATS[charClass]["defense"]

        self.row = row
        self.col = col

        self.selected = False

    def isSelected(self):
        return self.isSelected

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def draw(self, win):
        color = (255, 0, 0)
        pygame.draw.rect(
            win,
            color,
            [
                (MARGIN + SQUARE_SIZE[0]) * self.col + 7 + MARGIN,
                (MARGIN + SQUARE_SIZE[1]) * self.row + 7 + MARGIN,
                SQUARE_SIZE[0] - 15,
                SQUARE_SIZE[1] - 15,
            ],
        )
