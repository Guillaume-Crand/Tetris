import pygame
from random import randint

class tetramino:
	def __init__(self):
	 	#aléa des couleur et formes 
	 	self.pos = [(4,4),(3,4),(5,4),(4,5),(6,4),(7,4),(4,6)]
	 	self.couleur = -7

	 	#liste de coordonnées
	def taille(self):
		""" Fonction qui calcul la largueur et la longueur maximale du tétramino, les renvois, ainis que les coordonnés(x,y) les plus petites"""
		xmin=99
		xmax=0
		ymin=99
		ymax=0
		for (x,y) in self.pos:
			if x<xmin:
				xmin = x
			if x>xmax:
				xmax = x

			if y<ymin:
				ymin = y
			if y>ymax:
				ymax = y
		X = xmax-xmin +1   # Le +1 est la taille du premier carré
		Y = ymax-ymin +1
		return (xmin,ymin,X,Y)

	def a_tourner(self,xmin,ymin,X,Y):
		""" Calcul les valeurs (xmin,ymin,longueur) du carré minimum à faire tourner pour la rotation du tétramino"""
		if   (Y<X):
			x_carre = xmin  
			y_carre = ymin - (X-Y)
			L  = X
		elif (Y>X):
			x_carre = xmin
			y_carre = ymin
			L  = Y
		else:
			(x_carre,y_carre,L) = (xmin,ymin,X)
		return (x_carre,y_carre,L)
		

