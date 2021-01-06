from constants import SQUARE_SIZE, MARGIN, GRID_SIZE, CHAR_STATS
import pygame
from paths import spritePath


class Character:
    def __init__(self, charClass, row, col, player):
        self.health = CHAR_STATS[charClass]["hp"]
        self.movePoint = CHAR_STATS[charClass]["movePoint"]
        self.mana = CHAR_STATS[charClass]["mana"]
        self.defense = CHAR_STATS[charClass]["defense"]

        self.img = pygame.image.load(f"{spritePath}spritechar.png").convert_alpha()

        self.player = player

        self.row = row
        self.col = col

        self.selected = False

    def isOwner(self, player):
        return self.player == player

    def isSelected(self):
        return self.selected

    def changePos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def draw(self, win):
        win.blit(self.img, ((MARGIN + SQUARE_SIZE[0]) * self.col + MARGIN, (MARGIN + SQUARE_SIZE[1]) * self.row + MARGIN))

    def getMoves(self, board):
        moves = []

        for i in range(1, self.movePoint + 1):
            if self.row + i < GRID_SIZE[0]:
                moves.append((self.row + i, self.col))
            if self.row - i >= 0:
                moves.append((self.row - i, self.col))
            if self.col + i < GRID_SIZE[1]:
                moves.append((self.row, self.col + i))
            if self.col - i >= 0:
                moves.append((self.row, self.col - i))

        print(moves)
        for i in moves:
            # print("--")
            # print(i)
            if isinstance(board.grid[i[0]][i[1]], Character):
                # print("oui")
                moves.remove(i)
        print("===")
        print(moves)

        return moves
