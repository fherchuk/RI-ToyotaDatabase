import tkinter
from tkinter import *
from tkinter import ttk
from turtle import heading


root = Tk()
root.title = ("Database")
root.geometry("600x800")


 







class myButton:
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
    def __init__(self, size, values):
        self.size = size
        self.values = values
        self.frame = Frame(root)
        self.tv = ttk.Treeview(self.frame, columns=(1,2,3), show="headings", height = "20")
        self.heading(), self.scroll(), self.display()
        self.frame.grid(row = 10, column = 5)
        self.tv.grid(row = 10, column = 5, sticky='nsew')

    def heading(self):
        self.tv.heading(1, text="Year")
        self.tv.heading(2, text="Make")
        self.tv.heading(3, text="Model")

    def scroll(self):
        scrollbar = ttk.Scrollbar(root, orient = tkinter.VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=10, column=10, sticky='ns')


    def display(self):
        data = []
        for n in range(1, 100):
            year = (n+2000)
            data.append(({year},f'Toyota',f'Supra' ))

        for contact in data:
            self.tv.insert('', tkinter.END, values=contact)




def main():


    
    entry = Entry(root, width=30, borderwidth=5)
    entry.grid(row=0,column=0, columnspan=3)
    entry.insert(0, "Enter name: ")
    
    select = myButton("Select", entry, 1, 1)
    update = myButton("Update", entry, 2, 1)
    delete = myButton("Delete", entry, 1, 2)
    order = myButton("Order", entry, 2, 2)
    table = Table(5, 5)



    


if __name__ == '__main__':
    main()

root.mainloop()