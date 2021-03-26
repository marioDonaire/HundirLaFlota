import tkinter as tk
from tkinter import ttk,messagebox
from GUIGame import GUIGame
from CreateGame import CreateGame

class GUICreateGame:
    
    def __init__(self,language,frameMain):
        self.frameMain=frameMain
        self.language=language
        self.root=self.createGui()
        
        self.root.mainloop()
        

    def createGui(self):

        root = tk.Tk()
        root.title("")
        content = ttk.Frame(root, padding=(3,3,12,12))
        namelbl = ttk.Label(content, text=self.language.getCreate()[1])
        uri = ttk.Entry(content)
        ok = ttk.Button(content, text=self.language.getCreate()[0],command=lambda:self.joinGame(uri.get().strip()))
        back = ttk.Button(content, text=self.language.getCreate()[2],command=lambda: self.back())

        self.centerWindow(root)
        
        self.frameMain.iconify()

        content.grid(column=0, row=0, sticky=("N", "S", "E", "W"))
        namelbl.grid(column=0, row=1, columnspan=2, sticky=("N", "W"), padx=5)
        uri.grid(column=3, row=1, columnspan=2, sticky=("N", "E", "W"), pady=5, padx=5)
        ok.grid(column=3, row=3)
        back.grid(column=4, row=3)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=3)
        content.columnconfigure(1, weight=3)
        content.columnconfigure(2, weight=3)
        content.columnconfigure(3, weight=1)
        content.columnconfigure(4, weight=1)
        content.rowconfigure(1, weight=1)

        return root

    def centerWindow(self,root):
        root.attributes("-topmost", True)
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry('{}x{}+{}+{}'.format(300, 100, x, y))

    def back(self):
        self.frameMain.update()
        self.frameMain.deiconify()
        self.root.destroy()
    
    def joinGame(self,text):
        text="{}{}".format("PYRO:hundirLaFlota@",text)
        c=CreateGame(text)
        if c.CheckConection():
            self.root.destroy()       
            GUIGame(self.language,self.frameMain,2,text)          
        else:
            messagebox.showerror("",self.language.getCreate()[3],icon="error")

            
        
