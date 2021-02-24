from constants import SQUARE_SIZE, MARGIN, GRID_SIZE, CHAR_STATS
import pygame
from paths import spritePath


class Character:
    def __init__(self, charClass, row, col, player):
        self.health = CHAR_STATS[charClass]["hp"]
        self.movePoint = CHAR_STATS[charClass]["movePoint"]
        self.mana = CHAR_STATS[charClass]["mana"]
        self.defense = CHAR_STATS[charClass]["defense"]

        self.img = pygame.image.load(f"{spritePath}{charClass}.png").convert_alpha()

        self.player = player

        self.row = row
        self.col = col

        self.selected = False

        self.target = False

    def isOwner(self, player):
        return self.player == player

    def isSelected(self):
        return self.selected

    def changePos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def getMoves(self, board, playerMovePoint):
        moves = []
        attack = []

        for i in range(1, self.movePoint + 1):
            if i > playerMovePoint:
                break
            if self.row + i < GRID_SIZE[0]:
                moves.append((self.row + i, self.col))
            if self.row - i >= 0:
                moves.append((self.row - i, self.col))
            if self.col + i < GRID_SIZE[1]:
                moves.append((self.row, self.col + i))
            if self.col - i >= 0:
                moves.append((self.row, self.col - i))

        for i in moves:
            if isinstance(board.grid[i[0]][i[1]], Character):
                moves.remove(i)
                if board.grid[i[0]][i[1]].player != board.turn:
                    attack.append(i)

        return moves, attack
