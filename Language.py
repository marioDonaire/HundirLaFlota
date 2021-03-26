#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
class Language(metaclass=ABCMeta):


    @abstractmethod
    def getMain(self):
        raise NotImplementedError()
    
    @abstractmethod
    def getCreate(self):
        raise NotImplementedError()

    @abstractmethod
    def getGame(self):
        raise NotImplementedError()




class Italian(Language):

    def getMain(self):
        return["Affondare la flotta","Creare partita","Unirsi a una partita"]

    def getCreate(self):
        return["Unirsi","codice di gioco","Indietro","Impossibile accetare la connesione"]

    def getGame(self):        
        return ["Tavoliere rivale","Il tuo tavoliere ","Fine turno","Posiziona le navi","giocatore in attesa","Turno del rivale","È il tuo turno","Hai vinto","Hai perso","codice della partita"]




class Spanish(Language):

    def getMain(self):
        return["Hundir la flota","Crear partida","Unirse a una partida"]

    def getCreate(self):
        return["Unirse","Codigo de partida","Volver","Error en la conexión"]

    def getGame(self):
        return["Tablero enemigo","Tu tablero","Terminar turno","Coloca los barcos","Esperando Jugador","Turno del rival","Es tu turno","Has ganado","Has perdido","codigo de la partida"]