import pygame
from random import randint

size = 30
marge = 20
liste_de_tetraminos=[[(1,1),(1,2),(2,1),(2,2)],[(1,1),(2,1),(2,2),(3,2)],[(1,2),(2,1),(2,2),(3,1)],[(1,1),(2,1),(3,1),(4,1)],[(1,1),(1,2),(1,3),(2,2)],[(1,1),(1,2),(2,2),(3,2)],[(1,1),(1,2),(2,1),(3,1)]]

red 	 = ((249, 104,  84), (204, 51, 19), (240, 75, 40))
yellow	 = ((249, 209,  85), (221,172, 19), (245,193, 30))
blue	 = ((118, 191, 255), ( 57,141,216), ( 65,161,247))                 
green	 = (( 93, 220 ,137), ( 40,170, 89), ( 42,202, 98))                  
purple	 = ((153, 113, 239), (111, 69,227), (136, 86,245))                 
turquoise= ((103, 231, 212), ( 57,190,170), ( 50,216,191))
orange	 = ((251, 156,  76), (215,113, 27), (249,136, 43))
noir 	 = ((0,0,0),(0,0,0),(0,0,0))

#color = {"noir":0, "red":1,"yellow":2,"blue":3,"green":4,"purple":5,"turquoise":6,"orange":7}
color = {0:noir,1:red,2:yellow,3:blue,4:green,5:purple,6:turquoise,7:orange}


def zonedejeu(screen, pos , taille,marge):
	""" Dessone la bordure de la grille """
	pygame.draw.rect(screen, (255,255,255), (pos[0]-marge+size, pos[1]-marge+size , taille[0]+(2*marge),taille[1]+(2*marge) ))
	pygame.draw.rect(screen, (0,0,0), 		(pos[0]		 +size, pos[1]		+size, taille[0]			,taille[1]			  ))
	# a cause du décallage : il n'y a pas de case (0,0)

def carre(screen,pos,marge_grille,couleur):
	""" Dessine un carre de tetramino """
	pygame.draw.rect   (screen, couleur[0], (marge_grille[0]+pos[0]*size, marge_grille[1]+pos[1]*size, size, size))
	pygame.draw.polygon(screen, couleur[1], ( [marge_grille[0]+pos[0]*size, marge_grille[1]+pos[1]*size+size],[marge_grille[0]+pos[0]*size+size,marge_grille[1]+pos[1]*size+size],[marge_grille[0]+pos[0]*size+size,marge_grille[1]+pos[1]*size]))
	pygame.draw.rect   (screen, couleur[2], (marge_grille[0]+pos[0]*size+round(size/8), marge_grille[1]+pos[1]*size+round(size/8), size*(6/8), size*(6/8)))



class tetramino:
	def __init__(self,screen,marge_grille):
	 	#aléa des couleur et formes 
	 	self.screen = screen
	 	self.pos = [(4,4),(5,4),(5,5),(6,4),(8,4),(7,4)]  #,,(5,4),(8,4),
	 	self.couleur = -7
	 	self.couleurs = orange
	 	self.marge = marge_grille

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
		dec = 0
		L = X
		(x_carre,y_carre) = (xmin,ymin)
		if   (Y<X):
			y_carre = ymin - (X-Y)
			dec  = Y-X
		elif (Y>X):
			L  = Y 
		return (x_carre,y_carre,L,dec)
	

	def draw(self):
		for positions in self.pos:
			carre(self.screen,positions,self.marge,self.couleurs)

	def affiche(self,avant,apres):
		for val in avant:
			if not val in apres:
				carre(self.screen,val,self.marge,noir)
		for val in apres:
			if not val in avant:
				carre(self.screen,val,self.marge,self.couleurs)
		self.pos = apres			




