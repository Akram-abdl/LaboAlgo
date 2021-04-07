import pygame
from paths import imagePath


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

    def draw(self):
        if self.hovered:
            self.screen.blit(self.image_hover, self.imagerect)
        else:
            self.screen.blit(self.image, self.imagerect)


class Button2(pygame.sprite.Sprite):
    def __init__(
        self,
        x,
        y,
        width,
        height,
        callback,
        font,
        text="",
        text_color=(0, 0, 0),
        image_normal=f"{imagePath}skill/sword_attack.png",
        image_hover=f"{imagePath}skill/sword_attack.png",
        image_down=f"{imagePath}skill/sword_attack.png",
    ):
        super().__init__()
        # Scale the images to the desired size (doesn't modify the originals).
        self.image_normal = pygame.image.load(image_normal)
        self.image_hover = pygame.image.load(image_hover)
        self.image_down = pygame.image.load(image_hover)

        self.image = self.image_normal  # The currently active image.
        self.rect = self.image.get_rect(topleft=(x, y))
        # To center the text rect.
        image_center = self.image.get_rect().center
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=image_center)
        # Blit the text onto the images.
        for image in (self.image_normal, self.image_hover, self.image_down):
            image.blit(text_surf, text_rect)

        # This function will be called when the button gets pressed.
        self.callback = callback
        self.button_down = False

        self.show = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.image = self.image_down
                self.button_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # If the rect collides with the mouse pos.
            if self.rect.collidepoint(event.pos) and self.button_down:
                self.callback()  # Call the function.
                self.image = self.image_hover
            self.button_down = False
        elif event.type == pygame.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.button_down:
                self.image = self.image_hover
            elif not collided:
                self.image = self.image_normal
