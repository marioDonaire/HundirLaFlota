import tkinter as tk
from tkinter import messagebox
import functools,threading,time
from Game import Game
from Language import Spanish,Italian




class GUIGame():

    def __init__(self,language,frameMain,player,uri):
        #initialize server
        self.game=Game(player,uri)
        self.player=player
        self.change=0 #0 horizontal 1 vertical
        self.ships=[1,1,1,1,2,2,2,3,3]#if its 0 you put all ships
        self.actualShip=4 #start with 4 size ship
        self.language=language
        frameMain.iconify()
        #initialize GUI
        ret=self.createGui(frameMain)
        self.root=ret[0]
        self.buttons1=ret[1]
        self.buttons2=ret[2]
        self.lblinfo=ret[3]

        self.root.mainloop()

    def createGui(self,frameMain):
        root=tk.Tk()
        frameEnemy = tk.Frame(root)
        frameYou = tk.Frame(root)

        lblEnemy = tk.Label(root,text=self.language.getGame()[0])
        lblYou   = tk.Label(root,text=self.language.getGame()[1])
        lblinfo=tk.Label(root,text=self.language.getGame()[3])
        uri=str(self.game.getUri()).split("@")
        lbluri=tk.Label(root,text="{}: {}".format(self.language.getGame()[9],uri[1]))
        
        buttons1=[ [ None for y in range( 10 ) ] 
             for x in range( 10 ) ]
        buttons2=[ [ None for y in range( 10 ) ] 
             for x in range( 10 ) ]

        root.protocol("WM_DELETE_WINDOW", lambda arg1=frameMain: self.closeWindow(arg1)) # change bottom close/exit (X) in windows
        root.update_idletasks()

        width = root.winfo_width()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        root.geometry('+{}+{}'.format( x, 0))
        root.resizable(0,0)
        root.attributes("-topmost", True)
        root.bind('<Button-3>',functools.partial(self.changeBoat))
        
        for i in range (11):
            for j in range (11):
                if(i==0 or j==0):
                    if(i==0 and j==0):
                        pass
                    elif(j==0):
                        tk.Label(frameEnemy,text=chr(64+i)).grid(column=j,row=i)
                    elif(i==0):
                        tk.Label(frameEnemy,text=j).grid(column=j,row=i)
                else:
                    buttons1[i-1][j-1]=tk.Button(frameEnemy,width=3,bg="blue",height=1,state=tk.DISABLED)
                    buttons1[i-1][j-1].bind('<Button-1>',functools.partial(self.attackEnemy, i=i-1,j=j-1))
                    buttons1[i-1][j-1].grid(column=j,row=i,sticky='nswe')

        for i in range (11):
            for j in range (11):
                if(i==0 or j==0):
                    if(i==0 and j==0):
                        pass
                    elif(j==0):
                        tk.Label(frameYou,text=chr(64+i)).grid(column=j,row=i)
                    elif(i==0):
                        tk.Label(frameYou,text=j).grid(column=j,row=i)
                else:
                    buttons2[i-1][j-1]=tk.Button(frameYou,width=3,bg="blue",height=1)
                    buttons2[i-1][j-1].bind('<Enter>',functools.partial(self.enterBotton, i=i-1,j=j-1))
                    buttons2[i-1][j-1].bind('<Button-1>',functools.partial(self.putShip, i=i-1,j=j-1))
                    buttons2[i-1][j-1].bind('<Leave>',functools.partial(self.leaveButton, i=i-1,j=j-1))
                    buttons2[i-1][j-1].grid(column=j,row=i, sticky='nswe')

        lblEnemy.grid(column=0,row=0,padx=50,pady=10)
        frameEnemy.grid(column=0,row=1,padx=50)
        lblYou.grid(column=0,row=2,padx=50,pady=10)
        frameYou.grid(column=0,row=3,padx=50,pady=10)
        lblinfo.grid(column=0,row=4,padx=50,pady=10)
        lbluri.grid(column=0,row=5)
        return [root,buttons1,buttons2,lblinfo]

    def startGame(self):
        
        try:
            #send my matrix to the server
            matrixShip=[ [ 0 for y in range( 10 ) ] 
                for x in range( 10 ) ]
        
            for i in range(10):
                for j in range(10):
                    if self.buttons2[i][j]['background']=="green":
                        matrixShip[i][j]=1
            self.game.setPlayer(matrixShip)

        #check who start the game

            while not self.game.checkConection():
                self.lblinfo['text']=self.language.getGame()[4]
                self.root.update()
                time.sleep(1)
            if self.player==1:
                self.lblinfo['text']=self.language.getGame()[6]
                self.root.update()
                self.playGame()
            else:
                self.lblinfo['text']=self.language.getGame()[5]
                self.root.update()
                time.sleep(3)
                self.playGame()
       
            for i in range(10):
                for j in range(10):
                    self.buttons2[i][j]['state']=tk.DISABLED
                    self.buttons1[i][j]['state']=tk.NORMAL
        except:
            messagebox.showerror("",self.language.getCreate()[3],icon="error")
            exit(1)     

    def changeBoat(self,event):
        if self.change==0 :
            self.change=1
        else:
            self.change=0
        for i in range(10):
            for j in range(10):
                if(self.buttons2[i][j]['state']==tk.NORMAL and self.buttons2[i][j]['background']=="green"):
                    self.buttons2[i][j]['background']="blue"

        self.root.update()
               
    def putShip(self,event,i,j):
        num=self.actualShip
        enable=True
        if (self.change==0 and self.buttons2[i][j]['background']=="green"):
            j=j+1
            for k in range(j-num,j):
                if self.buttons2[i][k]['state']==tk.DISABLED:
                    enable=False
                self.buttons2[i][k]['state']=tk.DISABLED

            if enable:
                if len(self.ships)==0:
                    self.actualShip=0
                    self.startGame()
                else:
                    self.actualShip=self.ships.pop()  

        elif (self.change==1 and self.buttons2[i][j]['background']=="green"):
            for k in range(i,i+num):
                if self.buttons2[k][j]['state']==tk.DISABLED:
                    enable=False
                self.buttons2[k][j]['state']=tk.DISABLED
            self.actualShip=self.ships.pop()
            
            if enable:
                if len(self.ships)==0:
                    self.actualShip=0
                    self.startGame()
                else:
                    self.actualShip=self.ships.pop()
            
    def enterBotton(self,event,i,j):

        if self.actualShip==0:
            pass
        else:
            num=self.actualShip
            if self.checkEnterLeave(i,j):
                if self.change==0:
                    j=j+1
                    for k in range(j-num,j):  
                        self.buttons2[i][k]['background']="green"
                else:               
                    for k in range(i,i+num):
                        self.buttons2[k][j]['background']="green"
 
    def checkEnterLeave(self,i,j):

        num=self.actualShip

        if num==0:
            return False

        if self.change==0:
            if j-num+1>=0:
                j=j+1
                for k in range (j-num,j):
                    if(self.buttons2[i][k]['state']==tk.DISABLED):
                        return False
                return True
        else:
            if i+num-1>=0 :
                for k in range (i,i+num):
                    if(self.buttons2[k][j]['state']==tk.DISABLED):
                        return False
                return True

    def leaveButton(self,event,i,j):

        if self.actualShip==0:
            pass

        else:
            num=self.actualShip
            if self.checkEnterLeave(i,j):
                if self.change==0:
                    for k in range(j-num+1,j+1):
                        self.buttons2[i][k]['background']="blue"
                else:
                    for k in range(i,i+num):
                        self.buttons2[k][j]['background']="blue"
       
    def attackEnemy(self,event,i,j):
        if self.buttons1[i][j]['state']==tk.NORMAL:
            self.buttons1[i][j]['state']=tk.DISABLED
            if self.game.attackPlayer(i,j):
                self.buttons1[i][j].config(bg="red")
            else:
                self.buttons1[i][j].config(bg="yellow")
    
            self.game.setSemaphore(self.game.getSemaphore()-1)
            time.sleep(1)
            self.playGame()

    def playGame(self):
        
            while self.game.statusGame()==0:
                time.sleep(1)
                if self.game.getSemaphore()==1:
                    #bloque los botones para atacar
                    for i in range(10):
                        for j in range(10):
                            self.buttons1[i][j]['state']=tk.DISABLED
                    self.lblinfo['text']=self.language.getGame()[5]
                    self.root.update()
                    time.sleep(1)
                
                elif self.game.getSemaphore()==0:
                    self.game.setSemaphore(self.game.getSemaphore()+1)

                    self.updateMyShips()
                 
                    self.lblinfo['text']=self.language.getGame()[6]
                    self.root.update()

                    for i in range(10):#unlock buttons in blue
                        for j in range(10):
                            if self.buttons1[i][j]['background']=="blue":
                                self.buttons1[i][j]['state']=tk.NORMAL
                    break

            #says to the player who win 
            if self.game.statusGame()==1 and self.player==1:
                messagebox.showinfo("",self.language.getGame()[8])
                self.game.closeServer()
            elif self.game.statusGame()==2 and self.player==1:
                messagebox.showinfo("",self.language.getGame()[7])
                self.game.closeServer()
            elif self.game.statusGame()==2 and self.player==2:
                messagebox.showinfo("",self.language.getGame()[8])
            elif self.game.statusGame()==1 and self.player==2:
                messagebox.showinfo("",self.language.getGame()[7])


    def updateMyShips(self):

        t=self.game.getPlayer()
        for i in range(10):
            for j in range(10):
                if t[i][j]==2:
                    if self.buttons2[i][j]['background']=="green":
                        self.buttons2[i][j]['background']="red"
                    elif self.buttons2[i][j]['background']=="blue":
                        self.buttons2[i][j]['background']="yellow"
       
    def closeWindow(self,frameMain):
        try:
            if self.player==1:
                self.game.closeServer()
            frameMain.deiconify()
            frameMain.update()
            self.root.destroy()
        except:
            exit(1)