class Grille:
	#taille variable 
	def __init__(self,screen,petit=False,position=(20,20),marge=20):	
		self.tetraminos=[]			# peut-être ungroupe de sprite			
		self.tetra_bouge= tetramino(screen,position)
		self.next 		= tetramino(screen,position)		#Prochain tétramino
		self.position =  position
		self.screen = screen
		self.marge = marge

		if petit==False:
			self.taille = (10,20)
			self.plateau = {(1,1):0 , (1,2):0 , (1,3):0 , (1,4):0 , (1,5):0 , (1,6):0 , (1,7):0 , (1,8):0 , (1,9):0 , (1,10):0 , (1,11):0 , (1,12):0 , (1,13):0 , (1,14):0 , (1,15):0 , (1,16):0 , (1,17):0 , (1,18):0 , (1,19):0 , (1,20):0 , (2,1):0 , (2,2):0 , (2,3):0 , (2,4):0 , (2,5):0 , (2,6):0 , (2,7):0 , (2,8):0 , (2,9):0 , (2,10):0 , (2,11):0 , (2,12):0 , (2,13):0 , (2,14):0 , (2,15):0 , (2,16):0 , (2,17):0 , (2,18):0 , (2,19):0 , (2,20):0 , (3,1):0 , (3,2):0 , (3,3):0 , (3,4):0 , (3,5):0 , (3,6):0 , (3,7):0 , (3,8):0 , (3,9):0 , (3,10):0 , (3,11):0 , (3,12):0 , (3,13):0 , (3,14):0 , (3,15):0 , (3,16):0 , (3,17):0 , (3,18):0 , (3,19):0 , (3,20):0 , (4,1):0 , (4,2):0 , (4,3):0 , (4,4):0 , (4,5):0 , (4,6):0 , (4,7):0 , (4,8):0 , (4,9):0 , (4,10):0 , (4,11):0 , (4,12):0 , (4,13):0 , (4,14):0 , (4,15):0 , (4,16):0 , (4,17):0 , (4,18):0 , (4,19):0 , (4,20):0 , (5,1):0 , (5,2):0 , (5,3):0 , (5,4):0 , (5,5):0 , (5,6):0 , (5,7):0 , (5,8):0 , (5,9):0 , (5,10):0 , (5,11):0 , (5,12):0 , (5,13):0 , (5,14):0 , (5,15):0 , (5,16):0 , (5,17):0 , (5,18):0 , (5,19):0 , (5,20):0 , (6,1):0 , (6,2):0 , (6,3):0 , (6,4):0 , (6,5):0 , (6,6):0 , (6,7):0 , (6,8):0 , (6,9):0 , (6,10):0 , (6,11):0 , (6,12):0 , (6,13):0 , (6,14):0 , (6,15):0 , (6,16):0 , (6,17):0 , (6,18):0 , (6,19):0 , (6,20):0 , (7,1):0 , (7,2):0 , (7,3):0 , (7,4):0 , (7,5):0 , (7,6):0 , (7,7):0 , (7,8):0 , (7,9):0 , (7,10):0 , (7,11):0 , (7,12):0 , (7,13):0 , (7,14):0 , (7,15):0 , (7,16):0 , (7,17):0 , (7,18):0 , (7,19):0 , (7,20):0 , (8,1):0 , (8,2):0 , (8,3):0 , (8,4):0 , (8,5):0 , (8,6):0 , (8,7):0 , (8,8):0 , (8,9):0 , (8,10):0 , (8,11):0 , (8,12):0 , (8,13):0 , (8,14):0 , (8,15):0 , (8,16):0 , (8,17):0 , (8,18):0 , (8,19):0 , (8,20):0 , (9,1):0 , (9,2):0 , (9,3):0 , (9,4):0 , (9,5):0 , (9,6):0 , (9,7):0 , (9,8):0 , (9,9):0 , (9,10):0 , (9,11):0 , (9,12):0 , (9,13):0 , (9,14):0 , (9,15):0 , (9,16):0 , (9,17):0 , (9,18):0 , (9,19):0 , (9,20):0 , (10,1):0 , (10,2):0 , (10,3):0 , (10,4):0 , (10,5):0 , (10,6):0 , (10,7):0 , (10,8):0 , (10,9):0 , (10,10):0 , (10,11):0 , (10,12):0 , (10,13):0 , (10,14):0 , (10,15):0 , (10,16):0 , (10,17):0 , (10,18):0 , (10,19):0 , (10,20):0}
		else:
			self.taille = (5,5)
			self.plateau = {(1,1):0 ,(1,2):0 ,(1,3):0 ,(1,4):0 ,(1,5):0 ,(2,1):0 ,(2,2):0 ,(2,3):0 ,(2,4):0 ,(2,5):0 ,(3,1):0 ,(3,2):0 ,(3,3):0 ,(3,4):0 ,(3,5):0 ,(4,1):0 ,(4,2):0 ,(4,3):0 ,(4,4):0 ,(4,5):0 ,(5,1):0 ,(5,2):0 ,(5,3):0 ,(5,4):0 ,(5,5):0}

		zonedejeu(self.screen,(self.position[0], self.position[1]), (self.taille[0]*size,self.taille[1]*size), marge )

	def __repr__(self):
		""" Affiche la grille avec la fonction print """
		retour = ""
		for y in range (1,self.taille[1]+1):
		    for x in range (1,self.taille[0]+1):
		        retour += str(self.plateau[x,y]) + " "
		    retour += "\n"
		return retour


	def place_libre(self,liste):
		""" Prends en entrée une liste de valeures et renvoie si la liste d'emplacement est libre ou non"""
		OK = True
		for (x,y) in liste:
			if ((0<y) and (y<21) and (0<x) and (x<11)):
				if (self.plateau[x,y] > 0):
					print("IL Y A UN MUR")
					return False
			else:
				print("HORS MAP")
				return False
		#print(liste)
		return True
		
	def replace(self,tetramino,new_place):
		""" Remplace les positions d'un tetramino par une autre place """
		for (x,y) in tetramino.pos:
			self.plateau[x,y] = 0
		for (x,y) in new_place:
			self.plateau[x,y] = tetramino.couleur
		tetramino.affiche(tetramino.pos,new_place)

	def tomber(self,tetramino):
		pos_chute = []

		for x,y in tetramino.pos:
		    pos_chute.append((x,y+1))

		if self.place_libre(pos_chute):
		    self.replace(tetramino,pos_chute)
		else :
			self.arret(self.tetra_bouge)
		

	def tourne(self,tetramino,sens_horaire=False):
		pos_tourne = []
		(xmin,ymin,X,Y)   = tetramino.taille()
		(xmin,ymin,L,dec) = tetramino.a_tourner(xmin,ymin,X,Y)

		if not sens_horaire :
			for (x,y) in tetramino.pos:
				pos_tourne.append(( (xmin) + (  (y-ymin) + dec) , (ymin) + ( (L-1) - x+xmin)))
					
					
		else : 
			for (x,y) in tetramino.pos:
				pos_tourne.append(( (xmin) + (  (y-ymin) + dec) , (ymin) + ( (L-1) - (x-xmin))))


		# TROP A DROITE
		dec = 0
		for (x,y) in pos_tourne:
			if x>self.taille[0]:
				if dec < x-self.taille[0]:
					dec = x-self.taille[0]
		if dec > 0:
			nv_pos_tourne = []
			for (x,y) in pos_tourne:
				nv_pos_tourne.append((x-dec,y))
			pos_tourne = nv_pos_tourne


		if self.place_libre(pos_tourne):
			self.replace(tetramino,pos_tourne)
		else:
			print("Ouch le mur")

	def deplacer(self,tetramino,direction):
		new_pos = []
		for pos in tetramino.pos:
			if( (pos[0]+direction >10) or (pos[0]+direction <1) ):
				return False
			new_pos.append( (pos[0]+direction,pos[1]) )

		if self.place_libre(new_pos):
			self.replace(tetramino,new_pos)
		else:
			print("Ouch le mur")


	def test_ligne(self):
		(xmin,ymin,X,Y) = self.tetra_bouge.taille()

		p1 = self.plateau

		for y in range(ymin , ymin+Y):
			ligne_casse = True
			for x in range(1 , self.taille[0]+1):	#Parcours toute la largeur de la grille
				if (self.plateau[x,y] == 0):
					ligne_casse = False

			if (ligne_casse == True):
				for ny in range (y-1, 0,-1):
					for nx in range(self.taille[0] , 0,-1):

						carre(self.screen,(nx,ny+1),self.position,color[self.plateau[nx,ny]])
						(self.plateau[nx,ny+1] , self.plateau[nx,ny]) = (self.plateau[nx,ny] , 0)

	def arret(self,tetramino):
		"""
		-stop le tetra_bouge en cours
		-test si la ligne est complete ##PAS FAIT /!\
		"""
		for (x,y) in tetramino.pos:
			self.plateau[x,y] = - tetramino.couleur
		self.tetraminos.append(tetramino)
		self.test_ligne()
		self.test_perdu()
		self.ajoute()

	def test_perdu(self):
		if not self.place_libre(self.next.pos):
			print("PERDU")
			#EVENT

	def ajoute(self):
		""" 	
		-tetra_bouge devient tetra_next
		-place le nouveau tetra_bouge
		-création d'un nouveau tetra_next
		"""
		self.tetra_bouge = self.next
		
		# Place le tetra_bouge en haut de la grille 
		for x,y in self.tetra_bouge.pos:
			self.plateau[x,y] = self.tetra_bouge.couleur
		self.tetra_bouge.draw()

		#Crée un nouveau tetra_next
		self.next = tetramino(self.screen, self.position)


