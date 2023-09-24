import pygame
from pygame.locals import *
import tests

couleur = {"rouge": (255,0,0), "vert":(0,255,0),"bleuté": (102,102,199), "bleu":(0,0,255),"gris": (86,86,86), "blanc":(255,255,255),"or": (39,174,96),"noir":(0,0,0), "text":(100,100,153)}

class Bouton:
	def __init__(self,texte,pos,fonction,couleur = (86,86,86),type_partie = None,fen = None):
		self.texte      = texte
		self.position   = pos
		self.fonction   = fonction
		self.couleur    = couleur
		self.type 		= type_partie 
		self.centre 	= ( pos[0]+ ((pos[2]-pos[0])/2) , pos[1]+((pos[3]+pos[1])/2) )
		self.fen 		= fen

	def __str__(self):
		return self.texte

	def action(self):
		if 	self.type != None:
			self.page.jeu(self.type)

		elif self.fen != None:
			self.page.fen(self.fen)

		else:
			self.fonction()

	def dessin(self):
		pygame.draw.rect(self.fenetre,(128,128,128),self.position)


class text_encadre:
	def __init__(self,zone,texte,couleur_zone = couleur["gris"],couleur_texte = couleur["noir"]):
		self.texte 			= texte
		self.couleur_texte	= couleur_texte

		self.zone 			= zone
		self.couleur_zone	= couleur_zone

	def draw(self):
		pygame.draw.rect(self.fenetre,self.zone,self.couleur_zone)



