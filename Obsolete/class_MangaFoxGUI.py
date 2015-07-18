#!/usr/bin/python
# -*- coding: cp1252 -*-

from Tkinter import *
import tkMessageBox,tkFileDialog

class MangaGUI(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.title("MangaFox GUI")
        self.labelText = StringVar()
        self.labelText.set("MangaFox Recent Update Scanner!")
        self.label1 = Label(self,textvariable=self.labelText, height=1)

        self.directory = StringVar(None)
        self.Location = Entry(self,width=40, textvariable=self.directory)

        self.directory = StringVar()
        Location = Label(self,textvariable=self.directory)


        self.menubar = Menu(self)         #predefined menu bar!
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Quit", command=self.destroy)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.config(menu=self.menubar)

        self.button1 = Button(self,text="Browse", width=20, command=self.OnButtonClick)
        self.button1.pack(side='left',padx=15,pady=15)
        self.button2 = Button(self,text="OK",width=10, command=self.ProgramClose)
        self.button2.pack(side='right',padx=15,pady=15)

    def OnButtonClick(self):
        target = str(tkFileDialog.askopenfile(title='Open Manga List Location'))
        directory = re.compile("<open file u'(.*)', mode 'r' at \dx\d+>")
        Address = ''.join(re.findall(directory,target))
        self.Location.delete(0,END)
        self.Location.insert(0,Address)

    def getStr(self):
        return self.Location.get()

    def ProgramClose(self):
        self.Address = self.getStr()
        self.destroy()



def main():
    App = MangaGUI(None)
    App.mainloop()

if __name__ == '__main__': main()
