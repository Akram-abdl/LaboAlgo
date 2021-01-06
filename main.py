import pygame
from board import Board
from constants import WIN_SIZE, FPS, MARGIN, SQUARE_SIZE, GRID_SIZE
from button import Button
from paths import imagePath

pygame.init()
WIN = pygame.display.set_mode((WIN_SIZE[0], WIN_SIZE[1]))
pygame.display.set_caption("Dofus like")
clock = pygame.time.Clock()


def game():
    run = True
    board = Board()
    spritechar = pygame.image.load('assets\images\sprite\spritechar.png').convert_alpha()
    posX = 460
    posY = 249
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
                column = mouseX // (SQUARE_SIZE[0] + MARGIN)
                row = mouseY // (SQUARE_SIZE[1] + MARGIN)
                
                
                

                if row < GRID_SIZE[0] and column < GRID_SIZE[1]:
                    if board.grid[row][column] == 0:
                        board.grid[row][column] = 1
                    else:
                        board.grid[row][column] = 0
                    
                
                posX = (MARGIN + SQUARE_SIZE[0]) * column + MARGIN 
                posY = (MARGIN + SQUARE_SIZE[1]) * row -11
                
        
            


        board.draw(WIN)
        WIN.blit(spritechar, (posX, posY))
        pygame.display.update()







def settings():
    run = True
    backBtn = Button(f"{imagePath}/menu/back_normal.png", f"{imagePath}/menu/back_hover.png", (700, WIN_SIZE[1] - 100), WIN)
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
    playBtn = Button(f"{imagePath}/menu/start_normal.png", f"{imagePath}/menu/start_hover.png", (700, 200), WIN)
    settingsBtn = Button(f"{imagePath}/menu/settings_normal.png", f"{imagePath}/menu/settings_hover.png", (700, 500), WIN)
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
