from constants import CHAR_STATS


class Character:
    def __init__(self, charClass, row, col):
        self.health = CHAR_STATS[charClass]["hp"]
        self.movePoint = CHAR_STATS[charClass]["movePoint"]
        self.mana = CHAR_STATS[charClass]["mana"]
        self.defense = CHAR_STATS[charClass]["defense"]

        self.row = row
        self.col = col

        self.selected = False

    def isSelected(self):
        return self.isSelected

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]