class Grille:
	#taille variable 
	def __init__(self,petit=False):	
		self.tetraminos=[]			# peut-être ungroupe de sprite			
		self.tetra_bouge= tetramino()
		self.next = tetramino()		#Prochain tétramino
		
		if petit==False:
			self.taille = (20,10)
			self.plateau = {(1,1):0 , (1,2):0 , (1,3):0 , (1,4):0 , (1,5):0 , (1,6):0 , (1,7):0 , (1,8):0 , (1,9):0 , (1,10):0 , (1,11):0 , (1,12):0 , (1,13):0 , (1,14):0 , (1,15):0 , (1,16):0 , (1,17):0 , (1,18):0 , (1,19):0 , (1,20):0 , (2,1):0 , (2,2):0 , (2,3):0 , (2,4):0 , (2,5):0 , (2,6):0 , (2,7):0 , (2,8):0 , (2,9):0 , (2,10):0 , (2,11):0 , (2,12):0 , (2,13):0 , (2,14):0 , (2,15):0 , (2,16):0 , (2,17):0 , (2,18):0 , (2,19):0 , (2,20):0 , (3,1):0 , (3,2):0 , (3,3):0 , (3,4):0 , (3,5):0 , (3,6):0 , (3,7):0 , (3,8):0 , (3,9):0 , (3,10):0 , (3,11):0 , (3,12):0 , (3,13):0 , (3,14):0 , (3,15):0 , (3,16):0 , (3,17):0 , (3,18):0 , (3,19):0 , (3,20):0 , (4,1):0 , (4,2):0 , (4,3):0 , (4,4):0 , (4,5):0 , (4,6):0 , (4,7):0 , (4,8):0 , (4,9):0 , (4,10):0 , (4,11):0 , (4,12):0 , (4,13):0 , (4,14):0 , (4,15):0 , (4,16):0 , (4,17):0 , (4,18):0 , (4,19):0 , (4,20):0 , (5,1):0 , (5,2):0 , (5,3):0 , (5,4):0 , (5,5):0 , (5,6):0 , (5,7):0 , (5,8):0 , (5,9):0 , (5,10):0 , (5,11):0 , (5,12):0 , (5,13):0 , (5,14):0 , (5,15):0 , (5,16):0 , (5,17):0 , (5,18):0 , (5,19):0 , (5,20):0 , (6,1):0 , (6,2):0 , (6,3):0 , (6,4):0 , (6,5):0 , (6,6):0 , (6,7):0 , (6,8):0 , (6,9):0 , (6,10):0 , (6,11):0 , (6,12):0 , (6,13):0 , (6,14):0 , (6,15):0 , (6,16):0 , (6,17):0 , (6,18):0 , (6,19):0 , (6,20):0 , (7,1):0 , (7,2):0 , (7,3):0 , (7,4):0 , (7,5):0 , (7,6):0 , (7,7):0 , (7,8):0 , (7,9):0 , (7,10):0 , (7,11):0 , (7,12):0 , (7,13):0 , (7,14):0 , (7,15):0 , (7,16):0 , (7,17):0 , (7,18):0 , (7,19):0 , (7,20):0 , (8,1):0 , (8,2):0 , (8,3):0 , (8,4):0 , (8,5):0 , (8,6):0 , (8,7):0 , (8,8):0 , (8,9):0 , (8,10):0 , (8,11):0 , (8,12):0 , (8,13):0 , (8,14):0 , (8,15):0 , (8,16):0 , (8,17):0 , (8,18):0 , (8,19):0 , (8,20):0 , (9,1):0 , (9,2):0 , (9,3):0 , (9,4):0 , (9,5):0 , (9,6):0 , (9,7):0 , (9,8):0 , (9,9):0 , (9,10):0 , (9,11):0 , (9,12):0 , (9,13):0 , (9,14):0 , (9,15):0 , (9,16):0 , (9,17):0 , (9,18):0 , (9,19):0 , (9,20):0 , (10,1):0 , (10,2):0 , (10,3):0 , (10,4):0 , (10,5):0 , (10,6):0 , (10,7):0 , (10,8):0 , (10,9):0 , (10,10):0 , (10,11):0 , (10,12):0 , (10,13):0 , (10,14):0 , (10,15):0 , (10,16):0 , (10,17):0 , (10,18):0 , (10,19):0 , (10,20):0}
		else:
			self.taille = (5,5)
			self.plateau = {(1,1):0 ,(1,2):0 ,(1,3):0 ,(1,4):0 ,(1,5):0 ,(2,1):0 ,(2,2):0 ,(2,3):0 ,(2,4):0 ,(2,5):0 ,(3,1):0 ,(3,2):0 ,(3,3):0 ,(3,4):0 ,(3,5):0 ,(4,1):0 ,(4,2):0 ,(4,3):0 ,(4,4):0 ,(4,5):0 ,(5,1):0 ,(5,2):0 ,(5,3):0 ,(5,4):0 ,(5,5):0}

	def __repr__(self):
		""" Affiche la grille avec la fonction print """
		retour = ""
		for y in range (1,self.taille[0]+1):
		    for x in range (1,self.taille[1]+1):
		        retour += str(self.plateau[x,y]) + " "
		    retour += "\n"
		return retour

	def place_libre(self,liste):
		""" Prends en entrée une liste de valeures et renvoie si la liste d'emplacement est libre ou non"""
		OK = True
		for (x,y) in liste:
			if (self.plateau[x,y] > 0):
				return False
		return True

	def replace(self,tetramino,new_place):
		""" Remplace les positions d'un tetramino par une autre place """
		for (x,y) in tetramino.pos:
			self.plateau[x,y] = 0
		for (x,y) in new_place:
			self.plateau[x,y] = tetramino.couleur
		tetramino.pos = new_place

	def ajoute(self):
		""" 
		-stop le tetra_bouge en cours
		-test si la ligne est complete
		-ajout du tetra_next à tetra_bouge
		-création d'un nouveau tetra_next
		"""

		self.tetraminos.append(self.tetra_bouge)

		#ligne_complet()

		self.tetra_bouge = self.next

		##Place le tetra_bouge en haut de la grille 
		for x,y in self.tetra_bouge.pos:
		    self.plateau[x,y]= self.tetra_bouge.couleur

		self.next=tetramino()
		

	# def affichage(self):
	# 	""" Met à jour la fenêtre """

	# def ligne_complet(self):                                                        
	# 	""" Test si la ligne est complete"""

	def tomber(self,tetramino):
		pos_chute = []

		for x,y in tetramino.pos:
		    pos_chute.append((x,y+1))

		if self.place_libre(pos_chute):
		    self.replace(tetramino,pos_chute)
		else :
			print("OUCH LE MUR")

	def tourne(self,tetramino,sens_horaire=False):
		pos_tourne = []
		(xmin,ymin,X,Y)= tetramino.taille()
		(xmin,ymin,L)  = tetramino.a_tourner(xmin,ymin,X,Y)

		if not sens_horaire :
			for x in range (0,L):
				for y in range (0,L):
					if (self.plateau[xmin + x ,ymin +y ] == tetramino.couleur):
						pos_tourne.append(( (xmin-1) + (y) , (ymin-1) + (L-x) ))
		else : 
			for x in range (0,L):
				for y in range (0,L):
					if (self.plateau[xmin + x ,ymin +y ] == tetramino.couleur):
						pos_tourne.append(( (xmin-1) + (L-y) , (ymin-1) + (x)   ))

		if self.place_libre(pos_tourne):
			self.replace(tetramino,pos_tourne)
		else:
			print("Ouch le mur")










#### TEST ####
a=Grille()

a.ajoute()

print(a)


a.tourne(a.tetra_bouge)



print(a)



#print(valeurs(a.tetra_bouge.pos))








