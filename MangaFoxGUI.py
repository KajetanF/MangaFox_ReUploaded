from Tkinter import *
import tkMessageBox,tkFileDialog
import os


class MangaGUI(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.MangaList = []
        self.initialize()


    def initialize(self):
        self.grid()
        Grid.columnconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 1, weight=1)
        self.title("MangaFox GUI")

        self.directory = StringVar(None)
        self.Location = Entry(self,width=40, textvariable=self.directory)
        self.Location.grid(column=0,row=1,columnspan=1,sticky='EW')

        self.labelVariable2 = StringVar()
        label2 = Label(self,textvariable=self.labelVariable2)
        label2.grid(column=1,row=2,columnspan = 1,sticky='W')
        self.labelVariable2.set("Scan Pages!")

        self.labelVariable3 = StringVar()
        label3 = Label(self,textvariable=self.labelVariable3)
        label3.grid(column=0,row=5,columnspan = 1)
        self.labelVariable3.set("Use delete key to delete entry! Use Enter to enter Manga to list!")

        self.pagenumber = StringVar(None)
        self.pages = Entry(self,width=10, textvariable=self.pagenumber)
        self.pages.grid(column=0,row=2,columnspan=1,sticky='EW')

        self.menubar = Menu(self)         #predefined menu bar!
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Quit", command=self.destroy)
        self.filemenu.add_command(label="Browse", command=self.OnButtonClick)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.config(menu=self.menubar)

        button1 = Button(self,text="Browse", width=10, command=self.OnButtonClick)
        button1.grid(column=1,row=1,sticky='W')
        button2 = Button(self,text="OK",width=10, command=self.ProgramClose)
        button2.grid(column=1,row=3,sticky='W')
        button3 = Button(self,text="EXIT",width=10, command=self.Exit)
        button3.grid(column=1,row=4,sticky = 'NW')

        self.ListDisplay = Listbox(self,selectmode=EXTENDED)
        self.ListDisplay.grid(column=0,row=4,sticky='EW')
        self.ListDisplay.bind("<Delete>",self.DeleteSelect)

        self.MangaName = StringVar(None)
        self.MangaName.set("Enter manga names here to add.")
        self.MangL = Entry(self,width=20, textvariable=self.MangaName)
        self.MangL.grid(column=0,row=3,columnspan=1,sticky='EW')
        self.MangL.bind("<Return>",self.AppendList)

    def DeleteSelect(self,event):
        selected = self.ListDisplay.curselection()
        start = 0
        for i in selected:
            index = int(i) - start
            self.ListDisplay.delete(index,index)
            start = start + 1
        self.MangaList = set(self.ListDisplay.get(0,END))

    def AppendList(self,event):
        self.ListDisplay.delete(0,END)
        self.MangaList= set(self.MangaList)
        self.MangaList.update((self.MangaName.get(),))
        self.MangaList = sorted(self.MangaList)
                            
        self.ListDisplay.delete(0,END)
        for item in self.MangaList:
            self.ListDisplay.insert(END,item)
        self.MangaName.set("")
        
        
    def Exit(self):
        os._exit(-1)

    def extrastuff():
                              label(self,image="")
    def OnButtonClick(self):
        target = str(tkFileDialog.askopenfile(title='Open Manga List Location'))
        target = target.strip("^<open file u'")
        Local = target[:-26]
        self.Location.delete(0,END)
        self.Location.insert(0,Local)
                            
        self.ListDisplay.delete(0,END)
        with open(Local,"r") as data:
            ListManga = filter(None,data.read().split("\n"))
        self.MangaList = set(self.MangaList)
        for item in ListManga:
            self.MangaList.update((item,))
        self.MangaList = sorted(self.MangaList)
        for manga in self.MangaList:
            self.ListDisplay.insert(END,manga)
                
    def ProgramClose(self):
        self.Page = self.pages.get()
        with open("C:\MangaFox\myMangaList.txt","w") as Manga:
            for item in self.MangaList:
                Manga.write(item + "\n")
        self.destroy()
