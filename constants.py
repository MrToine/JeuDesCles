"""
Variables Global qui permet de stocker des infos utiles réutilisable
"""

SIZE_BLOC = 50
NB_BLOC = 12
CENTER = SIZE_BLOC / 2
BORDER_H = 20
SCREEN_H = SIZE_BLOC * NB_BLOC
SCREEN_W = SIZE_BLOC * NB_BLOC

## FILES ##

GAME_TITLE = "Jeu des Clés"
LVL_FILE = "levels/01.lvl"

KEYS = {
    "green" : "src/img/cleverte.gif",
    "blue" : "src/img/clebleue.gif",
    "red" : "src/img/clerouge.gif",
    "gold" : "src/img/cleor.gif",
}

PERSO = {
    "down" : "src/img/persobas.gif",
    "up" : "src/img/persohaut.gif",
    "right" : "src/img/persodroite.gif",
    "left" : "src/img/persoleft.gif",
}

CHEST = "src/img/coffre.gif"
WALL = "src/img/mur.gif"