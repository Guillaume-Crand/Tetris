#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:29:56 2019

@author: lerouge
"""


# MENU DU TETRIS CREE PAR VALENTIN LEROUGE

import sys

# Initialisation pygame
import pygame
from pygame.locals import *

import src.tests as tests

pygame.init()


# Initialisation du menu
class Menu:
    # initialisations de la fenêtre et des polices d'écritures
    def __init__(self):
        self.hauteur_ecran = 635
        self.longueur_ecran = 484
        self.fenetre = pygame.display.set_mode(
            (self.hauteur_ecran, self.longueur_ecran)
        )
        self.police = pygame.font.Font(
            "Polices/ArbutusSlab.ttf",
            20,
            #  bold="False",italic="False"
        )
        self.couleurs = {
            "rouge": (255, 0, 0),
            "vert": (0, 255, 0),
            "bleu": (0, 0, 255),
            "gris": (86, 86, 86),
            "blanc": (255, 255, 255),
        }

    # initialisation et placement de l'image de fond et du logo
    def parametres_menu(self):
        self.fond = pygame.image.load("img/TetrisFond.png")
        self.fenetre.blit(self.fond, (0, 0))
        self.image_menu = pygame.image.load("img/TetrisLogo.png")
        self.fenetre.blit(
            self.image_menu, (self.hauteur_ecran / 3.45, self.longueur_ecran / 7)
        )

        pygame.display.set_caption("Tetris - G/V/M/T")  # Nom de la fenêtre
        pygame.display.flip()  # Rafraîchissement


# Initialisation de la musique du menu
class Musique:
    # Initialisation des musiques
    def __init__(self):
        pygame.mixer.init()  # appel du module mixer
        self.playlist_musique = list()  # création de la playlist
        self.playlist_musique.append("Musique/TetrisBase.wav")

        pygame.mixer.music.load(self.playlist_musique.pop())  # Chargement musique
        pygame.mixer.music.play(-1)  # Lancement musique
        continuer = 1
        for event in pygame.event.get():
            if event.type == K_KP0:
                continuer = 0
                pygame.mixer.pause()
            else:
                pygame.mixer.unpause()


# Classe qui génère la 1ere fenêtre du menu
class MenuFrame:
    # initialisation des éléments de la fenêtre
    def __init__(self, background):
        self.background = background  # fond
        self.couleurs = {
            "rouge": (255, 0, 0),
            "vert": (0, 255, 0),
            "bleu": (0, 0, 255),
            "gris": (86, 86, 86),
            "blanc": (255, 255, 255),
        }  # Dico couleurs
        self.police = pygame.font.Font(
            "Polices/ArbutusSlab.ttf",
            20
            # ,bold="False",italic="False"
        )
        self.buttons = []  # liste vide de boutons
        self.buttons.append(
            AButton(
                Menu(),
                "Jouer",
                (200, 200, 270, 50),
                self.couleurs["gris"],
                self.jouer,
                330,
                225,
            )
        )  # création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Options",
                (200, 300, 270, 50),
                self.couleurs["gris"],
                self.options,
                330,
                325,
            )
        )  # création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Quitter",
                (200, 400, 270, 50),
                self.couleurs["gris"],
                self.quitter,
                330,
                425,
            )
        )  # création et ajout du bouton dans la liste

    # Fonction qui est active lorsque le bouton "Jouer" est cliqué
    def jouer(self):
        print("Jouer")
        return SecondFrame(
            self.background
        )  # Appel Classe de la seconde fenêtre "Fenetre de jeu"

    # Fonction qui est active lorsque le bouton "Options" est cliqué
    def options(self):
        print("Options")
        return ThirdFrame(
            self.background
        )  # Appel Classe de la 3e fenêtre "Fenêtre des options"

    # Fonction qui est active lorsque le bouton "Quitter" est cliqué
    def quitter(self):
        return Quit(self.background, Menu())


# Classe qui génère la 2nde fenêtre du menu, a savoir, la fenêtre des menus de jeu
class SecondFrame:
    # initialisation des éléments de la fenêtre
    def __init__(self, background):
        self.background = background  # fond
        self.couleurs = {
            "rouge": (255, 0, 0),
            "vert": (0, 255, 0),
            "bleu": (0, 0, 255),
            "gris": (86, 86, 86),
            "blanc": (255, 255, 255),
        }  # Dico Couleurs
        self.buttons = []  # Liste vide de boutons
        self.buttons.append(
            AButton(
                Menu(),
                "Solo",
                (90, 230, 200, 50),
                self.couleurs["gris"],
                self.solo,
                195,
                255,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Multijoueur en Réseau",
                (350, 230, 200, 50),
                self.couleurs["gris"],
                self.multireseau,
                450,
                255,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Multijoueur Local",
                (90, 350, 200, 50),
                self.couleurs["gris"],
                self.multilocal,
                195,
                375,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Retour",
                (350, 350, 200, 50),
                self.couleurs["gris"],
                self.retour,
                450,
                375,
            )
        )  # Création et ajout du bouton dans la liste

    # Fonction qui s'active lorsque le bouton "Solo" est cliqué
    def solo(self):
        screen = pygame.display.set_mode((1366, 768), FULLSCREEN)
        image_fond = pygame.image.load("img/cubefond2.jpg")
        screen.blit(image_fond, (0, 0))

        tests.partie(screen, 1)

        img = pygame.image.load("img/TetrisFin.jpg")
        screen.blit(img, (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)

        return MenuFrame(self.background)

    def multireseau(self):
        screen = pygame.display.set_mode((683, 766))
        image_fond = pygame.image.load("img/cubefond2.jpg")
        screen.blit(image_fond, (0, 0))

        tests.partie(screen, 3)

        img = pygame.image.load("img/TetrisFinMulti.png")
        screen.blit(img, (-65, 0))
        pygame.display.flip()
        pygame.time.wait(3000)

        return MenuFrame(self.background)

    def multilocal(self):
        screen = pygame.display.set_mode((1366, 768), FULLSCREEN)
        image_fond = pygame.image.load("img/cubefond2.jpg")
        screen.blit(image_fond, (0, 0))

        tests.partie(screen, 2)

        img = pygame.image.load("img/TetrisFin.jpg")
        screen.blit(img, (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)

        return MenuFrame(self.background)  # Retour à soi-même

    def retour(self):
        return MenuFrame(self.background)  # Rappel de la classe de la 1ere fenêtre


# Classe qui génère la fenêtre des options
class ThirdFrame:
    # initialisation des éléments de la fenêtre
    def __init__(self, background):
        self.background = background  # Fond
        self.couleurs = {"gris": (86, 86, 86)}  # Dico couleurs
        self.buttons = []  # Liste vide de boutons
        self.buttons.append(
            AButton(
                Menu(),
                "Fullscreen",
                (90, 230, 200, 50),
                self.couleurs["gris"],
                self.fullscreen,
                195,
                255,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Credit",
                (350, 230, 200, 50),
                self.couleurs["gris"],
                self.credit,
                450,
                255,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Scores",
                (90, 350, 200, 50),
                self.couleurs["gris"],
                self.scores,
                195,
                375,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Retour",
                (350, 350, 200, 50),
                self.couleurs["gris"],
                self.retour,
                450,
                375,
            )
        )  # Création et ajout du bouton dans la liste

    # Fonction qui est active lorsque le bouton "Fullscreen est appuyé
    def fullscreen(self):
        pygame.display.set_mode((635, 484), FULLSCREEN)
        return self  # retour à soi-même

    # Fonction qui est active lorsque le bouton "Credit" est cliqué
    def credit(self):
        return CreditFrame(
            self.background
        )  # Appel de la classe qui génère la fenêtre des crédits

    # Fonction qui est active lorsque le bouton "Scores" est cliqué
    def scores(self):
        import score  # Appel du fichier score.py

        return ScoreFrame(
            self.background, score
        )  # Appel de la classe génèrant la fenêtre des scores
        return self

    # Fonction qui est active lorsque que le bouton "Retour" est cliqué
    def retour(self):
        return MenuFrame(
            self.background
        )  # Rappel de la classe générant la 1ere fenêtre


# Classe générant la fenêtre des crédits
class CreditFrame:
    # Initialisation des éléments de la fenêtre
    def __init__(self, background):
        self.background = background  # fond
        self.couleurs = {
            "rouge": (153, 0, 0),
            "Or": (39, 174, 96),
            "bleu": (0, 0, 255),
            "gris": (86, 86, 86),
            "blanc": (255, 255, 255),
            "noir": (0, 0, 0),
        }  # Dico couleurs
        self.buttons = []  # Liste vide de boutons
        self.buttons.append(
            AButton(
                Menu(),
                "",
                (50, 202, 550, 250),
                self.couleurs["noir"],
                self.carrecredits,
                200,
                300,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "",
                (98, 248, 204, 54),
                self.couleurs["blanc"],
                self.carrecredits,
                200,
                275,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "",
                (348, 248, 204, 54),
                self.couleurs["blanc"],
                self.carrecredits,
                200,
                275,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "",
                (98, 348, 204, 54),
                self.couleurs["blanc"],
                self.carrecredits,
                200,
                275,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "",
                (348, 348, 204, 54),
                self.couleurs["blanc"],
                self.carrecredits,
                200,
                275,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Guillaume Crand",
                (100, 250, 200, 50),
                self.couleurs["rouge"],
                self.carrecredits,
                200,
                275,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Marguerite Bauchez",
                (350, 250, 200, 50),
                self.couleurs["rouge"],
                self.carrecredits,
                450,
                275,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Valentin Lerouge",
                (100, 350, 200, 50),
                self.couleurs["rouge"],
                self.carrecredits,
                200,
                375,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Thomas Gignoux",
                (350, 350, 200, 50),
                self.couleurs["rouge"],
                self.carrecredits,
                450,
                375,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Retour",
                (230, 402, 200, 50),
                self.couleurs["noir"],
                self.retour,
                330,
                425,
            )
        )  # Création et ajout du bouton dans la liste

    # Fonction de callback
    def carrecredits(self):
        return self  # Retour à lui-même

    # Fonction active lorsque le bouton "Retour" est cliqué
    def retour(self):
        return ThirdFrame(
            self.background
        )  # Rappel de la classe générant la fenêtre des options


# Classe qui s'occupe de générer la fenêtre des scores
class ScoreFrame:
    # Initialisation des éléments de la fenêtre
    def __init__(self, background, score):
        self.score = score  # variable pour fichier score
        self.background = background  # fond
        self.couleurs = {
            "rouge": (200, 0, 0),
            "bleuté": (102, 102, 199),
            "bleu": (153, 0, 255),
            "gris": (86, 86, 86),
            "blanc": (255, 255, 255),
            "noir": (0, 0, 0),
            "text": (100, 100, 153),
        }  # Dico couleurs
        self.buttons = []  # Liste vide de boutons
        self.buttons.append(
            AButton(
                Menu(),
                "",
                (0, 0, 635, 484),
                self.couleurs["bleu"],
                self.carrescores,
                200,
                300,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "",
                (30, 50, 575, 384),
                self.couleurs["bleuté"],
                self.carrescores,
                200,
                300,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Scores",
                (230, 0, 200, 50),
                self.couleurs["bleu"],
                self.carrescores,
                330,
                25,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Records",
                (42, 60, 544, 22),
                self.couleurs["noir"],
                self.carrescores,
                330,
                70,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Derniere Partie",
                (42, 180, 544, 22),
                self.couleurs["noir"],
                self.carrescores,
                330,
                190,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Overall",
                (42, 300, 544, 22),
                self.couleurs["noir"],
                self.carrescores,
                330,
                310,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                "Retour",
                (230, 434, 200, 50),
                self.couleurs["bleu"],
                self.retour,
                330,
                460,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                self.score.lecture_data_record(self.score.data),
                (42, 85, 544, 92),
                self.couleurs["text"],
                self.carrescores,
                315,
                115,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                self.score.lecture_data_lastgame(self.score.data),
                (42, 205, 544, 92),
                self.couleurs["text"],
                self.carrescores,
                315,
                235,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                self.score.lecture_data_overall(self.score.data),
                (42, 325, 544, 92),
                self.couleurs["text"],
                self.carrescores,
                315,
                355,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                self.score.lecture_data_record2(self.score.data),
                (0, 0, 0, 0),
                self.couleurs["text"],
                self.carrescores,
                315,
                150,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                self.score.lecture_data_lastgame2(self.score.data),
                (0, 0, 0, 0),
                self.couleurs["text"],
                self.carrescores,
                315,
                270,
            )
        )  # Création et ajout du bouton dans la liste
        self.buttons.append(
            AButton(
                Menu(),
                self.score.lecture_data_overall2(self.score.data),
                (0, 0, 0, 0),
                self.couleurs["text"],
                self.carrescores,
                315,
                390,
            )
        )  # Création et ajout du bouton dans la liste

    # Fonction de callback
    def carrescores(self):
        return self

    # Fonction qui s'active lorsque le bouton "Retour" esr cliqué
    def retour(self):
        return ThirdFrame(
            self.background
        )  # Rappel de la classe qui génère la fenêtre des options


class Quit:
    def __init__(self, background, menu):
        self.background = background
        self.menu = menu
        self.buttons = []  # Liste vide de boutons
        self.img = pygame.image.load("img/TetrisQuit.png")
        self.menu.fenetre.blit(self.img, (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()


# Classe qui s'occupe de générer le bouton
class AButton:
    # initialisation des éléments essentiels à la création du bouton
    def __init__(self, menu, texte, position, couleur, func, x, y):
        self.menu = menu
        self.x = x
        self.y = y
        self.func = func
        self.position = position
        self.texte = texte
        self.couleur = couleur
        self.menu.parametres_menu()


# BOUCLE PRINCIPALE

if __name__ == "__main__":
    screen = Menu()  # Génération du menu
    menu = MenuFrame("img/TetrisFond.png")
    musique = Musique()

    while True:
        # LISTE D'EVENTS USER
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:  # Lors du click
                for button in menu.buttons:  # dans la liste de boutons
                    if Rect(button.position).collidepoint(
                        event.pos
                    ):  # vérification de la coordonnée
                        menu = button.func()  # Appel de la fonction

            if (
                event.type == QUIT
            ):  # Si on quitte la fenêtre (sans passer par les boutons)
                sys.exit()  # Quitte le programme

        for button in menu.buttons:
            pygame.draw.rect(
                screen.fenetre, button.couleur, button.position
            )  # Dessine le bouton
            font = pygame.font.Font(
                "Polices/ArbutusSlab.ttf",
                16
                # , bold="False", italic="False"
            )  # Charge la police d'écriture
            txt = font.render(
                button.texte, True, (255, 255, 255)
            )  # Ecriture dans le bouton du texte prédéfini
            pos_texte = txt.get_rect(
                center=(button.x, button.y)
            )  # Selon les coordonnées prédéfinis
            screen.fenetre.blit(txt, pos_texte)  # Réactualisation de la fenêtre
        pygame.display.flip()  # Rafraichissement de la fenêtre
