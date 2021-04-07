import pygame
from Button import Button2
from constants import WIN_SIZE


class Skill:
    IMG_SIZE = (94, 94)

    def __init__(self, skillInfo, index, win, all_buttons):
        self.name = skillInfo["name"]
        self.pathImg = skillInfo["pathImg"]
        self.pathImgHover = skillInfo["pathImgHover"]
        self.index = index
        self.all_buttons = all_buttons
        self.x = (self.IMG_SIZE[0] + 10) * index
        self.y = WIN_SIZE[1] - self.IMG_SIZE[1] - 10
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.button = Button2(
            self.x,
            self.y,
            self.IMG_SIZE[0],
            self.IMG_SIZE[1],
            self.onClick,
            self.font,
            image_normal=self.pathImg,
            image_hover=self.pathImgHover,
            image_down=self.pathImgHover,
        )
        self.hide()

    def show(self):
        self.button.show = True
        if self.button not in self.all_buttons:
            self.all_buttons.add(self.button)

    def hide(self):
        self.button.show = False
        if self.button in self.all_buttons:
            self.all_buttons.remove(self.button)

    def onClick(self):
        print(f"name:{self.name}")
