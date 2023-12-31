from random import randint

import pygame
from pygame.locals import *

TOMBER1 = USEREVENT + 1
TOMBER2 = USEREVENT + 2
PERDU = USEREVENT + 3
LIGNE = USEREVENT + 4
STOP = USEREVENT + 5
J2 = USEREVENT + 6

vitesse_tetra = 600  # la vitesse de base des tetraminos
size = 30
tetraminos = [
    [(1, 1), (1, 2), (2, 1), (2, 2)],
    [(1, 1), (2, 1), (2, 2), (3, 2)],
    [(1, 2), (2, 1), (2, 2), (3, 1)],
    [(1, 1), (2, 1), (3, 1), (4, 1)],
    [(1, 1), (1, 2), (1, 3), (2, 2)],
    [(1, 1), (1, 2), (2, 2), (3, 2)],
    [(1, 1), (1, 2), (2, 1), (3, 1)],
]

red = ((249, 104, 84), (204, 51, 19), (240, 75, 40))
yellow = ((249, 209, 85), (221, 172, 19), (245, 193, 30))
blue = ((118, 191, 255), (57, 141, 216), (65, 161, 247))
green = ((93, 220, 137), (40, 170, 89), (42, 202, 98))
purple = ((153, 113, 239), (111, 69, 227), (136, 86, 245))
turquoise = ((103, 231, 212), (57, 190, 170), (50, 216, 191))
orange = ((251, 156, 76), (215, 113, 27), (249, 136, 43))
noir = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
redfantome = ((114, 63, 63), (98, 46, 38), (117, 51, 51))
yellowfantome = ((83, 84, 83), (76, 74, 42), (83, 77, 65))
bluefantome = ((53, 75, 99), (33, 56, 90), (35, 65, 91))
greenfantome = ((36, 61, 31), (11, 48, 8), (18, 55, 2))
purplefantome = ((83, 60, 98), (65, 41, 81), (77, 47, 97))
turquoisefantome = ((66, 87, 115), (27, 78, 107), (35, 89, 113))
orangefantome = ((127, 97, 75), (117, 77, 47), (129, 87, 55))

color = {
    0: noir,
    1: red,
    2: yellow,
    3: blue,
    4: green,
    5: purple,
    6: turquoise,
    7: orange,
}
color_fantome = {
    1: redfantome,
    2: yellowfantome,
    3: bluefantome,
    4: greenfantome,
    5: purplefantome,
    6: turquoisefantome,
    7: orangefantome,
}
score_ligne = {1: 100, 2: 300, 3: 600, 4: 400}


def carre(screen, pos, marge_grille, couleur):
    """Dessine un carre de tetramino"""
    pos = (pos[0] - 1, pos[1] - 1)
    pygame.draw.rect(
        screen,
        couleur[0],
        (marge_grille[0] + pos[0] * size, marge_grille[1] + pos[1] * size, size, size),
    )
    pygame.draw.polygon(
        screen,
        couleur[1],
        (
            [marge_grille[0] + pos[0] * size, marge_grille[1] + pos[1] * size + size],
            [
                marge_grille[0] + pos[0] * size + size,
                marge_grille[1] + pos[1] * size + size,
            ],
            [marge_grille[0] + pos[0] * size + size, marge_grille[1] + pos[1] * size],
        ),
    )
    pygame.draw.rect(
        screen,
        couleur[2],
        (
            marge_grille[0] + pos[0] * size + round(size / 8),
            marge_grille[1] + pos[1] * size + round(size / 8),
            size * (6 / 8),
            size * (6 / 8),
        ),
    )


