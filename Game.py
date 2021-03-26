
import Pyro4
from Server import Server
import time

class Game():
    def __init__(self,player,uri):
        self.player=player
        if player==1:
            self.server=Server()
            time.sleep(1)
            self.gameServer=Pyro4.Proxy(self.server.getUri())
            self.uri=self.server.getUri()
        else:
            self.gameServer=Pyro4.Proxy(uri)
            self.uri=uri
            

    def setPlayer(self,matrix):
        self.gameServer.setPlayer(matrix,self.player)
    
    def getPlayer(self):
        return self.gameServer.getPlayer(self.player)
    
    def checkConection(self):
        return self.gameServer.checkConection()

    def attackPlayer(self,i,j):
        return self.gameServer.attackPlayer(i,j,self.player)

    def getSemaphore(self):
        return self.gameServer.getSemaphore()
    
    def setSemaphore(self,sem):
        self.gameServer.setSemaphore(sem)

    def statusGame(self):
        return self.gameServer.statusGame()

    def closeServer(self):
        self.server.close()

    def getUri(self):
        return self.uri