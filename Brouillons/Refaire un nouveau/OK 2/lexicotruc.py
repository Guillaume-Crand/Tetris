import pygame
from pygame.locals import *
from random import shuffle

pygame.init()

# VARIABLES
continuer = True

Police = {
	"cursive"	: pygame.font.Font("Polices/ArbutusSlab.ttf",20,bold="False",italic="False"),
	"majuscule"	: pygame.font.Font("Polices/ArbutusSlab.ttf",20,bold="False",italic="False")
}

keyboard = {"113" : "a",
	## lettres
	# ligne 1
	"119" : "z",
	"101" : "e",
	"114" : "r",
	"116" : "t",
	"121" : "y",
	"117" : "u",
	"105" : "i",
	"111" : "o",
	"112" : "p",

	# ligne 2
	"97"  : "q",
	"115" : "s",
	"100" : "d",
	"102" : "f",
	"103" : "g",
	"104" : "h",
	"106" : "j",
	"107" : "k",
	"108" : "l",
	"59"  : "m",

	# ligne 3
	"122" : "w",
	"120" : "x",
	"99"  : "c",
	"118" : "v",
	"98"  : "b",
	"110" : "n",

	## Chiffre du clavier numérique
	"256" : "0",
	"257" : "1",
	"258" : "2",
	"259" : "3",
	"260" : "4",
	"261" : "5",
	"262" : "6",
	"263" : "7",
	"264" : "8",
	"265" : "9"
}

chiffres = [1,2,3,4,5,6,7,8,9,0]
chiffre  = ["zéro","un","deux","trois","quatre","cinq","six","sept","huit","neuf"]

### CLASSES
class FENETRE:
	def __init__(self):
		self.screen = pygame.display.set_mode((640,640))
		self.plein_ecran = False

	def fullscreen(self):
		"""	Fonction permettant de passer 
		-en plein écran si on ne l'est pas 
		-revenir en fenetre si on est en plein écran	"""
		if not self.plein_ecran:
			self.plein_ecran = True
			self.screen = pygame.display.set_mode((1600,900),FULLSCREEN)
		else :		
			self.plein_ecran = False
			self.screen = pygame.display.set_mode((640,640))

	def fen_1(self):
		jouer = BOUTON(a,[50,50,200,300],"jouer")
		jouer.draw()

	def jeu(self,liste):
		print("DEBUT")

		reponse = []
		mots = liste.copy()
		shuffle(mots)
		print(mots)

		while len(reponse) < 500: #len(liste):
			pygame.time.Clock().tick(30)
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if str(event.key) in keyboard.keys():
						val_entree = keyboard[str(event.key)]
						print(val_entree)
						if val_entree == str(mots[len(reponse)]):
							print("Bonne réponse")
						else:
							print("Mauvaise réponse")
					else :
						print("Je ne connais pas cette touche")
					reponse.append("0")
					#print(reponse)

				if event.type == QUIT:
					return False

				
				pygame.display.flip()

		print("FIN")
		return True

class BOUTON:
	def __init__(self,fonction,position,texte,couleur = (0,255,0)):
		# self.screen est défini dans la boucle
		self.fonction 	= fonction
		self.texte 		= texte

		self.position 	= position
		self.centre 	= ( int((position[0]+position[2])/2) , int((position[1]+position[3])/2) )
		self.couleur 	= couleur

	def draw(self):
		pygame.draw.rect(self.screen,self.couleur,self.position)


### FONCTIONS
def a():
	print("a")

### BOUCLE

# création de la fenêtre
fenetre = FENETRE()
BOUTON.screen  = fenetre.screen



while continuer == True:
	pygame.time.Clock().tick(30)
	for event in pygame.event.get():

		if event.type == MOUSEBUTTONDOWN:
			#fenetre.fullscreen()
			continuer = fenetre.jeu(chiffres)


		if event.type == KEYDOWN:
			ok=0


		if event.type == QUIT:
			continuer = False
		pygame.display.flip()

pygame.quit()








"""
-ajouter le dessin du texte au bouton 


"""
