import pygame


class Button:
    def __init__(self, img, hover_img, coords, screen):
        self.coords = coords
        self.screen = screen

        self.hovered = False

        self.image = pygame.image.load(img)
        self.image_hover = pygame.image.load(hover_img)

        self.imagerect = self.image.get_rect()
        self.imagerect.topright = self.coords

        self.draw()

        # self.draw_button(screen)

    def draw(self):
        if self.hovered:
            self.screen.blit(self.image_hover, self.imagerect)
        else:
            self.screen.blit(self.image, self.imagerect)
