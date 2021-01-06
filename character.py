from constants import CHAR_STATS
from constants import SQUARE_SIZE, MARGIN, GRID_SIZE
import pygame


class Character:
    def __init__(self, charClass, row, col):
        self.health = CHAR_STATS[charClass]["hp"]
        self.movePoint = CHAR_STATS[charClass]["movePoint"]
        self.mana = CHAR_STATS[charClass]["mana"]
        self.defense = CHAR_STATS[charClass]["defense"]

        self.img = pygame.image.load("assets\images\sprite\spritechar.png").convert_alpha()

        self.row = row
        self.col = col

        self.selected = False

    def isSelected(self):
        return self.isSelected

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def draw(self, win):
        win.blit(self.img, ((MARGIN + SQUARE_SIZE[0]) * self.col + MARGIN, (MARGIN + SQUARE_SIZE[1]) * self.row + MARGIN))