class tetramino:
    def __init__(self, screen, marge_grille, pos=False, couleur=False):
        """Crée le tétramino"""
        if couleur != False:
            self.couleur = int(couleur)
        else:
            self.couleur = randint(1, 7)  # On ne prends pas le 0 car c'est le noir

        if pos != False:
            self.numpos = int(pos)
        else:
            self.numpos = randint(0, 6)

        self.pos = tetraminos[self.numpos]
        self.screen = screen
        self.marge = marge_grille

    def __repr__(self):
        """Permet de visualiser le tetramino"""
        return "pos:" + str(self.pos) + "  /  couleur:" + str(self.couleur)

    def taille(self):
        """Fonction qui calcul la largueur et la longueur maximale du tétramino, les renvois, ainis que les coordonnés(x,y) les plus petites"""
        xmin = 99
        xmax = 0
        ymin = 99
        ymax = 0
        for x, y in self.pos:
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x

            if y < ymin:
                ymin = y
            if y > ymax:
                ymax = y

        X = xmax - xmin + 1  # Le +1 est la taille du premier carré
        Y = ymax - ymin + 1

        return (xmin, ymin, X, Y)

    def a_tourner(self):
        """Calcul les valeurs (xmin,ymin,longueur) du carré minimum à faire tourner pour la rotation du tétramino"""
        (xmin, ymin, X, Y) = self.taille()

        dec = 0
        L = X
        (x_carre, y_carre) = (xmin, ymin)

        if Y < X:
            dec = X - Y
            y_carre = ymin - dec

        elif Y > X:
            L = Y
        return (x_carre, y_carre, L, -dec)

    def draw(self, pos, marge):
        """Dessine le tetramino sur la fenetre"""
        for positions in pos:
            carre(self.screen, positions, marge, color[self.couleur])

    def affiche(self, avant, apres, hors=[], fantome=False):
        """Redessine le tetramino, les positions dessinées ne doivent pas faire partie de hors"""
        ### Efface les valeurs qu'on ne garde pas
        for val in avant:
            if not (val in apres or val in hors):
                carre(self.screen, val, self.marge, noir)

        ### Defini la couleur à dessiner
        if not fantome:
            couleur = color[self.couleur]
        else:
            couleur = color_fantome[self.couleur]

        ### Dessine les carres manquants pour compléter la nouvelle position du tétramino
        for val in apres:
            if not (val in avant or val in hors):
                carre(self.screen, val, self.marge, couleur)

    def centrer(self, taille_grille):
        """Centre un tetramino dans la grille"""

        ### CALCUL DU DECALAGE NECESSAIRE POUR CENTRER
        dec = int(taille_grille[0] / 2 - ((self.taille()[2]) / 2))

        ### CALCUL DES NOUVELLES POSITIONS
        newposition = []
        for x, y in self.pos:
            newposition.append((x + dec, y))

        self.pos = newposition


