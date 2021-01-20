import pygame
from constants import SQUARE_SIZE, MARGIN, GRID_SIZE, WIN_SIZE
from character import Character


class Board:
    def __init__(self):
        self.grid = [[0 for x in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]

        self.grid[0][int(GRID_SIZE[1] / 2)] = Character("swordsman", 0, int(GRID_SIZE[1] / 2), 0)
        self.grid[0][int(GRID_SIZE[1] / 2) + 1] = Character("swordsman", 0, int(GRID_SIZE[1] / 2) + 1, 0)

        self.grid[GRID_SIZE[0] - 1][int(GRID_SIZE[1] / 2)] = Character("archer", GRID_SIZE[0] - 1, int(GRID_SIZE[1] / 2), 1)

        self.playerList = [0, 1]
        self.turn = 0

        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.lblPlayer = self.font.render(f"PLAYER {self.turn}", True, (255, 0, 0))
        self.lblPlayerRect = self.lblPlayer.get_rect()
        self.lblPlayerRect.center = (WIN_SIZE[0] - 170, 100)

        self.lblPlayerMovePoint = self.font.render("Moves : 5", True, (255, 0, 0))
        self.lblPlayerMovePointRect = self.lblPlayerMovePoint.get_rect()
        self.lblPlayerMovePointRect.center = (WIN_SIZE[0] - 170, 200)

    def updatePlayerMove(self, movePoint):
        self.lblPlayerMovePoint = self.font.render(f"Move : {movePoint}", True, (255, 0, 0))

    def updateTurn(self):
        self.turn = self.playerList[(self.turn + 1) % len(self.playerList)]
        self.lblPlayer = self.font.render(f"PLAYER {self.turn+1}", True, (255, 0, 0))

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

        win.blit(self.lblPlayer, self.lblPlayerRect)
        win.blit(self.lblPlayerMovePoint, self.lblPlayerMovePointRect)
