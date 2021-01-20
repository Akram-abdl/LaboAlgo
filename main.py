import pygame
from board import Board
from constants import WIN_SIZE, FPS, MARGIN, SQUARE_SIZE, GRID_SIZE
from button import Button
from paths import menuPath
from character import Character

pygame.init()
WIN = pygame.display.set_mode((WIN_SIZE[0], WIN_SIZE[1]))
pygame.display.set_caption("Dofus like")
clock = pygame.time.Clock()


def game():
    run = True
    board = Board()
    oldSel = None
    endTurn = False
    playerMovePoint = 5
    while run:
        WIN.fill((0, 0, 0))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                col = mouseX // (SQUARE_SIZE[0] + MARGIN)
                row = mouseY // (SQUARE_SIZE[1] + MARGIN)

                if row < GRID_SIZE[0] and col < GRID_SIZE[1]:
                    if isinstance(board.grid[row][col], Character) and board.grid[row][col].isOwner(board.turn):  # grid char
                        tileSelected = board.grid[row][col]
                        if tileSelected.isSelected():
                            tileSelected.selected = False
                        else:
                            tileSelected.selected = True

                        moves = tileSelected.getMoves(board)
                        for i in moves:
                            if tileSelected.isSelected():
                                if abs(row - i[0] + col - i[1]) <= playerMovePoint:  # if enought playerMovePoint show blue tile
                                    board.grid[i[0]][i[1]] = 1
                            else:
                                board.grid[i[0]][i[1]] = 0

                        oldSel = tileSelected

                    elif board.grid[row][col] == 1:  # grid moves
                        for i in moves:  # remove old grid moves
                            board.grid[i[0]][i[1]] = 0
                        oldSel.selected = False

                        board.grid[row][col] = oldSel
                        board.grid[oldSel.row][oldSel.col] = 0

                        playerMovePoint -= abs(oldSel.row - row + oldSel.col - col)

                        board.grid[row][col].changePos((row, col))

                        if playerMovePoint <= 0:
                            endTurn = True

                if endTurn:
                    board.updateTurn()
                    endTurn = False
                    playerMovePoint = 5

                board.updatePlayerMove(playerMovePoint)

                print(f"Click ({mouseX} {mouseY}) | Grid coordinates: {row} {col}")

        board.draw(WIN)
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
