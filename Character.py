from constants import SQUARE_SIZE, MARGIN, GRID_SIZE, CHAR_STATS
import pygame
from paths import spritePath
from Skill import Skill


class Character(pygame.sprite.Sprite):
    def __init__(self, charClass, pos, player, index, win, all_buttons, grid):
        self.health = CHAR_STATS[charClass]["hp"]
        self.movePoint = CHAR_STATS[charClass]["movePoint"]
        self.mana = CHAR_STATS[charClass]["mana"]
        self.defense = CHAR_STATS[charClass]["defense"]
        self.charClass = charClass

        self.all_buttons = all_buttons
        self.grid = grid

        self.img = pygame.image.load(f"{spritePath}{charClass}.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.row = pos[0]
        self.col = pos[1]
        self.rect.x = self.getX()
        self.rect.y = self.getY()
        self.player = player

        self.win = win

        self.skills = []

        self.selected = False

        self.target = False

    def __str__(self):
        return "oui"

    def initSkills(self):
        print("initSkill()")
        self.skills = []
        for index, skill in CHAR_STATS[self.charClass]["skills"].items():
            new_skill = Skill(skill, index, self.win, self.all_buttons, self.grid, self.row, self.col)
            self.skills.append(new_skill)

    def isOwner(self, player):
        return self.player == player

    def isSelected(self):
        return self.selected

    def getX(self):
        return (MARGIN + SQUARE_SIZE[0]) * self.col + MARGIN + 7

    def getY(self):
        return (MARGIN + SQUARE_SIZE[1]) * self.row + MARGIN

    def resetMovePoint(self):
        self.movePoint = CHAR_STATS[self.charClass]["movePoint"]

    def changePos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

        self.rect.x = self.getX()
        self.rect.y = self.getY()

    def getMoves(self, board):
        self.initSkills()
        moves = []
        attack = []
        print("getMoves()")
        for i in range(1, self.movePoint + 1):
            if i > board.playerMovePoint:
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
                if board.grid[i[0]][i[1]].player != board.player:
                    attack.append(i)

        return moves, attack
