import pygame
from constants import SQUARE_SIZE, MARGIN, GRID_SIZE, WIN_SIZE
from Character import Character


class Board:
    def __init__(self):
        self.grid = [[0 for x in range(GRID_SIZE[1])] for _ in range(GRID_SIZE[0])]

        self.playerList = [0, 1]
        self.turn = 0

        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.lblPlayer = None
        self.lblPlayerRect = None
        self.lblPlayerMovePoint = None
        self.lblPlayerMovePointRect = None

        self.initLbl()
        self.initChar()

    def initChar(self):
        # Player 0
        self.grid[0][int(GRID_SIZE[1] / 2)] = Character("swordsman", 0, int(GRID_SIZE[1] / 2), 0)
        self.grid[0][int(GRID_SIZE[1] / 2) + 1] = Character("swordsman", 0, int(GRID_SIZE[1] / 2) + 1, 0)

        # Player 1
        self.grid[GRID_SIZE[0] - 1][int(GRID_SIZE[1] / 2)] = Character("archer", GRID_SIZE[0] - 1, int(GRID_SIZE[1] / 2), 1)

    def initLbl(self):
        self.lblPlayer = self.font.render(f"PLAYER {self.turn+1}", True, (255, 0, 0))
        self.lblPlayerRect = self.lblPlayer.get_rect()
        self.lblPlayerRect.center = (WIN_SIZE[0] - 170, 100)

        self.lblPlayerMovePoint = self.font.render("Moves : 5", True, (255, 0, 0))
        self.lblPlayerMovePointRect = self.lblPlayerMovePoint.get_rect()
        self.lblPlayerMovePointRect.center = (WIN_SIZE[0] - 170, 200)

    def updatePlayerMove(self, movePoint):
        self.lblPlayerMovePoint = self.font.render(f"Moves : {movePoint}", True, (255, 0, 0))

    def updateTurn(self):
        self.turn = self.playerList[(self.turn + 1) % len(self.playerList)]
        self.lblPlayer = self.font.render(f"PLAYER {self.turn+1}", True, (255, 0, 0))

    def draw(self, win):
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
                    tile.draw(win)

        win.blit(self.lblPlayer, self.lblPlayerRect)
        win.blit(self.lblPlayerMovePoint, self.lblPlayerMovePointRect)
