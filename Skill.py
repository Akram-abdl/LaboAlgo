from Button import Button
from constants import WIN_SIZE


class Skill:
    IMG_SIZE = (94, 94)

    def __init__(self, skillInfo, index, win):
        self.name = skillInfo["name"]
        self.pathImg = skillInfo["pathImg"]
        self.pathImgHover = skillInfo["pathImgHover"]
        self.index = index
        self.coords = ((self.IMG_SIZE[0] + 10) * index, WIN_SIZE[1] - self.IMG_SIZE[1] - 10)
        self.win = win
        self.button = Button(self.pathImg, self.pathImgHover, self.coords, self.win)

    def Show(self):
        pass

    def Hide(self):
        pass
