import pygame
from Board import Board
from constants import WIN_SIZE, FPS, MARGIN, SQUARE_SIZE, GRID_SIZE
from Button import Button
from paths import menuPath, imagePath
from Character import Character
from random import randint

pygame.init()
WIN = pygame.display.set_mode((WIN_SIZE[0], WIN_SIZE[1]))
pygame.display.set_caption("Dofus like")
clock = pygame.time.Clock()


def game():
    run = True
    board = Board()
    prevSel = None
    endTurn = False
    playerMovePoint = 5
    moves = None
    attack = None
    bgimg = pygame.image.load(f"{imagePath}background.jpg")
    while run:

        WIN.fill((0, 0, 0))
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
                col = mouseX // (SQUARE_SIZE[0] + MARGIN)
                row = mouseY // (SQUARE_SIZE[1] + MARGIN)

                if row < GRID_SIZE[0] and col < GRID_SIZE[1]:
                    if isinstance(board.grid[row][col], Character) and board.grid[row][col].isOwner(board.turn):  # grid char
                        tileSelected = board.grid[row][col]

                        if prevSel and prevSel != tileSelected and prevSel.isSelected():
                            for i in moves:  # remove old grid moves
                                board.grid[i[0]][i[1]] = 0
                            for i in attack:  # remove old grid moves
                                board.grid[i[0]][i[1]].target = False
                            prevSel.selected = False

                        if tileSelected.isSelected():
                            tileSelected.selected = False
                        else:
                            tileSelected.selected = True

                        moves, attack = tileSelected.getMoves(board, playerMovePoint)
                        for i in moves:
                            if tileSelected.isSelected():
                                if abs(row - i[0] + col - i[1]) <= playerMovePoint:  # if enought playerMovePoint show blue tile
                                    board.grid[i[0]][i[1]] = 1
                            else:
                                board.grid[i[0]][i[1]] = 0

                        for i in attack:
                            if tileSelected.isSelected():
                                board.grid[i[0]][i[1]].target = True
                            else:
                                board.grid[i[0]][i[1]].target = False

                        prevSel = tileSelected

                    elif board.grid[row][col] == 1:  # grid moves
                        for i in moves:  # remove old grid moves
                            board.grid[i[0]][i[1]] = 0
                        moves = None
                        for i in attack:
                            board.grid[i[0]][i[1]].target = False
                        attack = None

                        prevSel.selected = False

                        board.grid[row][col] = prevSel
                        board.grid[prevSel.row][prevSel.col] = 0

                        playerMovePoint -= abs(prevSel.row - row + prevSel.col - col)

                        board.grid[row][col].changePos((row, col))

                        if playerMovePoint <= 0:
                            endTurn = True

                if endTurn:
                    board.updateTurn()
                    endTurn = False
                    playerMovePoint = randint(3, 6)

                board.updatePlayerMove(playerMovePoint)

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
