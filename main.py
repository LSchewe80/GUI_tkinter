from tkinter_class import *

#Main-Programm
if __name__ == '__main__':
    root = Tk()

    #Objekt erzeugen
    app = Window(master=root)

    #mainloop
    app.mainloop()
    root.destroy()
