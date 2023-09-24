from Grille_10 import *
from horloge   import *

screen = pygame.display.set_mode((1400,700))

def partie(screen,nb_joueur = 1):
	continuer = 1

	j1 = Grille(screen)
	pygame.time.set_timer(TOMBER1,600)

	if nb_joueur == 1:
		while continuer == 1:
			pygame.time.Clock().tick(30)	
			for event in pygame.event.get():

				if event.type == TOMBER1:
					j1.tomber(j1.tetra_bouge)

				if event.type == QUIT:
					continuer = 0

				if event.type == KEYDOWN:
					#J1
					if event.key == K_LEFT:
						j1.deplacer(j1.tetra_bouge,-1)
					if event.key == K_RIGHT:
						j1.deplacer(j1.tetra_bouge,1)
					if event.key == K_UP:
						j1.tourne(j1.tetra_bouge, False)
					if event.key == K_DOWN:	
						pygame.time.set_timer(TOMBER1,1)
						

					if event.key == (K_SPACE):
						print(j1)

				if (event.type == PERDU):
					print("Le joueur",event.joueur,"a perdu")
					continuer = 0


				pygame.display.flip()

	if nb_joueur == 2:
		j2 = Grille(screen, position = (720,20), numero = 2)
		pygame.time.set_timer(TOMBER2,600)

		temps = USEREVENT + 5
		pygame.time.set_timer(temps,1000)
		mon_horloge = horloge(screen,Rect((470,400),(190,90)))
		

		while continuer == 1:
			pygame.time.Clock().tick(30)	
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0

				if event.type == temps:
					mon_horloge.actualisation()

				if event.type == TOMBER1:
					j1.tomber(j1.tetra_bouge)

				if event.type == TOMBER2:
					j2.tomber(j2.tetra_bouge)

				if (event.type == PERDU):
					print("Le joueur",event.joueur,"a perdu")
					print("Score:",j1.score,"/",j2.score)
					continuer = 0

				if event.type == LIGNE:
					if event.joueur == 1:
						j2.malus += event.nombre
					elif event.joueur == 2:
						j1.malus += event.nombre
					print("Joueur",event.joueur,":",event.nombre,"lignes")

				if event.type == KEYDOWN:
					#J1
					if event.key == K_LEFT:
						j1.deplacer(j1.tetra_bouge,-1)
					if event.key == K_RIGHT:
						j1.deplacer(j1.tetra_bouge,1)
					if event.key == K_UP:
						j1.tourne(j1.tetra_bouge, False)
					if event.key == K_DOWN:	
						pygame.time.set_timer(TOMBER1,1)
							
					#J2
					if event.key == 97:  #gauche
						j2.deplacer(j2.tetra_bouge,-1)
					if event.key == 100: #droite
						j2.deplacer(j2.tetra_bouge,1)
					if event.key == 119: #haut
						j2.tourne(j2.tetra_bouge, False)
					if event.key == 115: #bas
						pygame.time.set_timer(TOMBER2,1)
						

					if event.key == (K_SPACE):
						#print(j1,j2)
						#print(j1.tetra_fantome()) 
						#j1.draw_tetra_fantome()
						j1.tomber(j1.tetra_bouge)

				pygame.display.flip()

partie(screen,2)
pygame.quit()