class Grille:
    def __init__(
        self,
        screen,
        petit=False,
        position=(50, 50),
        marge=30,
        taille_next=6,
        numero=1,
        malus=0,
        reseau=False,
    ):
        if petit == False:
            self.taille = (10, 20)
            self.plateau = {
                (1, 1): 0,
                (1, 2): 0,
                (1, 3): 0,
                (1, 4): 0,
                (1, 5): 0,
                (1, 6): 0,
                (1, 7): 0,
                (1, 8): 0,
                (1, 9): 0,
                (1, 10): 0,
                (1, 11): 0,
                (1, 12): 0,
                (1, 13): 0,
                (1, 14): 0,
                (1, 15): 0,
                (1, 16): 0,
                (1, 17): 0,
                (1, 18): 0,
                (1, 19): 0,
                (1, 20): 0,
                (2, 1): 0,
                (2, 2): 0,
                (2, 3): 0,
                (2, 4): 0,
                (2, 5): 0,
                (2, 6): 0,
                (2, 7): 0,
                (2, 8): 0,
                (2, 9): 0,
                (2, 10): 0,
                (2, 11): 0,
                (2, 12): 0,
                (2, 13): 0,
                (2, 14): 0,
                (2, 15): 0,
                (2, 16): 0,
                (2, 17): 0,
                (2, 18): 0,
                (2, 19): 0,
                (2, 20): 0,
                (3, 1): 0,
                (3, 2): 0,
                (3, 3): 0,
                (3, 4): 0,
                (3, 5): 0,
                (3, 6): 0,
                (3, 7): 0,
                (3, 8): 0,
                (3, 9): 0,
                (3, 10): 0,
                (3, 11): 0,
                (3, 12): 0,
                (3, 13): 0,
                (3, 14): 0,
                (3, 15): 0,
                (3, 16): 0,
                (3, 17): 0,
                (3, 18): 0,
                (3, 19): 0,
                (3, 20): 0,
                (4, 1): 0,
                (4, 2): 0,
                (4, 3): 0,
                (4, 4): 0,
                (4, 5): 0,
                (4, 6): 0,
                (4, 7): 0,
                (4, 8): 0,
                (4, 9): 0,
                (4, 10): 0,
                (4, 11): 0,
                (4, 12): 0,
                (4, 13): 0,
                (4, 14): 0,
                (4, 15): 0,
                (4, 16): 0,
                (4, 17): 0,
                (4, 18): 0,
                (4, 19): 0,
                (4, 20): 0,
                (5, 1): 0,
                (5, 2): 0,
                (5, 3): 0,
                (5, 4): 0,
                (5, 5): 0,
                (5, 6): 0,
                (5, 7): 0,
                (5, 8): 0,
                (5, 9): 0,
                (5, 10): 0,
                (5, 11): 0,
                (5, 12): 0,
                (5, 13): 0,
                (5, 14): 0,
                (5, 15): 0,
                (5, 16): 0,
                (5, 17): 0,
                (5, 18): 0,
                (5, 19): 0,
                (5, 20): 0,
                (6, 1): 0,
                (6, 2): 0,
                (6, 3): 0,
                (6, 4): 0,
                (6, 5): 0,
                (6, 6): 0,
                (6, 7): 0,
                (6, 8): 0,
                (6, 9): 0,
                (6, 10): 0,
                (6, 11): 0,
                (6, 12): 0,
                (6, 13): 0,
                (6, 14): 0,
                (6, 15): 0,
                (6, 16): 0,
                (6, 17): 0,
                (6, 18): 0,
                (6, 19): 0,
                (6, 20): 0,
                (7, 1): 0,
                (7, 2): 0,
                (7, 3): 0,
                (7, 4): 0,
                (7, 5): 0,
                (7, 6): 0,
                (7, 7): 0,
                (7, 8): 0,
                (7, 9): 0,
                (7, 10): 0,
                (7, 11): 0,
                (7, 12): 0,
                (7, 13): 0,
                (7, 14): 0,
                (7, 15): 0,
                (7, 16): 0,
                (7, 17): 0,
                (7, 18): 0,
                (7, 19): 0,
                (7, 20): 0,
                (8, 1): 0,
                (8, 2): 0,
                (8, 3): 0,
                (8, 4): 0,
                (8, 5): 0,
                (8, 6): 0,
                (8, 7): 0,
                (8, 8): 0,
                (8, 9): 0,
                (8, 10): 0,
                (8, 11): 0,
                (8, 12): 0,
                (8, 13): 0,
                (8, 14): 0,
                (8, 15): 0,
                (8, 16): 0,
                (8, 17): 0,
                (8, 18): 0,
                (8, 19): 0,
                (8, 20): 0,
                (9, 1): 0,
                (9, 2): 0,
                (9, 3): 0,
                (9, 4): 0,
                (9, 5): 0,
                (9, 6): 0,
                (9, 7): 0,
                (9, 8): 0,
                (9, 9): 0,
                (9, 10): 0,
                (9, 11): 0,
                (9, 12): 0,
                (9, 13): 0,
                (9, 14): 0,
                (9, 15): 0,
                (9, 16): 0,
                (9, 17): 0,
                (9, 18): 0,
                (9, 19): 0,
                (9, 20): 0,
                (10, 1): 0,
                (10, 2): 0,
                (10, 3): 0,
                (10, 4): 0,
                (10, 5): 0,
                (10, 6): 0,
                (10, 7): 0,
                (10, 8): 0,
                (10, 9): 0,
                (10, 10): 0,
                (10, 11): 0,
                (10, 12): 0,
                (10, 13): 0,
                (10, 14): 0,
                (10, 15): 0,
                (10, 16): 0,
                (10, 17): 0,
                (10, 18): 0,
                (10, 19): 0,
                (10, 20): 0,
            }
        else:
            self.taille = (5, 5)
            self.plateau = {
                (1, 1): 0,
                (1, 2): 0,
                (1, 3): 0,
                (1, 4): 0,
                (1, 5): 0,
                (2, 1): 0,
                (2, 2): 0,
                (2, 3): 0,
                (2, 4): 0,
                (2, 5): 0,
                (3, 1): 0,
                (3, 2): 0,
                (3, 3): 0,
                (3, 4): 0,
                (3, 5): 0,
                (4, 1): 0,
                (4, 2): 0,
                (4, 3): 0,
                (4, 4): 0,
                (4, 5): 0,
                (5, 1): 0,
                (5, 2): 0,
                (5, 3): 0,
                (5, 4): 0,
                (5, 5): 0,
            }

        self.screen = screen
        self.numero = numero
        self.malus = 0
        self.score = 0
        self.reseau = reseau

        self.tetra_bouge = tetramino(screen, position)
        self.tetra_fantome = tetramino(screen, position)
        self.position = position
        self.marge = marge

        self.next = tetramino(screen, position)
        self.next_position = (
            self.position[0] + size * (self.taille[0] + 2) + self.marge * 2,
            self.position[1],
        )
        self.next_taille = taille_next
        self.next_marge = marge

        self.apres_next = []

        self.zonedejeu(self.position, self.taille)
        self.zonedejeu(self.next_position, (self.next_taille, self.next_taille))
        self.draw_next()

        if not self.reseau:
            self.apres_next = [tetramino(screen, position), tetramino(screen, position)]
            self.ajoute()

    def __repr__(self):
        """Affiche la grille avec la fonction print"""
        retour = ""
        for y in range(1, self.taille[1] + 1):
            for x in range(1, self.taille[0] + 1):
                retour += str(self.plateau[x, y]) + " "
            retour += "\n"
        return retour

    def place_libre(self, liste):
        """Prends en entrée une liste de valeures et renvoie si la liste d'emplacement est libre ou non"""
        OK = True
        for x, y in liste:
            if (0 < y) and (y <= self.taille[1]) and (0 < x) and (x <= self.taille[0]):
                if self.plateau[x, y] > 0:
                    ### IL Y A UN MUR
                    return False
            else:
                ### HORS MAP
                return False
        ### C'EST LIBRE
        return True

    def replace(self, tetramino, apres, fantome=False):
        """Remplace les positions d'un tetramino par une autre place"""

        ### Change les positions de la grille
        for x, y in tetramino.pos:
            self.plateau[x, y] = 0
        for x, y in apres:
            self.plateau[x, y] = -tetramino.couleur

        ### Remplace la pos du tetramino
        avant = tetramino.pos
        tetramino.pos = apres

        ### Dessine le tetramino
        tetramino.affiche(avant, apres)
        if fantome == True:
            self.draw_tetra_fantome()

    def zonedejeu(self, pos, taille):
        """Dessone la bordure de la grille"""
        screen = self.screen
        marge = self.marge
        taille = (taille[0] * size, taille[1] * size)

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (
                pos[0] - marge,
                pos[1] - marge,
                taille[0] + (2 * marge),
                taille[1] + (2 * marge),
            ),
        )
        pygame.draw.rect(screen, (0, 0, 0), (pos[0], pos[1], taille[0], taille[1]))

    ### Mouvement de tetramino
    def tomber(self, tetramino):
        """Fais tomber le tetramino d'une case"""
        # Prends les nouvelles valeurs du tetramino
        pos_chute = []
        for x, y in tetramino.pos:
            pos_chute.append((x, y + 1))

        # Test si on peut se déplacer
        if self.place_libre(pos_chute):
            self.replace(tetramino, pos_chute)
        else:
            self.arret(self.tetra_bouge)

    def tourne(self, tetramino, sens_horaire=False):
        """Fais tourner un tetramino"""

        ### OBTENIR LA POSITION APRES ROTATION DU TETRAMINO
        pos_tourne = []
        (xmin, ymin, L, dec) = tetramino.a_tourner()

        if not sens_horaire:
            for x, y in tetramino.pos:
                pos_tourne.append(
                    (xmin + (y - ymin) + dec, ymin + ((L - 1) - (x - xmin)))
                )
        else:
            for x, y in tetramino.pos:
                pos_tourne.append(
                    (xmin + ((L - 1) - (y - ymin)) + dec, ymin + ((x - xmin)))
                )

        ### LE TETRAMINO EST TROP A DROITE
        dec = 0
        for x, y in pos_tourne:
            if x > self.taille[0]:
                if dec < x - self.taille[0]:
                    dec = x - self.taille[0]
        if dec > 0:
            nv_pos_tourne = []
            for x, y in pos_tourne:
                nv_pos_tourne.append((x - dec, y))
            pos_tourne = nv_pos_tourne

        ### ON REMPLACE LES POSITIONS
        if self.place_libre(pos_tourne):
            self.replace(tetramino, pos_tourne, fantome=True)
        else:
            print("Ouch le mur")

    def deplacer(self, tetramino, direction):
        """Déplace un tetramino horizontalement de la valeur de direcion"""

        ### On crée les nouvelles positions
        new_pos = []
        for pos in tetramino.pos:
            new_pos.append((pos[0] + direction, pos[1]))

        ### On remplace
        if self.place_libre(new_pos):
            self.replace(tetramino, new_pos, fantome=True)
        else:
            print("Ouch le mur")

    def decale(self, debut, fin=0, decalage=1, sens=-1):
        """Decale tout une ligne du plateau vers le haut ou vers le bas"""
        for ny in range(debut, fin, sens):
            # On part du bas (sens = -1) car cela permet de ne pas arriver sur la ligne qu'on vient de déplacer et donc la redécaler encore
            for nx in range(self.taille[0], 0, -1):
                # On dessine les images à l'écran et on remplace dans le plateau
                carre(
                    self.screen,
                    (nx, ny + decalage),
                    self.position,
                    color[abs(self.plateau[nx, ny])],
                )
                (self.plateau[nx, ny + decalage], self.plateau[nx, ny]) = (
                    self.plateau[nx, ny],
                    0,
                )

    def arret(self, tetramino):
        """
        - stop le tetramino
        - Vide le tetramino fantome de ses valeurs
        - test si la ligne est complete et s'il a un malus
        - ajoute un nouveau tetramino
        """
        for x, y in tetramino.pos:
            self.plateau[x, y] = tetramino.couleur
        self.tetra_fantome.pos = []

        self.test_ligne()
        self.test_malus()

        # Permet au prochain tetramino d'avoir une vitesse normale si la vitesse avait été accélérée
        pygame.time.set_timer(USEREVENT + self.numero, vitesse_tetra)

        self.ajoute()

    def test_ligne(self):
        """Test si le tetramino qui s'arrête vient de combler une ou plusieurs lignes"""

        (xmin, ymin, X, Y) = self.tetra_bouge.taille()
        nb_ligne = 0

        # On parcours toute les lignes que peut combler le tetramino
        for y in range(ymin, ymin + Y):
            ligne_casse = True

            # Parcours toute la largeur de la grille (+1 car la deuxième valeur n'est pas comprise)
            for x in range(1, self.taille[0] + 1):
                if self.plateau[x, y] == 0:
                    ligne_casse = False

            # On comble la ligne complete
            if ligne_casse == True:
                self.decale(y - 1)
                nb_ligne += 1

        if nb_ligne > 0:
            self.score += score_ligne[nb_ligne]
            pygame.event.post(
                pygame.event.Event(LIGNE, {"joueur": self.numero, "nombre": nb_ligne})
            )

    def test_perdu(self):
        """Test si le joueur a perdu"""

        # On test si la place du nouveau tetramino est prise
        if not self.place_libre(self.next.pos):
            pygame.event.post(pygame.event.Event(PERDU, {"joueur": self.numero}))

    def test_malus(self):
        """Rajoute des lignes creuses en bas de plateau"""
        if self.malus > 0:
            self.decale(
                1 + self.malus, 21, -self.malus, 1
            )  # On ne prends pas 1 pour ne pas dessiner en 0
            trou = randint(1, self.taille[0])
            couleur = randint(1, 7)

            for y in range(self.taille[1] - self.malus, self.taille[1]):
                for x in range(1, self.taille[0] + 1):
                    if x != trou:
                        carre(self.screen, (x, y + 1), self.position, color[couleur])
                        self.plateau[x, y + 1] = couleur
                    else:
                        # On met du noir sur toutes les cases qui ne sont pas de couleur
                        carre(self.screen, (x, y + 1), self.position, color[0])
            pygame.event.post(
                pygame.event.Event(
                    J2, {"touche": "malus", "trou": trou, "malus": self.malus}
                )
            )
            self.malus = 0

    def ajoute(self):
        """
        - test de défaite
        - Le tetra_next devient le tetra_bouge et il est placé en haut de la grille
        - Crée un nouveau tetra_next
        - Envoie le message en réseau
        """

        ### TEST DE DEFAITE
        self.next.centrer(self.taille)
        self.test_perdu()

        ### Le tetra_next devient le tetra_bouge et il est placé en haut de la grille
        self.tetra_bouge = self.next
        for x, y in self.tetra_bouge.pos:
            self.plateau[x, y] = -self.tetra_bouge.couleur
        self.tetra_bouge.draw(self.tetra_bouge.pos, self.tetra_bouge.marge)

        ### Crée un nouveau tetra_next et tetra_apres_next
        self.next = self.apres_next[0]
        del self.apres_next[0]

        if not self.reseau:
            self.apres_next.append(tetramino(self.screen, self.position))
        self.draw_next()
        self.draw_tetra_fantome()

        ### Partage en réseau
        pygame.event.post(pygame.event.Event(STOP, {"joueur": self.numero}))

    ### TETRA NEXT
    def next_tetra_pos(self):
        """Renvoie la position que doit prendre le tetra_next"""
        # -p1/p2 point en haut à gauche de la grille
        # -bordgrand(la largeur et hauteur de cette grille)
        # -borptitlarg/borptithaut(la largeur et la hauteur du tetra dans cette grille)

        (a, b, borptithaut, borptilarg) = self.next.taille()
        (borptilarg, borptithaut) = (borptithaut * size, borptilarg * size)

        (p1, p2) = self.next_position
        borgrand = self.next_taille * size

        newp1 = int(p1 + (1 / 2) * borgrand - (1 / 2) * borptilarg)
        newp2 = int(p2 + (1 / 2) * borgrand - (1 / 2) * borptithaut)

        return (newp1, newp2)

    def draw_next(self):
        """Redessine le tetramino suivant"""

        ### On met un fond noir
        (p1, p2) = self.next_position
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (p1, p2, self.next_taille * size, self.next_taille * size),
        )

        ### On dessine le tetramino
        self.next.draw(self.next.pos, self.next_tetra_pos())

    def change_tetra_next(self, tetra):
        """Change le tetra_next et l'affiche"""
        self.tetra_next = tetra
        self.draw_next()

    ### TETRA FANTOME
    def pos_tetra_fantome(self):
        """
        Cette fonction a pour but d'obtenir les coordonnées du tétramino fantome,
        pour cela on test si la place est libre un rang en dessous du tétramino,
        si oui on réitère l'opération deux rang en dessous et ainsi de suite
        jusqu'a ce qu'il n'y ait plus de place
        """
        copie = (
            self.tetra_bouge.pos.copy()
        )  # on réalise une copie des positions du tétramino dont on veut le fantome
        limite = []  # cette liste sert à tester si la place est libre
        for i in range(len(copie)):  # on parcour les position du tétramino
            limite.append(
                (copie[i][0], copie[i][1] + 1)
            )  # on ajoute chaque position à la liste limite
        while self.place_libre(
            limite
        ):  # on test grace à limite si la place est libre un rang en dessous du tétramino
            for j in range(len(copie)):
                """
                        on ajoute à copie(liste des positions du tétramino fantome) les position de la liste limite
                (se sont les coordonées un rang en dessous de copie)
                """
                copie[j] = (copie[j][0], copie[j][1] + 1)
            for i in range(len(copie)):
                limite.append(
                    (copie[i][0], copie[i][1] + 1)
                )  # on remplace les positions de limite par de nouvelles positions( un range en dessous des anciennes)
        return copie

    def draw_tetra_fantome(self):
        """ """

        ### Récupère la couleur du tetramino
        self.tetra_fantome.couleur = self.tetra_bouge.couleur
        avant = self.tetra_fantome.pos
        apres = self.pos_tetra_fantome()

        self.tetra_fantome.affiche(
            avant, apres, hors=self.tetra_bouge.pos, fantome=True
        )
        self.tetra_fantome.pos = apres

    ### Réseau
    def change_tetra_bouge(self, tetra):
        self.replace(self.tetra_bouge, tetra.pos, True)
        self.tetra_bouge = tetra
