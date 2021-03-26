#!/usr/bin/python3
import tkinter as tk
from Language import Spanish,Italian
from GUICreateGame import GUICreateGame
from GUIGame import GUIGame




class GUIMain():

    def __init__(self):
        
        self.language=Spanish()
        #create GUI
        self.root=tk.Tk()
        principal = tk.Frame(self.root)
        content= tk.Frame(principal)
        #downloads images
        spain = tk.PhotoImage(file="icons\spain.png")
        italy = tk.PhotoImage(file="icons\italy.png")
        
        #create buttons 
        btnSpain=tk.Button(content, image=spain,command=lambda: self.ChangeSpanish())
        btnItaly=tk.Button(content, image=italy,command=lambda: self.ChangeItalian())
        self.btnCreateGame=tk.Button(content,text=self.language.getMain()[1],command=lambda: self.createGame())
        self.btnJoinGame=tk.Button(content,text=self.language.getMain()[2],command=lambda: self.JoinGame())

        self.root.title(self.language.getMain()[0])
        #center a window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(270, 200, x, y))
        #disable maximize button
        self.root.resizable(0,0)
        self.root.attributes("-topmost", True)
        #show interface
        principal.pack(expand=True)
        content.pack()
        btnSpain.grid(column=3,row=0)
        btnItaly.grid(column=4,row=0)
        tk.Label(content).grid(column=0,row=0,rowspan=5,padx=30)
        self.btnCreateGame.grid(column=1,row=1,columnspan=2,pady=20,sticky='ew')
        self.btnJoinGame.grid(column=1,row=2,columnspan=2,pady=20,sticky='ew')
        content.columnconfigure(0,pad=20)

        self.root.mainloop()

    def ChangeSpanish(self):
        
        self.language=Spanish()

        self.btnCreateGame['text']=self.language.getMain()[1]
        self.btnJoinGame['text']=self.language.getMain()[2]
        self.root.title(self.language.getMain()[0])

    def ChangeItalian(self):
        
        self.language=Italian()
        self.btnCreateGame['text']=self.language.getMain()[1]
        self.btnJoinGame['text']=self.language.getMain()[2]
        self.root.title(self.language.getMain()[0])

    def createGame(self):
        
        GUIGame(self.language,self.root,1,None)

    def JoinGame(self):

        GUICreateGame(self.language,self.root)


if __name__ == "__main__":
    GUIMain()