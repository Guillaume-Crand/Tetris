plateau = {(1,1):0 , (1,2):0 , (1,3):0 , (1,4):0 , (1,5):0 , (1,6):0 , (1,7):0 , (1,8):0 , (1,9):0 , (1,10):0 , (1,11):0 , (1,12):0 , (1,13):0 , (1,14):0 , (1,15):0 , (1,16):0 , (1,17):0 , (1,18):0 , (1,19):0 , (1,20):0 , (2,1):0 , (2,2):0 , (2,3):0 , (2,4):0 , (2,5):0 , (2,6):0 , (2,7):0 , (2,8):0 , (2,9):0 , (2,10):0 , (2,11):0 , (2,12):0 , (2,13):0 , (2,14):0 , (2,15):0 , (2,16):0 , (2,17):0 , (2,18):0 , (2,19):0 , (2,20):0 , (3,1):0 , (3,2):0 , (3,3):0 , (3,4):0 , (3,5):0 , (3,6):0 , (3,7):0 , (3,8):0 , (3,9):0 , (3,10):0 , (3,11):0 , (3,12):0 , (3,13):0 , (3,14):0 , (3,15):0 , (3,16):0 , (3,17):0 , (3,18):0 , (3,19):0 , (3,20):0 , (4,1):0 , (4,2):0 , (4,3):0 , (4,4):0 , (4,5):0 , (4,6):0 , (4,7):0 , (4,8):0 , (4,9):0 , (4,10):0 , (4,11):0 , (4,12):0 , (4,13):1 , (4,14):1 , (4,15):0 , (4,16):0 , (4,17):0 , (4,18):0 , (4,19):0 , (4,20):0 , (5,1):0 , (5,2):0 , (5,3):0 , (5,4):0 , (5,5):0 , (5,6):0 , (5,7):0 , (5,8):0 , (5,9):0 , (5,10):0 , (5,11):0 , (5,12):1 , (5,13):1 , (5,14):0 , (5,15):0 , (5,16):0 , (5,17):0 , (5,18):0 , (5,19):0 , (5,20):0 , (6,1):0 , (6,2):0 , (6,3):0 , (6,4):0 , (6,5):0 , (6,6):0 , (6,7):0 , (6,8):0 , (6,9):0 , (6,10):0 , (6,11):0 , (6,12):0 , (6,13):0 , (6,14):0 , (6,15):0 , (6,16):0 , (6,17):0 , (6,18):0 , (6,19):0 , (6,20):0 , (7,1):0 , (7,2):0 , (7,3):0 , (7,4):0 , (7,5):0 , (7,6):0 , (7,7):0 , (7,8):0 , (7,9):0 , (7,10):0 , (7,11):0 , (7,12):0 , (7,13):0 , (7,14):0 , (7,15):0 , (7,16):0 , (7,17):0 , (7,18):0 , (7,19):0 , (7,20):0 , (8,1):0 , (8,2):0 , (8,3):0 , (8,4):0 , (8,5):0 , (8,6):0 , (8,7):0 , (8,8):0 , (8,9):0 , (8,10):0 , (8,11):0 , (8,12):0 , (8,13):0 , (8,14):0 , (8,15):0 , (8,16):0 , (8,17):0 , (8,18):0 , (8,19):0 , (8,20):0 , (9,1):0 , (9,2):0 , (9,3):0 , (9,4):0 , (9,5):0 , (9,6):0 , (9,7):0 , (9,8):0 , (9,9):0 , (9,10):0 , (9,11):0 , (9,12):0 , (9,13):0 , (9,14):0 , (9,15):0 , (9,16):0 , (9,17):0 , (9,18):0 , (9,19):0 , (9,20):0 , (10,1):0 , (10,2):0 , (10,3):0 , (10,4):0 , (10,5):0 , (10,6):0 , (10,7):0 , (10,8):0 , (10,9):0 , (10,10):0 , (10,11):0 , (10,12):0 , (10,13):0 , (10,14):0 , (10,15):0 , (10,16):0 , (10,17):0 , (10,18):0 , (10,19):0 , (10,20):0}

tetra = [(3,3),(2,3),(2,4),(3,2)]

def affiche(tableau):
		retour = ""
		for y in range (1,21):
		    for x in range (1,11):
		        retour += str(plateau[x,y]) + " "
		    retour += "\n"
		print(retour)

def taille(liste):
	xmin=99
	xmax=0
	ymin=99
	ymax=0

	for (x,y) in liste:
		if x<xmin:
			xmin = x
		if x>xmax:
			xmax = x

		if y<ymin:
			ymin = y
		if y>ymax:
			ymax = y

	largeur = xmax-xmin +1
	longueur = ymax-ymin +1
	return (largeur,longueur)


#print(taille(tetra))


def tourner_h(tetra):
    retour = []
    (largeur,longueur)=taille(tetra)
    for (x,y) in tetra:
        retour.append( (2+longueur-y,x) ) #OK
    print(tetra,"\n",retour,"\n",largeur,longueur)


tourner_h(tetra)

    




		#print(tetramino.taille())
		for (x,y) in tetramino.pos:	        
			pos_tourne.append(( (ymax-y)+(xmin) , (xmin-x)+(ymax+Y-1) ))
		
		#print("pos_tourne:",pos_tourne,"\npos_tetra: ",tetramino.pos)
		if (valeurs(pos_tourne)[3] != ymax):
			# Redescends le tetramino si le faire tourner l'a fait remonter
			print("Je suis trop haut ou trop bas, je redescends")
			ecart = (ymax - valeurs(pos_tourne)[3])
			for j in range (0,len(pos_tourne)):
					pos_tourne[j]= (pos_tourne[j][0],pos_tourne[j][1] + ecart )
					print(pos_tourne[j])
		#print("pos_tourne:",pos_tourne,"\npos_tetra: ",tetramino.pos)


		for x,y in pos_tourne:
			#test si la place est libre
			if (x>0 and y>0) and (x<21 and y<21):
			    if self.plateau[x,y]>0:
			        OK = False	
			        print("problème en :",(x,y))
			else:
				print("hors map")



		if OK == True:
			# effacement des couleurs
		    for x,y in tetramino.pos:
		        self.plateau[x,y] = 0
		    # replacement des couleurs
		    for x,y in pos_tourne: 
		        self.plateau[x,y] = tetramino.couleur
		    # Mise à jour des positions du tetramino
		    tetramino.pos = pos_tourne

		else : 
			print("FATAL ERROR SYSTEM\n",pos_tourne)
		print(self)






def valeurs(liste):
	xmin=99
	xmax=0
	ymin=99
	ymax=0
	for (x,y) in liste:
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






















def a_tourner(xmin,ymin,X,Y):
	if   (Y<X):
		x_bouge = xmin  
		y_bouge = ymin - (X-Y)
		L  = X
	elif (Y>X):
		x_bouge = xmin
		y_bouge = ymin
		L  = Y
	else:
		(x_bouge,y_bouge,L) = (xmin,ymin,X)
	return (x_bouge,y_bouge,L)