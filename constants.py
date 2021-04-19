from paths import imagePath

WIN_SIZE = [1280, 800]
GRID_SIZE = [10, 15]
SQUARE_SIZE = [60, 60]
MARGIN = 5
FPS = 60

CHAR_STATS = {
    "swordsman": {
        "hp": 70,
        "movePoint": 3,
        "mana": 7,
        "defense": 30,
        "skills": {
            1: {"name": "Coup d'épée", "pathImg": f"{imagePath}skill/sword_attack.png", "pathImgHover": f"{imagePath}skill/sword_attack.png", "manaCost" : 2, "damage" : 10, "range": [[1,0],[-1,0],[0,1],[0,-1]], "damageZone" : [[0,0]]},
            2: {"name": "Épée de la mort", "pathImg": f"{imagePath}skill/dead_sword.png", "pathImgHover": f"{imagePath}skill/dead_sword.png", "manaCost" : 4, "damage" : 20, "range": [[0,0]], "damageZone" : [[1,1],[1,0],[1,-1],[0,1],[0,0],[0,-1],[-1,1],[-1,0],[-1,-1]]},
        },
    },
    "archer": {
        "hp": 50,
        "movePoint": 2,
        "mana": 7,
        "defense": 10,
        "skills": {
            1: {"name": "Tir de flèche", "pathImg": f"{imagePath}skill/arrow_attack.png", "pathImgHover": f"{imagePath}skill/arrow_attack.png", "manaCost" : 2, "damage" : 15, "range": [[4,0],[-4,0],[0,4],[0,-4]], "damageZone" : [[0,0]]},
            2: {"name": "Pluie de flèches", "pathImg": f"{imagePath}skill/arrows_rain_attack.png", "pathImgHover": f"{imagePath}skill/arrows_rain_attack.png", "manaCost" : 4, "damage" : 10, "range": [[3,0],[-3,0],[0,3],[0,-3],[4,0],[-4,0],[0,4],[0,-4],[5,0],[-5,0],[0,5],[0,-5]], "damageZone" : [[1,1],[1,0],[1,-1],[0,1],[0,0],[0,-1],[-1,1],[-1,0],[-1,-1]]},
        },
    },
}
