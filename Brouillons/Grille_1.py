class tetraminaux:
	def __init__(self,forme,couleur):
		self.couleur = couleur
		self.forme = forme

	def mouvement(self)
		


			if not (self.mur[x+1][y] > 0):		#si la case du dessous est un mur
				self.mouvement = false
			else:
				tetra_mouv.append((x+1,y))		#ajoute la position de la case en dessous du tétraminau qui bouge
				self.mur[x][y]=0				#efface le tétraminaux






			if not (self.mur[x+1][y] > 0):		#si la case du dessous est un mur
				tetra_mouv.append((x+1,y))		#ajoute la position de la case en dessous du tétraminau qui bouge
				couleur=self.mur[x][y]			#capture la couleur
				self.mur[x][y]=0				#efface la tétraminau
			else:
				block=True




class fenetre:
	def __init__(self,liste):
		self.mur=liste

	def affichage2(self):
		for val in self.mur:
			print(val,"\n")

	def descente(self):
		couleur=0										#La couleur du tétraminaux en mouvement
		tetra_mouv=[]									#Tout les tétraminaux qu'on va déplacer 
		block=False										#défini si on déplace le tétraminau
		for x in range(0,len(self.mur)-1):			
			for y in range (0,len(self.mur[0])):
				if self.mur[x][y] < 0:					#si c'est une pièce qui bouge
					if not (self.mur[x+1][y] > 0):		#si la case du dessous est un mur
						tetra_mouv.append((x+1,y))		#ajoute la position de la case en dessous du tétraminau qui bouge
						couleur=self.mur[x][y]			#capture la couleur
						self.mur[x][y]=0				#efface la tétraminau
					else:
						block=True

		if block ==True 
			for (x,y) in tetra_mouv:				
				self.mur[x][y]=couleur					#replace le tétraminau






					





a=fenetre([[-1,-1,-1],[1,0,0],[0,0,1]])

a.affichage2()

a.descente()
print("00000000000000")
a.affichage2()

print("00000000000000")
a.descente()
a.affichage2()

print("00000000000000")
a.descente()
a.affichage2()









































