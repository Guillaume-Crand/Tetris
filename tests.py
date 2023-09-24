from Grille    import *
from horloge   import *
from reseau    import *

def partie(screen,type_jeu = 1):
	"""Crée une partie de jeu dans la fenetre screen
	type 1: Partie 1 joueur local
	type 2: Partie 2 joueur local
	type 3: Partie 1 joueur en ligne
	"""
	continuer = 1

	if type_jeu == 1:
		### On crée le joueur 1
		j1 = Grille(screen, position = (470,90))
		pygame.time.set_timer(TOMBER1,vitesse_tetra)

		### On crée le temps 
		temps = USEREVENT + 5
		pygame.time.set_timer(temps,1000) # 1 fois toute les 1000 millisecondes
		mon_horloge = horloge(screen,Rect((890,400),(190,90)))

		while continuer == 1:
			pygame.time.Clock().tick(30)	
			for event in pygame.event.get():

				if event.type == TOMBER1:
					j1.tomber(j1.tetra_bouge)

				if event.type == QUIT:
					continuer = 0

				if event.type == temps:
					# Mise à jour de l'horloge
					mon_horloge.actualisation()

				if event.type == KEYDOWN:
					if event.key == K_LEFT:
						# Aller a droite
						j1.deplacer(j1.tetra_bouge,-1)

					if event.key == K_RIGHT:
						# Aller à gauche
						j1.deplacer(j1.tetra_bouge,1)

					if event.key == K_UP:
						# Faire tourner le tetramino
						j1.tourne(j1.tetra_bouge, False)

					if event.key == K_DOWN:	
						# Faire tomber le tetramino très vite 
						pygame.time.set_timer(TOMBER1,80)

				if event.type == PERDU:
					print("Perdu, score:", j1.score)
					continuer = 0

				# Mise à jour de la fenetre
				pygame.display.flip()

	if type_jeu == 2:

		# Création du joueur 1
		j1 = Grille(screen)
		pygame.time.set_timer(TOMBER1,vitesse_tetra)

		# Création du joueur 2
		j2 = Grille(screen, position = (750,50), numero = 2)
		pygame.time.set_timer(TOMBER2,vitesse_tetra)

		# On crée le temps 
		temps = USEREVENT + 5
		pygame.time.set_timer(temps,1000)
		mon_horloge = horloge(screen,Rect((470,400),(190,90)))	

		while continuer == 1:
			pygame.time.Clock().tick(30)	
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0

				if event.type == temps:
					# Mise à jour de l'horloge
					mon_horloge.actualisation()

				if event.type == TOMBER1:
					j1.tomber(j1.tetra_bouge)

				if event.type == TOMBER2:
					j2.tomber(j2.tetra_bouge)

				if event.type == PERDU:
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
						pygame.time.set_timer(TOMBER1,80)
					if event.key == K_SPACE:
						print(j1,j1.tetra_bouge)
							
					#J2
					if event.key == 97:  #gauche
						j2.deplacer(j2.tetra_bouge,-1)
					if event.key == 100: #droite
						j2.deplacer(j2.tetra_bouge,1)
					if event.key == 119: #haut
						j2.tourne(j2.tetra_bouge, False)
					if event.key == 115: #bas
						pygame.time.set_timer(TOMBER2,80)

				# Mise à jour de la fenetre
				pygame.display.flip()

	if type_jeu == 3:
		## Attente du 2 ème joueur
		reseau_jeu = reseau(True)
		while not reseau_jeu.ecoute:
			pygame.time.delay(100)
			pass


		### crée les joueurs	
		j1 = Grille(screen)

		### initialise la chute
		pygame.time.set_timer(TOMBER1,vitesse_tetra)

		### Gestion du temps
		TEMPS = USEREVENT + 7
		pygame.time.set_timer(TEMPS,1000)
		mon_horloge = horloge(screen,Rect((470,400),(190,90)))
		
		while continuer == 1:
			pygame.time.Clock().tick(30)	
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0

				if event.type == TEMPS:
					# Mise à jour de l'horloge
					mon_horloge.actualisation()

				if event.type == TOMBER1:
					j1.tomber(j1.tetra_bouge)

				if event.type == PERDU:
					reseau_jeu.message("touche = perdu / joueur = "+str(event.joueur)+" / score = "+str(j1.score))
					print("Vous avez perdu")
					continuer = 0

				if event.type == LIGNE:
					reseau_jeu.message("touche = ligne / nombre = "+str(event.nombre))
				
				if event.type == KEYDOWN:
					if event.key == K_LEFT:
						j1.deplacer(j1.tetra_bouge,-1)
						reseau_jeu.message("touche = gauche")

					if event.key == K_RIGHT:
						j1.deplacer(j1.tetra_bouge,1)
						reseau_jeu.message("touche = droite")

					if event.key == K_UP:
						j1.tourne(j1.tetra_bouge, False)
						reseau_jeu.message("touche = tourne")

					if event.key == K_DOWN:	
						pygame.time.set_timer(TOMBER1,80)
						reseau_jeu.message("touche = tombe_vite")
					
					if event.key == K_SPACE:
						#pygame.event.post(pygame.event.Event(J2,{"next":str(j2.next.numpos)+"/"+str(j2.next.couleur)} ))
						ok = 1

				if event.type == J2:
					if   event.touche == "ligne":
						j1.malus += int(event.nombre)

					if   event.touche == "perdu":
						print("Le joueur 2 a perdu")
						continuer = 0





				pygame.display.flip()



	if type_jeu == 4:

		def message_reseau(mes):
			if 	 mes == "tetra_bouge":
				reseau_jeu.message("touche = tetra_bouge / pos = "+str(j1.tetra_bouge.numpos)+" / couleur = "+str(j1.tetra_bouge.couleur))
			elif mes == "tetra_next":
				reseau_jeu.message("touche = tetra_next / pos = " +str(j1.next.numpos)       +" / couleur = "+str(j1.next.couleur))
			elif mes == "apres_next":
				reseau_jeu.message("touche = apres_next / pos = " +str(j1.apres_next[len(j1.apres_next)-1].numpos) +" / couleur = "+str(j1.apres_next[len(j1.apres_next)-1].couleur))

		## Attente du 2 ème joueur
		reseau_jeu = reseau(True)
		while not reseau_jeu.ecoute:
			pygame.time.delay(100)
			pass


		### crée les joueurs	
		j1 = Grille(screen)
		j2 = Grille(screen, position = (500,50), numero = 2, reseau = True)


		### mets en commun les joueur 2 en fonction du joueur 1 de l'adversaire
		message_reseau("tetra_bouge")
		message_reseau("tetra_next")
		reseau_jeu.message("touche = apres_next / pos = " +str(j1.apres_next[0].numpos) +" / couleur = " + str(j1.apres_next[0].couleur))
		reseau_jeu.message("touche = apres_next / pos = " +str(j1.apres_next[1].numpos) +" / couleur = " + str(j1.apres_next[1].couleur))

		### initialise la chute
		pygame.time.set_timer(TOMBER1,vitesse_tetra)
		pygame.time.set_timer(TOMBER2,vitesse_tetra)

		### Gestion du temps
		TEMPS = USEREVENT + 7
		pygame.time.set_timer(TEMPS,1000)
		mon_horloge = horloge(screen,Rect((470,400),(190,90)))
		
		while continuer == 1:
			pygame.time.Clock().tick(30)	
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0

				if event.type == TEMPS:
					# Mise à jour de l'horloge
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
					if   event.joueur == 1:
						j2.malus += event.nombre
					elif event.joueur == 2:
						j1.malus += event.nombre
					#print("Joueur",event.joueur,":",event.nombre,"lignes")

				if event.type == STOP:
					if event.joueur == 1:
						message_reseau("apres_next")

					
				if event.type == KEYDOWN:
					if event.key == K_LEFT:
						j1.deplacer(j1.tetra_bouge,-1)
						reseau_jeu.message("touche = gauche")

					if event.key == K_RIGHT:
						j1.deplacer(j1.tetra_bouge,1)
						reseau_jeu.message("touche = droite")

					if event.key == K_UP:
						j1.tourne(j1.tetra_bouge, False)
						reseau_jeu.message("touche = tourne")

					if event.key == K_DOWN:	
						pygame.time.set_timer(TOMBER1,80)
						reseau_jeu.message("touche = tombe_vite")
					
					if event.key == K_SPACE:
						#pygame.event.post(pygame.event.Event(J2,{"next":str(j2.next.numpos)+"/"+str(j2.next.couleur)} ))
						#print("oui",DROITE,event.type,KEYDOWN)
						#reseau_jeu.message("touche = tetra_next / pos = "+str(j2.next.numpos)+" / couleur = "+str(j2.next.couleur))
						#print("touche = tetra_next / pos = "+str(j2.next.numpos)+" / couleur ="+str(j2.next.couleur))
						print(j2.tetra_bouge,"\n",j2.next,"\n",j2.apres_next,"\n\n",j1.tetra_bouge,"\n",j1.next,"\n",j1.apres_next,"##################")


				if event.type == J2:
					if   event.touche == "gauche":
						j2.deplacer(j2.tetra_bouge,-1)
					elif event.touche == "droite":
						j2.deplacer(j2.tetra_bouge,1)
					elif event.touche == "tourne":
						j2.tourne(j2.tetra_bouge, False)
					elif event.touche == "tombe_vite":
						pygame.time.set_timer(TOMBER2,80)

				
					# if event.touche == "malus":
					# 	#print(event.trou,event.malus)
					# 	ok = 1


					elif event.touche == "tetra_bouge":
					 	j2.change_tetra_bouge(tetramino(screen,j2.position,event.pos,event.couleur))

					elif event.touche == "tetra_next":
						print(event.pos,event.couleur)
						#j2.change_tetra_next(tetramino(screen,j2.position,event.pos,event.couleur))
		
					elif event.touche == "apres_next":
						j2.apres_next.append(tetramino(screen,j2.position,event.pos,event.couleur))






				pygame.display.flip()


pygame.quit()


