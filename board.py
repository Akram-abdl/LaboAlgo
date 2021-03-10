import pygame
from constants import SQUARE_SIZE, MARGIN, GRID_SIZE, WIN_SIZE
from Character import Character
from random import randint


class Board:
    def __init__(self):
        self.grid = [[0 for x in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]

        self.playerList = [0, 1]
        self.player = 0
        self.resetMovePoint()

        self.moves = None
        self.atackTargets = None

        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.lblPlayer = None
        self.lblPlayerRect = None
        self.lblPlayerMovePoint = None
        self.lblPlayerMovePointRect = None

        self.initLbl()
        self.initChar()

    def getCellValue(self, row, col):
        return self.grid[row][col]

    def setCellValue(self, row, col, value):
        self.grid[row][col] = value

    def setCellTargetValue(self, row, col, value):
        self.getCellValue(row, col).target = value

    def getRowCol(self, x, y):
        return x // (SQUARE_SIZE[0] + MARGIN), y // (SQUARE_SIZE[1] + MARGIN)

    def isInGrid(self, col, row):
        return row < GRID_SIZE[0] and col < GRID_SIZE[1]

    def updateMovesList(self, cellSelected):
        self.moves, self.attackTargets = cellSelected.getMoves(self)

    def setMoves(self, cellSelected):
        for i in self.moves:
            if cellSelected.isSelected():
                if abs(cellSelected.row - i[0] + cellSelected.col - i[1]) <= self.playerMovePoint:  # if enought playerMovePoint show blue tile
                    self.setCellValue(i[0], i[1], 1)
            else:
                self.setCellValue(i[0], i[1], 0)

    def resetMoves(self):
        for i in self.moves:
            self.setCellValue(i[0], i[1], 0)

    def setAttackTargets(self, cellSelected):
        for i in self.attackTargets:
            if cellSelected.isSelected():
                self.getCellValue(i[0], i[1]).target = True
            else:
                self.getCellValue(i[0], i[1]).target = False

    def resetAttackTargets(self):
        for i in self.attackTargets:
            self.getCellValue(i[0], i[1]).target = False

    def updateCellSelected(self, cellSelected):
        cellSelected.selected = False if cellSelected.isSelected() else True

    def checkEndTurn(self):
        return self.playerMovePoint <= 0

    def resetMovePoint(self):
        self.playerMovePoint = randint(3, 6)

    def initChar(self):
        # Player 0
        self.grid[0][int(GRID_SIZE[1] / 2)] = Character("swordsman", 0, int(GRID_SIZE[1] / 2), 0)
        self.grid[0][int(GRID_SIZE[1] / 2) + 1] = Character("swordsman", 0, int(GRID_SIZE[1] / 2) + 1, 0)

        # Player 1
        self.grid[GRID_SIZE[0] - 1][int(GRID_SIZE[1] / 2)] = Character("archer", GRID_SIZE[0] - 1, int(GRID_SIZE[1] / 2), 1)

    def initLbl(self):
        self.lblPlayer = self.font.render(f"PLAYER {self.player+1}", True, (255, 0, 0))
        self.lblPlayerRect = self.lblPlayer.get_rect()
        self.lblPlayerRect.center = (WIN_SIZE[0] - 170, 100)

        self.lblPlayerMovePoint = self.font.render("Moves : 5", True, (255, 0, 0))
        self.lblPlayerMovePointRect = self.lblPlayerMovePoint.get_rect()
        self.lblPlayerMovePointRect.center = (WIN_SIZE[0] - 170, 200)

    def updateLblPlayerMove(self):
        self.lblPlayerMovePoint = self.font.render(f"Moves : {self.playerMovePoint}", True, (255, 0, 0))

    def nextPlayer(self):
        self.player = self.playerList[(self.player + 1) % len(self.playerList)]
        self.lblPlayer = self.font.render(f"PLAYER {self.player+1}", True, (255, 0, 0))

    def drawBoard(self, win):
        for row in range(GRID_SIZE[0]):
            for column in range(GRID_SIZE[1]):
                color = (204, 202, 202)
                tile = self.grid[row][column]
                if tile == 1:  # grid moves
                    color = (150, 202, 202)
                pygame.draw.rect(
                    win,
                    color,
                    [(MARGIN + SQUARE_SIZE[0]) * column + MARGIN, (MARGIN + SQUARE_SIZE[1]) * row + MARGIN, SQUARE_SIZE[0], SQUARE_SIZE[1]],
                )

                if isinstance(tile, Character):  # grid char
                    if tile.target:
                        pygame.draw.rect(
                            win,
                            (255, 100, 100),
                            [(MARGIN + SQUARE_SIZE[0]) * column + MARGIN, (MARGIN + SQUARE_SIZE[1]) * row + MARGIN, SQUARE_SIZE[0], SQUARE_SIZE[1]],
                        )
                    self.drawChar(tile, win)

        win.blit(self.lblPlayer, self.lblPlayerRect)
        win.blit(self.lblPlayerMovePoint, self.lblPlayerMovePointRect)

    def drawChar(self, char, win):
        win.blit(char.img, ((MARGIN + SQUARE_SIZE[0]) * char.col + MARGIN + 7, (MARGIN + SQUARE_SIZE[1]) * char.row + MARGIN))