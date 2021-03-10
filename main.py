import pygame
from Board import Board
from constants import WIN_SIZE, FPS
from Button import Button
from paths import menuPath, imagePath
from Character import Character

pygame.init()
WIN = pygame.display.set_mode((WIN_SIZE[0], WIN_SIZE[1]))
pygame.display.set_caption("Dofus like")
clock = pygame.time.Clock()


def game():
    run = True
    board = Board()
    prevSel = None
    endTurn = False
    bgimg = pygame.image.load(f"{imagePath}background.jpg")
    while run:
        WIN.blit(bgimg, (0, 0))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                col, row = board.getRowCol(mouseX, mouseY)

                if board.isInGrid(col, row):
                    cellSelected = board.getCellValue(row, col)
                    if isinstance(cellSelected, Character) and cellSelected.isOwner(board.player):  # grid char

                        if prevSel and prevSel != cellSelected and prevSel.isSelected():
                            board.resetMoves()
                            board.resetAttackTargets()
                            prevSel.selected = False

                        board.updateCellSelected(cellSelected)

                        board.updateMovesList(cellSelected)

                        board.setMoves(cellSelected)
                        board.setAttackTargets(cellSelected)

                        prevSel = cellSelected

                    elif cellSelected == 1:  # grid moves
                        board.resetMoves()
                        board.moves = None
                        board.resetAttackTargets()
                        board.attackTargets = None

                        prevSel.selected = False

                        board.playerMovePoint -= abs(prevSel.row - row + prevSel.col - col)

                        board.setCellValue(row, col, prevSel)
                        board.setCellValue(prevSel.row, prevSel.col, 0)

                        prevSel.changePos((row, col))

                        if board.checkEndTurn():
                            endTurn = True

                    elif isinstance(cellSelected, Character) and board.grid[row][col]:
                        print("you can attackTargets")

                if endTurn:
                    board.nextPlayer()
                    endTurn = False
                    board.resetMovePoint()

                board.updateLblPlayerMove()

                print(f"Click ({mouseX} {mouseY}) | Grid coordinates: {row} {col}")

        board.drawBoard(WIN)
        pygame.display.update()


def settings():
    run = True
    backBtn = Button(f"{menuPath}back_normal.png", f"{menuPath}back_hover.png", (700, WIN_SIZE[1] - 100), WIN)
    while run:
        WIN.fill((0, 0, 0))
        clock.tick(FPS)

        mousePos = pygame.mouse.get_pos()

        backBtn.hovered = backBtn.imagerect.collidepoint(mousePos)
        backBtn.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if backBtn.hovered:
                    run = False
                    break

        pygame.display.update()


def main_menu():
    playBtn = Button(f"{menuPath}start_normal.png", f"{menuPath}start_hover.png", (700, 200), WIN)
    settingsBtn = Button(f"{menuPath}settings_normal.png", f"{menuPath}settings_hover.png", (700, 500), WIN)
    while True:
        WIN.fill((0, 0, 0))
        clock.tick(FPS)

        mousePos = pygame.mouse.get_pos()

        playBtn.hovered = playBtn.imagerect.collidepoint(mousePos)
        playBtn.draw()
        settingsBtn.hovered = settingsBtn.imagerect.collidepoint(mousePos)
        settingsBtn.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if playBtn.hovered:
                    game()
                elif settingsBtn.hovered:
                    settings()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
