""" Crée un dictionnaire de valeur correspondant à une grille de 11*21"""

a = "" 
for i in range (1,11):
	for j in range (1,21):
		a += "(" + str(i) + "," + str(j) + "):0 ,"

print(a)
