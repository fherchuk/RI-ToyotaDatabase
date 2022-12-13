
from cgitb import text
import tkinter
import sql 
from tkinter import *
from tkinter import ttk


BG_COLOR = '#b0c4de'

root = Tk()
root.title('Toyota Database Manager')
root.configure(bg=BG_COLOR)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (1200/2))
y_cordinate = int((screen_height/2) - (800/2))

root.geometry("{}x{}+{}+{}".format(1200, 800, x_cordinate, y_cordinate))

class MyButton:
    def __init__(self, name, entry, row, col):
        self.name = name
        self.entry = entry
        self.btn = Button(root,width=12,height= 1, text=self.name, command=lambda: table.clickBtn(self.name))
        self.btn.grid(row = row, column = col, padx=5)


class MyLabel:
    def __init__(self, text, row, col):
        self.label = Label(root, text = text)
        self.label.grid(row = row, column = col, columnspan = 2, padx=2)
        self.label.configure(bg=BG_COLOR, font=('bold',12))
    def update(self, text):
        self.label.configure(text = text)

class MenuBox():
    def __init__(self, options, row, col, w):
        self.selection = StringVar()
        self.selection.set(options[0])
        self.drop = OptionMenu(root, self.selection, *options)
        self.drop.config(width = w)
        self.drop.grid(row = row, column = col, padx=10)
        self.drop.configure(border=3)

    def update(self, options):
        self.drop['menu'].delete(0, 'end')
        for i in options:
            self.drop['menu'].add_command(label= i, command=tkinter._setit(self.selection, i))
        self.selection.set(options[0])
        print(options)

class EntryBox:
    def __init__(self, row, col):
        self.entry = Entry(root, width=30, borderwidth=5)
        self.entry.grid(row = row,column = col, columnspan=3, padx= 10)

