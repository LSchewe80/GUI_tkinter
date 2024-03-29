from tkinter import * #Tk, Frame, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.frame1 = Frame(master, bg='yellow')
        self.frame2 = Frame(master, bg='cyan')
        self.frame3 = Frame(master, bg='blue')
        self.frame4 = Frame(master, bg='red')
        
        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master=self.frame1, textvariable=self.total_label_text)

        self.label = Label(master=self.frame1, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master=self.frame2, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master=self.frame3, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master=self.frame3, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master=self.frame3, text="Reset", command=lambda: self.update("reset"))

        self.close_button = Button(master=self.frame4, text="Schliessen", command=self.close_GUI)
        
#############################################################################################
        # LAYOUT
        self.frame1.grid(row=0, column=0, padx='5', pady='5')
        self.frame2.grid(row=1, column=0, padx='5', pady='5')
        self.frame3.grid(row=2, column=0, padx='5', pady='5')
        self.frame4.grid(row=3, column=0, padx='5', pady='5')
        
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
        
        self.close_button.grid(row=0, column=0)
        
#############################################################################################
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)
    
    def close_GUI(self):
        self.master.destroy()