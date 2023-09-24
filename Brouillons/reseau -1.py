import socket
import threading

class reseau(threading.Thread):
	def __init__(self, port = 12800):
		threading.Thread.__init__(self)
		print("le réseau démarre")
		self.port 		= port 
		self.hote 		= "localhost"
		self.message_envois = ""
		self.ecoute = True

		self.test()
		self.start()

	def test(self):
		self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		test_erreur = self.connexion.connect_ex((self.hote, self.port))

		print(test_erreur)

		if test_erreur != 0:
			print ("serveur")			
			self.serveur = True

			self.connexion.close()
			self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.connexion.bind((self.hote, self.port))
			self.connexion.listen(5)


		else:
			print("client")
			self.serveur = False
	
	def run(self):
		""" la fonction qui est appelée par le start et qui est fait en parralèle du programme connexion_principal """		
		if self.serveur:
			self.co_client, self.infos = self.connexion.accept()			
			self.boucle(self.co_client)
			self.co_client.close()

		else:
			self.boucle(self.connexion)
		
		self.connexion.close()
		print("Fermeture de la connexion")

	def boucle(self,co):
		while self.ecoute: #((message.decode() != "fin") and (self.message_envois != b"fin") ):
			message = co.recv(1024).decode()
			print(" --",message) #,message.decode() != "fin",(self.message_envois))

			if message == "fin":
				self.ecoute = False

		self.message("fin")

	def message(self,message):

		### retester si le programme ecoute permet de ne pas avoir d'erreur si la connexion se ferme durant le input
		if self.ecoute:
			self.message_envois = message.encode()
			if self.serveur:
				self.co_client.send(self.message_envois)	
			else :
				self.connexion.send(self.message_envois)

			if message == "fin":
				self.ecoute = False

	
		

b = reseau()

message = ""
while b.ecoute :#((message != "fin") and (b.message_envois != b"fin")):
	message = input("")
	b.message(message)
		


input("C'est OK")