import Pyro4,threading,time,socket


@Pyro4.behavior(instance_mode="single")
class GameServer(object):

    def __init__(self):
        self.shipPlayer1=20
        self.shipPlayer2=20
        self.player1=None
        self.player2=None
        self.conection=0
        self.semaphore=0

    @Pyro4.expose
    def setPlayer(self,matrix,player):
        if self.conection== 2:
            pass

        if player==1:
            self.player1=matrix
            self.conection=self.conection+1

        elif player==2:
            self.player2=matrix
            self.conection=self.conection+1

    @Pyro4.expose
    def getPlayer(self,player):

        if player==1:
            return self.player1

        else:
            return self.player2

    @Pyro4.expose
    def attackPlayer(self,i,j,player):
        if player==2:
            if self.player1[i][j]==1:
                self.shipPlayer1=self.shipPlayer1-1
                self.player1[i][j]=2
                return True
            self.player1[i][j]=2
            return False

        elif player==1:
            if self.player2[i][j]==1:
                self.shipPlayer2=self.shipPlayer2-1
                self.player2[i][j]=2
                return True
            self.player2[i][j]=2
            return False
    
    @Pyro4.expose
    def checkConection(self):
        if self.conection==2 :
            return True
        else:
            return False

    @Pyro4.expose
    def statusGame(self):
        '''
        0: still game
        1: player 1 win 
        2: player2 win
        '''
        if self.shipPlayer1==0:
            return 1
        elif self.shipPlayer2==0:
            return 2
        else:
            return 0 
 
    @Pyro4.expose
    def getSemaphore(self):
        return self.semaphore

    @Pyro4.expose
    def setSemaphore(self,semaphore):
        self.semaphore=semaphore
    

class Server:

    def __init__(self):

        hilo =  threading.Thread(target=self.createServer)
        hilo.start()
        time.sleep(1)

    def createServer(self):
        
        self.daemon = Pyro4.Daemon(host=Pyro4.socketutil.getIpAddress("", workaround127=True),port=0)
        
        self.uri = self.daemon.register(GameServer,"hundirLaFlota")
        self.daemon.requestLoop()

    def getUri(self):

        return self.uri

    def close(self):
        self.daemon.unregister(GameServer)
        self.daemon.close()

    
    

