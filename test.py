import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 

WIDTH = 40
HEIGHT = 40
 

MARGIN = 10
 

grid = []
for row in range(10):
    
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
 

grid[1][5] = 1
 

pygame.init()
 

WINDOW_SIZE = [510, 510]
screen = pygame.display.set_mode(WINDOW_SIZE)
 

pygame.display.set_caption("game")
 

done = False
 

clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()
            
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    
    screen.fill(BLACK)
 
    
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    
    clock.tick(60)
 
    
    pygame.display.flip()
 

pygame.quit()