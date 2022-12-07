from ast import Global
import tkinter
import sql as sql
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
class MenuBox():
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
class EntryBox:
    def __init__(self, row, col):
        self.entry = Entry(root, width=30, borderwidth=5)
        self.entry.grid(row = row,column = col, columnspan=3)

# PRIMARY TABLE CLASS
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
        
        ##SELECTION ITEMS##
        self.tablebox = MenuBox(["Vehicles", "Customer", "Sales Representatives", "Sales", "RI Toyota"], 10, 2, 20)
        self.headerbox = MenuBox(self.headers,15,0,20)
        self.comparison_tablebox = MenuBox(["=",">","<",">=","<="], 15, 1, 2)
        self.comparison_tablebox.drop.config(font = 8)
        self.entry = EntryBox(15,2)
    def heading(self):
        self.style.configure('Treeview.Heading', background= "lightblue2")
        self.tv['columns'] = (self.headers)
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.heading('#0', text='', anchor=CENTER)
        for i in self.headers:
            self.tv.column(i, anchor=CENTER, width = (1000//len(self.headers)))
            self.tv.heading(i, text=i, anchor=CENTER)
        self.frame.grid(row = 10, column = 7, rowspan= 40)
        self.tv.grid(row = 10, column = 7, rowspan= 40, sticky='nsew')
    def scroll(self):
        scrollbar = ttk.Scrollbar(root, orient = tkinter.VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=10, column=10, rowspan=40, sticky='ns')
    def clickMenu(self):
        if self.tablebox.selection.get() == "Vehicles":
            self.headers=["VIN","Year","Make","Model","Color"]
            self.name="vehicles"
        elif self.tablebox.selection.get() == "Customer":
            self.headers=["Customer ID", "Phone", "Insurance", "License", "Name"]
            self.name="customer"
        elif self.tablebox.selection.get() == "Sales Representatives":
            self.headers=["Employee ID", "Name", "Phone"]
            self.name="sales_rep"
        elif self.tablebox.selection.get() == "Sales":
            self.headers=["Sale ID", "Sale Date"]
            self.name="sales"
        elif self.tablebox.selection.get() == "RI Toyota":
            self.headers=["Location Number", "City", "Phone"]
            self.name="ri_toyota"
        self.heading()
        self.display(sql.selectAll(self.name))
        self.headerbox.update(self.headers)
    def clickBtn(self, name):
        if name == "Select":
            entryString = "'"+self.entry.entry.get()+"'"
            self.display(sql.select("*",table.name,[self.headerbox.selection.get(),self.comparison_tablebox.selection.get(),entryString]))
        elif name == "Update":
            myLabel = Label(root, text="updated "+self.entry.get())
        elif name == "Select Table":
            self.clickMenu()
        else:
            myLabel = Label(root, text="clicked "+self.entry.get())
            myLabel.grid(row=3, column=1)
    def display(self, val):
        self.clear_all()
        ind = 0
        for contact in val:
            self.tv.insert(parent='', index=ind, iid=ind, text='', values=(contact))
            ind+=1
    def clear_all(self):
        for item in (self.tv.get_children()):
            self.tv.delete(item)

#--GLOBAL TABLE OBJECT--
table = Table(["None Selected"],[])




class MyLabel:
    def __init__(self, text, row, col):
        self.label =   myLabel = Label(root, text = text)
        self.label.grid(row = row, column = col)



class MyButton:
    def __init__(self, name, entry, row, col):
        self.name = name
        self.entry = entry
        self.btn = Button(root,width=10, text=self.name, command=lambda: table.clickBtn(self.name))
        self.btn.grid(row = row, column = col)


            









def initialize():


    
    

    entryLabel = MyLabel("Enter Here:",0, 0)

    selectbtn = MyButton("Select", table.entry, 16, 2)
    select_table = MyButton("Select Table", "", 10, 4,)

    



    root.mainloop()
