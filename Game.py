import pygame
from Board import Board
from paths import imagePath
from Character import Character
from constants import FPS
from Button import Button2


class Game:
    def __init__(self, win, clock):
        self.running = True
        self.clock = clock
        self.win = win
        self.bgImg = pygame.image.load(f"{imagePath}background.jpg")

        # self.test = Button2(500, 500, 94, 94, self.onClick, self.font)

        self.all_buttons = pygame.sprite.Group()

        self.prevSel = None
        self.endTurn = False

        self.board = Board(win, self.all_buttons)

    def run(self):
        while self.running:
            self.win.blit(self.bgImg, (0, 0))
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    col, row = self.board.getRowCol(mouseX, mouseY)

                    if self.board.isInGrid(col, row):
                        cellSelected = self.board.getCellValue(row, col)
                        if isinstance(cellSelected, Character) and cellSelected.isOwner(self.board.player):  # grid char
                            if cellSelected.movePoint <= 0:
                                break

                            if self.prevSel and self.prevSel != cellSelected and self.prevSel.isSelected():
                                self.board.resetMoves()
                                self.board.resetAttackTargets()
                                self.prevSel.selected = False

                            self.board.updateCellSelected(cellSelected)

                            self.board.updateMovesList(cellSelected)

                            self.board.setMoves(cellSelected)
                            self.board.setAttackTargets(cellSelected)
                            self.board.updateSkill(cellSelected)

                            self.prevSel = cellSelected

                        elif cellSelected == 1:  # grid moves
                            self.board.resetMoves()
                            self.board.moves = None
                            self.board.resetAttackTargets()
                            self.board.attackTargets = None

                            self.prevSel.selected = False

                            self.board.updateSkill(cellSelected)

                            movePoint = abs(self.prevSel.row - row + self.prevSel.col - col)

                            self.board.playerMovePoint -= movePoint
                            self.prevSel.movePoint -= movePoint

                            self.board.setCellValue(row, col, self.prevSel)
                            self.board.setCellValue(self.prevSel.row, self.prevSel.col, 0)

                            self.prevSel.changePos((row, col))

                            if self.board.checkEndTurn(self.prevSel):
                                self.endTurn = True

                        elif isinstance(cellSelected, Character) and not cellSelected.isOwner(self.board.player):
                            print("you can attackTargets")

                    if self.endTurn:
                        self.board.nextPlayer()
                        self.endTurn = False
                        self.board.resetMovePoint()
                        for rows in self.board.grid:
                            for cols in rows:
                                if isinstance(cols, Character):
                                    cols.resetMovePoint()

                    self.board.updateLblPlayerMove()

                for button in self.all_buttons:
                    button.handle_event(event)

            self.board.drawBoard()
            self.all_buttons.draw(self.win)
            pygame.display.update()
