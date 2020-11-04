import constants

class char:

    def __init__(self, type):
        self.health = constants.CHAR_STATS[type]["hp"]
        self.pointMouvement = constants.CHAR_STATS[type]["pointMouvement"]
        self.mana = constants.CHAR_STATS[type]["mana"]
        self.defense = constants.CHAR_STATS[type]["defense"]

    def startTurn():
        self.move = constants.CHAR_STATS[type]["pointMouvement"]
        self.mana = constants.CHAR_STATS[type]["mana"]

    def bouger(pc, pm):
        coutpdm = abs(pc[0]-pm[0])+abs(pc[1]-pm[1])
        if coutpdm <= self.pointMouvement :
            self.position = pm
            self.pointMouvement -= coutpdm
        else :
            print("Pas assez de pdm")


    def takeDmg(dmg):
        self.health -= dmg
        if self.health <= 0:
            self.die()        
        
    def endTurn():


    def die():