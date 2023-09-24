from Grille_10 import *

screen = pygame.display.set_mode((1400,700))

def partie(screen,nb_joueur = 1):
	continuer = 1
	LIGNE_CASSE1 = USEREVENT + 4
	LIGNE_CASSE2 = USEREVENT + 5
	points1 = 0
	points2 = 0
	j1 = Grille(screen)
	j1.ajoute()
	pygame.time.set_timer(TOMBER1,600)
	pygame.event.post(pygame.event.Event(LIGNE_CASSE1))
	pygame.event.post(pygame.event.Event(LIGNE_CASSE2))

	if nb_joueur == 1:
		while continuer == 1:
			pygame.time.Clock().tick(30)	
			for event in pygame.event.get():
				if event.type == LIGNE_CASSE1:
					points1 += 100
					print("BRAVO JOUEUR 1")
				if event.type == QUIT:
					continuer = 0

				if event.type == KEYDOWN:
					if event.key == K_LEFT:
						j1.deplacer(j1.tetra_bouge,-1)

					if event.key == K_RIGHT:
						j1.deplacer(j1.tetra_bouge,1)

					if event.key == K_UP:
						j1.tourne(j1.tetra_bouge, False)

					if event.key == K_DOWN:	
						j1.tomber(j1.tetra_bouge)

					if event.key == (K_SPACE):
						print(j1)

				pygame.display.flip()

	if nb_joueur == 2:
		j2 = Grille(screen, position = (720,20), numero = 2)
		j2.ajoute()
		pygame.time.set_timer(TOMBER2,600)

		while continuer == 1:
			pygame.time.Clock().tick(30)	
			for event in pygame.event.get():
				if event.type == LIGNE_CASSE2:
					points2 += 100
					print("BRAVO JOUEUR 2")

				if event.type == QUIT:
					continuer = 0

				if event.type == TOMBER1:
					j1.tomber(j1.tetra_bouge)

				if event.type == TOMBER2:
					j2.tomber(j2.tetra_bouge)

				if (event.type == PERDU):
					print(event.joueur)
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
						j1.decale(20)

				pygame.display.flip()

	print("joueur 1 a " + str(points1) + "points")
	print("joueur 2 a " + str(points2) + "points")

partie(screen,2)

pygame.quit()