class page:
	def __init__(self,fenetre):

		# Le fond de l'écran 
		self.background = pygame.image.load("images/TetrisFond.png")
		logo 			= pygame.image.load("images/TetrisLogo.png")
		self.background.blit(logo,(0,0))

		# Les items à afficher 
		self.boutons 	= []
		self.affichage 	= []
		self.texte 		= []

		self.police 	= pygame.font.Font("Polices/ArbutusSlab.ttf",20,bold="False",italic="False")
		self.musique 	= Musique()
		self.fenetre 	= fenetre
		Bouton.fenetre  = fenetre 
		Bouton.page 	= self

		# On arrive sur le menu 
		self.fen("1")

	## Les fenêtres
	def fen(self,numero):
		""" Affiche la fenêtre *numéro* """
		self.boutons = []
		if numero == "1":
			self.boutons.append(Bouton("Jouer"				,(200,200,270,50),self.fen		,fen ="2"		)) #330, 225
			self.boutons.append(Bouton("Options"			,(200,300,270,50),self.fen 		,fen ="options"	)) #330, 325
			self.boutons.append(Bouton("Quitter"			,(200,400,270,50),self.quitter					)) #330, 425
		
		elif numero == "2":
			self.boutons.append(Bouton("Solo"				,( 90,230,200,50),self.jeu		,type_partie = 1)) #195,255
			self.boutons.append(Bouton("Multijoueur Local"	,(350,230,200,50),self.jeu		,type_partie = 2)) #450,255
			self.boutons.append(Bouton("Multijoueur Réseau"	,( 90,350,200,50),self.jeu		,type_partie = 3)) #195,375
			self.boutons.append(Bouton("Retour"				,(350,350,200,50),self.fen 		,fen = "1"		)) #450,375
		
		elif numero == "options":
			self.boutons.append(Bouton("Fullscreen"			,( 90,230,200,50),self.fullscreen 				)) #195,255
			self.boutons.append(Bouton("Credit" 			,(350,230,200,50),self.fen 		,fen = "credit"	)) #450,255
			self.boutons.append(Bouton("Scores"				,( 90,350,200,50),self.fen 		,fen = "score"	)) #195,375
			self.boutons.append(Bouton("Retour"				,(350,350,200,50),self.fen 		,fen = "1"		)) #450,375

		elif numero == "credit":
			self.affichage.append( ((50,202,550,250),couleur["or"]) )
			for val in ((98, 248, 204, 54),(348, 248, 204, 54),(98, 348, 204, 54),(348, 348, 204, 54)):
				self.affichage.append( (val,couleur["gris"]) )
			
		self.draw()

	## PAS OUF
	def fen_credits(self):
		self.buttons.append(AButton(Menu(),"",(50,202,550,250),self.couleurs["noir"],self.carrecredits,200,300)) #Création et ajout du bouton dans la liste
		self.buttons.append(AButton(Menu(),"", (98, 248, 204, 54), self.couleurs["blanc"], self.carrecredits, 200,275)) #Création et ajout du bouton dans la liste
		self.buttons.append(AButton(Menu(),"", (348, 248, 204, 54), self.couleurs["blanc"], self.carrecredits, 200,275)) #Création et ajout du bouton dans la liste
		self.buttons.append(AButton(Menu(),"", (98, 348, 204, 54), self.couleurs["blanc"], self.carrecredits, 200,275)) #Création et ajout du bouton dans la liste
		self.buttons.append(AButton(Menu(),"", (348, 348, 204, 54), self.couleurs["blanc"], self.carrecredits, 200,275)) #Création et ajout du bouton dans la liste
		self.buttons.append(AButton(Menu(),"Guillaume Crand", (100, 250, 200, 50), self.couleurs["rouge"], self.carrecredits, 200,275)) #Création et ajout du bouton dans la liste
		self.buttons.append(AButton(Menu(),"Marguerite Bauchez", (350,250,200,50),self.couleurs["rouge"], self.carrecredits, 450,275)) #Création et ajout du bouton dans la liste
		self.buttons.append(AButton(Menu(),"Valentin Lerouge", (100,350,200,50),self.couleurs["rouge"], self.carrecredits, 200,375)) #Création et ajout du bouton dans la liste
		self.buttons.append(AButton(Menu(),"Thomas Gignoux", (350,350,200,50),self.couleurs["rouge"], self.carrecredits, 450,375)) #Création et ajout du bouton dans la liste
		self.buttons.append(AButton(Menu(),"Retour", (230,402,200,50),self.couleurs["noir"], self.retour, 330,425)) #Création et ajout du bouton dans la liste

	def fen_score(self):
		a = faire
		# import score #Appel du fichier score.py
  		#       return ScoreFrame(self.background,score) #Appel de la classe génèrant la fenêtre des scores

 		 #       self.buttons.append(AButton(Menu(),"",(0,0,635,484),self.couleurs["bleu"],self.carrescores,200,300)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),"",(30,50,575,384),self.couleurs["bleuté"],self.carrescores,200,300)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),"Scores", (230, 0, 200, 50), self.couleurs["bleu"], self.carrescores, 330,25)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),"Records", (42, 60, 544, 22),self.couleurs["noir"], self.carrescores, 330,70)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),"Derniere Partie", (42,180,544,22),self.couleurs["noir"], self.carrescores, 330,190)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),"Overall", (42,300,544,22),self.couleurs["noir"], self.carrescores, 330,310)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),"Retour", (230,434,200,50),self.couleurs["bleu"], self.retour, 330,460)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),self.score.lecture_data_record(self.score.data),(42,85,544,92),self.couleurs["text"],self.carrescores,315,115)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),self.score.lecture_data_lastgame(self.score.data),(42,205,544,92),self.couleurs["text"],self.carrescores,315,235)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),self.score.lecture_data_overall(self.score.data),(42,325,544,92),self.couleurs["text"],self.carrescores,315,355)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),self.score.lecture_data_record2(self.score.data),(0,0,0,0),self.couleurs["text"],self.carrescores,315,150)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),self.score.lecture_data_lastgame2(self.score.data),(0,0,0,0),self.couleurs["text"],self.carrescores,315,270)) #Création et ajout du bouton dans la liste
		# self.buttons.append(AButton(Menu(),self.score.lecture_data_overall2(self.score.data),(0,0,0,0),self.couleurs["text"],self.carrescores,315,390)) #Création et ajout du bouton dans la liste
    ## FIN DES FENeTRES

	def jeu(self,type_partie):
		# Mise en place de la fenêtre 
		self.fenetre 	= pygame.display.set_mode((1366,768),FULLSCREEN)
		image_fond 		= pygame.image.load("images/cubefond2.jpg")
		self.fenetre.blit(image_fond,(0,0))

		# Le jeu en lui-même
		tests.partie(self.fenetre,type_partie)

		# Image d'après partie 
		img = pygame.image.load("images/TetrisFin.jpg")
		self.fenetre.blit(img,(0,0))
		pygame.display.flip()
		pygame.time.wait(3000)


		self.fenetre 	= pygame.display.set_mode((635,484))
		self.fen("1")

		# screen = pygame.display.set_mode((683,766))
		# screen.blit(img,(-65,0))

	def draw(self):
		""" Dessine les boutons à l'écran"""
		self.fenetre.blit(self.background,(0,0))

		for bouton in self.boutons: 
			# Charge la police d'écriture, le texte et calcul la position du texte
			font 		= pygame.font.Font("Polices/ArbutusSlab.ttf",16,bold="False",italic="False") 
			texte 		= font.render(bouton.texte,False, (255,255,255)) 
			pos_texte 	= texte.get_rect(center = bouton.centre) 
			
			# Dessin du Bouton et du texte
			pygame.draw.rect(self.fenetre, bouton.couleur, bouton.position)
			self.fenetre.blit(texte,bouton.position )# pos_texte) 

		for (zone,couleur) in self.affichage:
			pygame.draw.rect(self.fenetre,couleur,zone)

		# Rafraichissement 
		pygame.display.flip()

	def fullscreen(self):
		pygame.display.set_mode((635,484),FULLSCREEN)

	def quitter(self):
		image = pygame.image.load("images/TetrisQuit.png")
		self.fenetre.blit(image,(0,0))
		pygame.display.flip()
		pygame.time.wait(3000)
		pygame.event.post(pygame.event.Event(QUIT,{}))

class Musique:
	def __init__(self):
		""" Initialisation des musiques """
		pygame.mixer.init() 
		self.play = True

		self.playlist = pygame.mixer.music
		self.playlist.load("Musique/TetrisBase.wav") 
		self.playlist.play()
	
	def pause(self):
		""" met ou quitte la pause """
		if self.play:
			self.play = False
			self.playlist.pause()
		else:
			self.play = True
			self.playlist.unpause()


# Boucle de jeu
if __name__ == "__main__":		
	pygame.init()
	screen = pygame.display.set_mode((635,484))

	A = page(screen)

	continuer = True
	while continuer :
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN: 
				for button in A.boutons: 
					if Rect(button.position).collidepoint(event.pos): 
						menu = button.action()
						print(button)

			if event.type == KEYDOWN:
				if event.key == K_TAB:
					A.musique.pause()
					print(A.musique.play)

			if event.type == QUIT:
				continuer = False

