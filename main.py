import pygame
from board import Board
from constants import WIN_SIZE, FPS, MARGIN, SQUARE_SIZE


pygame.init()
WIN = pygame.display.set_mode((WIN_SIZE[0], WIN_SIZE[1]))
pygame.display.set_caption("Dofus like")


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                column = pos[0] // (SQUARE_SIZE[0] + MARGIN)
                row = pos[1] // (SQUARE_SIZE[1] + MARGIN)

                board.grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)

        board.draw_grid(WIN)
        pygame.display.update()


if __name__ == "__main__":
    main()
