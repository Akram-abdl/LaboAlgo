import pygame
from Button import Button2
from constants import WIN_SIZE


class Skill:
    IMG_SIZE = (94, 94)

    def __init__(self, skillInfo, index, win, all_buttons, grid, row, col):
        self.name = skillInfo["name"]
        self.pathImg = skillInfo["pathImg"]
        self.pathImgHover = skillInfo["pathImgHover"]
        self.range = skillInfo["range"]
        self.damageZone = skillInfo["damageZone"]
        self.index = index
        self.all_buttons = all_buttons
        self.grid = grid
        self.charPos = (row, col)
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
            print("removed")

    def onClick(self):
        colorRange = (255, 87, 51)
        colorDamage = (255, 0, 0)
        rangeCell = []
        for cell in self.range:
            rangeCell.append([self.charPos[0]+cell[0], self.charPos[1]+cell[1]])
        # damageCell = []
        # pygame.draw.rect(
        #     self.win,
        #     colorRange,
        #     [(MARGIN + SQUARE_SIZE[0]) * column + MARGIN, (MARGIN + SQUARE_SIZE[1]) * row + MARGIN, SQUARE_SIZE[0], SQUARE_SIZE[1]],
        # )
        print(rangeCell)