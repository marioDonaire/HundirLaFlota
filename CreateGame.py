import Pyro4

class CreateGame():

    def __init__(self,text):
        self.text=text

    def CheckConection(self):
        try:
            self.p = Pyro4.Proxy(self.text)
            self.p.statusGame()
            return True
            

        except:
            return False