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
            1: {"name": "Coup d'épée", "pathImg": f"{imagePath}skill/sword_attack.png", "pathImgHover": f"{imagePath}skill/sword_attack.png"},
            2: {"name": "Épée de la mort", "pathImg": f"{imagePath}skill/dead_sword.png", "pathImgHover": f"{imagePath}skill/dead_sword.png"},
        },
    },
    "archer": {
        "hp": 50,
        "movePoint": 2,
        "mana": 7,
        "defense": 10,
        "skills": {
            1: {"name": "Tire de flèche", "pathImg": f"{imagePath}skill/arrow_attack.png", "pathImgHover": f"{imagePath}skill/arrow_attack.png"}
        },
    },
}
