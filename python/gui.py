import tkinter
import sql
from tkinter import *
from tkinter import ttk
from turtle import color, heading, width


root = Tk()
root.title('Toyota Database Manager')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (1600/2))
y_cordinate = int((screen_height/2) - (900/2))

root.geometry("{}x{}+{}+{}".format(1600, 900, x_cordinate, y_cordinate))


 
class MyLabel:
    def __init__(self, text, row, col):
        self.label =   myLabel = Label(root, text = text)
        self.label.grid(row = row, column = col)

class DropBox:
    def __init__(self, options, row, col):
        self.selection = StringVar()
        self.selection.set(options[0])
        self.drop = OptionMenu(root, self.selection, *options)
        self.drop.config(width=20)
        self.drop.grid(row = row, column = col)



class MyButton:
    def __init__(self, name, entry, row, col):
        self.name = name
        self.entry = entry
        self.btn = Button(root,width=10, text=self.name, command=lambda: self.click())
        self.btn.grid(row = row, column = col)

    def click(self):
        if self.name == "Select":
            myLabel = Label(root, text="selected "+self.entry.get())
        elif self.name == "Update":
            myLabel = Label(root, text="updated "+self.entry.get())
        else:
            myLabel = Label(root, text="clicked "+self.entry.get())
        myLabel.grid(row=3, column=1)

class Table:
    def __init__(self, headers, values):
        self.headers = headers
        self.values = values
        self.frame = Frame(root)
        self.tv = ttk.Treeview(self.frame, columns= headers, show="headings", height = "38")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.heading(), self.scroll(), self.display()
        self.frame.grid(row = 10, column = 5, rowspan= 40)
        self.tv.grid(row = 10, column = 5, rowspan= 40, sticky='nsew')

    def heading(self):
        self.style.configure('Treeview.Heading', background= "lightblue2")
        for i in range(len(self.headers)):
            self.tv.heading(self.headers[i], text=self.headers[i])
            self.tv.column(self.headers[i], anchor=CENTER, stretch=NO, width=(1200 // len(self.headers)))

    def scroll(self):
        scrollbar = ttk.Scrollbar(root, orient = tkinter.VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=10, column=10, rowspan=40, sticky='ns')

    def display(self):
        data = []
        for n in range(1, 100):
            year = (n+2000)
            data.append(({year},f'Toyota',f'Supra' ))

        for contact in data:
            self.tv.insert('', tkinter.END, values=contact)




def initialize():


    
    entry = Entry(root, width=30, borderwidth=5)
    entry.grid(row=0,column=1, columnspan=3)
    entry.insert(0, "Enter name: ")

    entryLabel = MyLabel("Enter Here:",0, 0)
    select = MyButton("Select", entry, 1, 1)
    update = MyButton("Update", entry, 2, 1)
    delete = MyButton("Delete", entry, 1, 2)
    order = MyButton("Order", entry, 2, 2)
    table = Table(["Year", "Make", "Model"], 2)

    table_label = MyLabel("Select Table", 10, 1)
    table_drop = DropBox(["Vehicles", "Customer", "Sales Representatives", "Sales", "RI Toyota"], 10, 2)

    root.mainloop()