class EntryBundle:
    def __init__(self):
        self.entry1 = EntryBox(20,1)
        self.entry2 = EntryBox(21,1)
        self.entry3 = EntryBox(22,1)
        self.entry4 = EntryBox(23,1)
        self.entry5 = EntryBox(24,1)

        self.label1 = MyLabel("",20,0)
        self.label2 = MyLabel("",21,0)
        self.label3 = MyLabel("",22,0)
        self.label4 = MyLabel("",23,0)
        self.label5 = MyLabel("",24,0)

    def update(self, headers):
        while len(headers) < 5:
            headers.append("")
        self.label1.update(headers[0]) 
        self.label2.update(headers[1]) 
        self.label3.update(headers[2]) 
        self.label4.update(headers[3]) 
        self.label5.update(headers[4]) 

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
        self.headersize = 0

        ##SELECTION ITEMS##
        self.tablebox = MenuBox(["Vehicles", "Customer", "Sales Representatives", "Sales", "RI Toyota"], 8, 2, 15)
        self.headerbox = MenuBox(self.headers,15,0,15)
        self.comparison_tablebox = MenuBox(["=","!=",">","<",">=","<="], 15, 1, 2)
        self.comparison_tablebox.drop.config(font = 8)
        self.entry = EntryBox(15,2)
        self.insertentries = EntryBundle()

    def heading(self):
        self.style.configure('Treeview.Heading', background= "lightblue2")
        self.tv['columns'] = (self.headers)
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.heading('#0', text='', anchor=CENTER)
        for i in self.headers:
            self.tv.column(i, anchor=CENTER, width = (650//len(self.headers)))
            self.tv.heading(i, text=i, anchor=CENTER)
        self.frame.grid(row = 10, column = 8, rowspan= 20)
        self.tv.grid(row = 10, column = 8, rowspan= 20, sticky='nsew')
   
    def scroll(self):
        scrollbar = ttk.Scrollbar(root, orient = tkinter.VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=10, column=10, rowspan=120, sticky='ns')

    def clickMenu(self):
        if self.tablebox.selection.get() == "Vehicles":
            self.headers=["VIN","Year","Make","Model","Color"]
            self.name="vehicles"
            self.headersize = 5
        elif self.tablebox.selection.get() == "Customer":
            self.headers=["ID", "Name", "Phone", "Insurance"]
            self.name="customer"
            self.headersize = 4
        elif self.tablebox.selection.get() == "Sales Representatives":
            self.headers=["ID", "Name", "Phone", "Location"]
            self.name="sales_rep"
            self.headersize = 4
        elif self.tablebox.selection.get() == "Sales":
            self.headers=["ID", "Date", "Agent", "VIN", "Customer"]
            self.name="sales"
            self.headersize = 5
        elif self.tablebox.selection.get() == "RI Toyota":
            self.headers=["Location", "City", "Phone"]
            self.name="ri_toyota"
            self.headersize = 3
        self.heading()
        self.display(sql.selectAll(self.name))
        self.headerbox.update(self.headers)
        self.insertentries.update(self.headers)
    
    def clickBtn(self, name):
        entryString = "'"+self.entry.entry.get()+"'"
        viewname = self.entry.entry.get()
        if name == "Select":
            self.display(sql.select("*",table.name,[self.headerbox.selection.get(),self.comparison_tablebox.selection.get(),entryString]))
        if name == "View":
            sql.view(viewname,"*",table.name,[self.headerbox.selection.get(),self.comparison_tablebox.selection.get(),entryString])
            self.display(sql.select("*",table.name,[self.headerbox.selection.get(),self.comparison_tablebox.selection.get(),entryString]))

        elif name == "Populate":
            focus = self.tv.item(self.tv.focus())
            selection = []
            i = 0
            while i < self.headersize:
                selection.append(focus['values'][i])
                i += 1
            print(selection)
            self.select(selection)
        elif name == "Delete":
            sql.delete(table.name,self.headerbox.selection.get(),entryString)
            self.clickMenu()
            myLabel = Label(root, text="Deleted "+self.entry.entry.get())
            myLabel.grid(row=17, column=1)

        elif name == "Insert":
            sql.insert(table.name, self.headers, [self.insertentries.entry1.entry.get(), self.insertentries.entry2.entry.get(), self.insertentries.entry3.entry.get(), self.insertentries.entry4.entry.get(), self.insertentries.entry5.entry.get()], self.headersize)
            self.display(sql.select("*",table.name,[self.headerbox.selection.get(),self.comparison_tablebox.selection.get(),entryString]))

        elif name == "Select Table":
            self.clickMenu()

        else:
            myLabel = Label(root, text="clicked "+self.entry.entry.get())
            myLabel.grid(row=3, column=1)





    def display(self, val):
        self.clear_all()
        ind = 0
        for contact in val:
            self.tv.insert(parent='', index=ind, iid=ind, text='', values=(contact))
            ind+=1
    def clear_all(self):
        for item in (self.tv.get_children()):
            self.tv.delete(item);


    def select(self, selection):
        selected = [selection]
        self.insertentries.entry1.entry.delete(first=0, last=len(self.insertentries.entry1.entry.get()))
        self.insertentries.entry2.entry.delete(first=0, last=len(self.insertentries.entry2.entry.get()))
        self.insertentries.entry3.entry.delete(first=0, last=len(self.insertentries.entry3.entry.get()))
        self.insertentries.entry4.entry.delete(first=0, last=len(self.insertentries.entry4.entry.get()))
        self.insertentries.entry5.entry.delete(first=0, last=len(self.insertentries.entry5.entry.get()))


        self.insertentries.entry1.entry.insert(0,selected[0][0])
        self.insertentries.entry2.entry.insert(0,selected[0][1])
        if (len(selection) >= 3):
            self.insertentries.entry3.entry.insert(0,selected[0][2])
        if (len(selection) >= 4):
            self.insertentries.entry4.entry.insert(0,selected[0][3])
        if (len(selection) >= 5):
            self.insertentries.entry5.entry.insert(0,selected[0][4])

#--GLOBAL TABLE OBJECT--
table = Table(["None Selected"],[])




def initialize():


    
    


    delete = MyButton("Delete", table.entry, 16, 0)
    search = MyButton("Select", table.entry, 16, 1)
    select_table = MyButton("Select Table", "",8,3)
    select = MyButton("Populate", table.entry, 28, 2)
    createview = MyButton("View",table.entry,16,2)
    insert = MyButton("Insert", table.entry, 28, 1)
    



    root.mainloop()
