import tkinter
import sql as sql
from tkinter import *
from tkinter import ttk
from turtle import color, heading, width

DEFAULT_TABLE = ["None Selected"]
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



class MyButton:
    def __init__(self, name, entry, row, col, table):
        self.name = name
        self.entry = entry
        self.btn = Button(root,width=10, text=self.name, command=lambda: self.click())
        self.btn.grid(row = row, column = col)
        self.table = table


    def click(self):
        if self.name == "Select":
            self.display(sql.select(self.entry,""))
        elif self.name == "Update":
            myLabel = Label(root, text="updated "+self.entry.get())
        elif self.name == "Select Table":
            self.table.click()
        else:
            myLabel = Label(root, text="clicked "+self.entry.get())
            myLabel.grid(row=3, column=1)

class Table:
    def __init__(self, headers, values):
        self.headers = headers
        self.values = values
        self.frame = Frame(root)
        self.name = ""
        self.tv = ttk.Treeview(self.frame, columns= headers, show="headings", height = "30")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.heading(), self.scroll()
        self.dropbox = DropBox(["Vehicles", "Customer", "Sales Representatives", "Sales", "RI Toyota"], 10, 2, 20)
        self.headerbox = DropBox(self.headers, 15, 1, 20)


    def heading(self):
        self.style.configure('Treeview.Heading', background= "lightblue2")
        self.tv['columns'] = (self.headers)
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.heading('#0', text='', anchor=CENTER)
        for i in self.headers:
            self.tv.column(i, anchor=CENTER, width = (1000//len(self.headers)))
            self.tv.heading(i, text=i, anchor=CENTER)
        self.frame.grid(row = 10, column = 5, rowspan= 40)
        self.tv.grid(row = 10, column = 5, rowspan= 40, sticky='nsew')

    def scroll(self):
        scrollbar = ttk.Scrollbar(root, orient = tkinter.VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=10, column=10, rowspan=40, sticky='ns')

    def click(self):
        if self.dropbox.selection.get() == "Vehicles":
            self.headers=["VIN","Year","Make","Model","Color"]
            self.name="vehicles"
        elif self.dropbox.selection.get() == "Customer":
            self.headers=["Customer ID", "Phone", "Insurance", "License", "Name"]
            self.name="customer"
        elif self.dropbox.selection.get() == "Sales Representatives":
            self.headers=["Employee ID", "Name", "Phone"]
            self.name="sales_rep"
        elif self.dropbox.selection.get() == "Sales":
            self.headers=["Sale ID", "Sale Date"]
            self.name="sales"
        elif self.dropbox.selection.get() == "RI Toyota":
            self.headers=["Location Number", "City", "Phone"]
            self.name="ri_toyota"
        self.heading()
        self.display(sql.selectAll(self.name))
        self.headerbox.update(self.headers)
        
        
    def display(self, val):
        self.clear_all()
        ind = 0
        for contact in val:
            self.tv.insert(parent='', index=ind, iid=ind, text='', values=(contact))
            ind+=1
    def clear_all(self):
        for item in (self.tv.get_children()):
            self.tv.delete(item)


class DropBox():
    def __init__(self, options, row, col, w):
        self.selection = StringVar()
        self.selection.set(options[0])
        self.drop = OptionMenu(root, self.selection, *options)
        self.drop.config(width = w)
        self.drop.grid(row = row, column = col)
    def update(self, options):
        self.drop['menu'].delete(0, 'end')
        for i in options:
            self.drop['menu'].add_command(label= i, command=tkinter._setit(self.selection, i))
        self.selection.set(options[0])
        print(options)






def initialize():


    
    entry = Entry(root, width=30, borderwidth=5)
    entry.grid(row=0,column=1, columnspan=3)
    entry.insert(0, "Enter name: ")
    
    table = Table(DEFAULT_TABLE,[])
    

    entryLabel = MyLabel("Enter Here:",0, 0)

    select = MyButton("Select", entry, 1, 1, table)
    update = MyButton("Update", entry, 2, 1, table)
    delete = MyButton("Delete", entry, 1, 2, table)
    order = MyButton("Order", entry, 2, 2, table)

    select_table = MyButton("Select Table", entry, 10, 4, table)

    comparison_dropbox = DropBox(["=",">","<",">=","<="], 15, 2, 2)
    comparison_dropbox.drop.config(font = 8)
    



    root.mainloop()
