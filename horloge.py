import pygame
from pygame.locals import *

pygame.font.init()


class horloge:
    def __init__(
        self,
        screen,
        position=Rect((120, 10), (190, 90)),
        couleur=(255, 0, 0),
        taille=72,
    ):
        """Crée l'horloge et l'affiche"""
        self.fenetre = screen
        self.s = 0
        self.m = 0
        self.couleur = (255, 0, 0)

        self.police = pygame.font.Font(None, taille)
        self.texte = self.police.render("   0:0   ", False, self.couleur)
        self.rectTexte = position

        self.reaffiche()

    def actualisation(self):
        """Met à jour le temps"""
        self.s += 1
        self.texte = self.police.render(
            "   " + str(self.m) + ":" + str(self.s) + "   ",
            False,
            self.couleur,
            (0, 0, 0),
        )

        if self.s == 59:
            self.m += 1
            self.s = -1

        self.reaffiche()

    def reaffiche(self):
        """Affiche le temps à l'écran"""
        self.fenetre.blit(self.texte, self.rectTexte)
