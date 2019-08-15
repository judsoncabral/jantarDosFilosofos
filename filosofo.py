import _thread
import threading
import time, random

class Liberado:
  #Se o garfo tá livre ou não(Começa todos como true, pois todos estão livres)
  livre = True
  #Mudar o garfo para livre ou não livre
  def mudarLivre(self,livre):
    self.livre = livre
  #Verifica se o garfo tá livre ou não 
  def getLivre(self):
    return self.livre

#Lista de garfos (Os 5 garfos)
garfo = list()
for i in range(5):
   garfo.append(Liberado())

def filosofo(f):
  ## Pega a posição do filosofo 
   f = int(f)
   #While infinito para processo de comer ou pensar
   while True:
    #Verifica se o garfo a direita e a esquerda tá livre
    if garfo[f].getLivre() ==True and garfo[(f + 1) % 5].getLivre() == True :
      #Se ta livre os dois garfos, muda os garfos para não livre(False)
      garfo[f].mudarLivre(False)
      garfo[(f+1)%5].mudarLivre(False)
      #Começa a comer
      print ("Filósofo", f, "comendo...")
      #Tempo para liberar o garfo
      time.sleep(random.randint(1, 5))
      #Libera os dois garfos
      garfo[f].mudarLivre(True)
      garfo[(f + 1) % 5].mudarLivre(True)
      #Muda para pensando
      print ("Filósofo ", f ," pensando na comida...")
      #Espera para poder comer denovo
      time.sleep(random.randint(1, 10))

for i in range(5):
  print ("Filósofo")
  print(i)
  #Inicia um filoso com sua posição 
  _thread.start_new_thread(filosofo, tuple([i]))

#Continuar execução...
while True:
  continue