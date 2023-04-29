from tkinter import *

class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.geometry('500x400')
        master.title('Überschrift')
        self.pack()

        self.widgetsAnlegen()

    def text(self):
        print("Ausgabe auf dem Terminal!")

    def closeWindow(self):
        print("Das Fenster wird geschlossen!")
        self.quit()

    def widgetsAnlegen(self):
        #Schließen-Button
        self.schliessenButton = Button(self, text= "Schließen",
                                             bg="green",
                                             fg="red",
                                             command = self.closeWindow)
        self.schliessenButton.pack(side=LEFT)

        #Ausgabe-Button (Terminal)
        self.hiButton = Button(self, text = "Textausgabe über das Terminal",
                                     bg = "yellow",
                                     fg="blue",
                                     command =self.text)
        self.hiButton.pack(side=LEFT)