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
        return self.selected

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def draw(self, win):
        win.blit(self.img, ((MARGIN + SQUARE_SIZE[0]) * self.col + MARGIN, (MARGIN + SQUARE_SIZE[1]) * self.row + MARGIN))

    def getMoves(self):
        i = self.row
        j = self.col
        moves = []

        if i + 1 < GRID_SIZE[0]:
            moves.append((i + 1, j))
        if i - 1 >= 0:
            moves.append((i - 1, j))
        if j + 1 < GRID_SIZE[1]:
            moves.append((i, j + 1))
        if j - 1 >= 0:
            moves.append((i, j - 1))

        print(moves)

        return moves

    def showMoves(self, win):
        moves = self.getMoves()
