from tkinter import *
root = Tk()
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




def main():

    
    entry = Entry(root, width=30, borderwidth=5)
    entry.grid(row=0,column=0, columnspan=3)
    entry.insert(0, "Enter name: ")
    
    select = myButton("Select", entry, 1, 1)
    update = myButton("Update", entry, 2, 1)
    delete = myButton("Delete", entry, 1, 2)
    order = myButton("Order", entry, 2, 2)

    


if __name__ == '__main__':
    main()

root.mainloop()