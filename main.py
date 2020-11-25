import pygame
from board import Board
from constants import WIN_SIZE, FPS, MARGIN, SQUARE_SIZE
from button import Button
from paths import imagePath

pygame.init()
WIN = pygame.display.set_mode((WIN_SIZE[0], WIN_SIZE[1]))
pygame.display.set_caption("Dofus like")


def game():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        WIN.fill((0, 0, 0))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                column = mouseX // (SQUARE_SIZE[0] + MARGIN)
                row = mouseY // (SQUARE_SIZE[1] + MARGIN)

                if board.grid[row][column] == 0:
                    board.grid[row][column] = 1
                else:
                    board.grid[row][column] = 0
                print(f"Click ({mouseX} {mouseY}) | Grid coordinates: {row} {column}")

        board.draw_grid(WIN)
        pygame.display.update()


def settings():
    backBtn = Button(f"{imagePath}/menu/back_normal.png", f"{imagePath}/menu/back_hover.png", (700, WIN_SIZE[1] - 100), WIN)
    run = True
    clock = pygame.time.Clock()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if backBtn.hovered:
                    run = False
                    break

        pygame.display.update()


def main_menu():
    playBtn = Button(f"{imagePath}/menu/start_normal.png", f"{imagePath}/menu/start_hover.png", (700, 200), WIN)
    settingsBtn = Button(f"{imagePath}/menu/settings_normal.png", f"{imagePath}/menu/settings_hover.png", (700, 500), WIN)
    clock = pygame.time.Clock()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playBtn.hovered:
                    game()
                elif settingsBtn.hovered:
                    settings()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
