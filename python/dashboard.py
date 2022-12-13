from tkinter import font
from turtle import bgcolor, width
import customtkinter as ctk
import tkinter as tk

from tkinter import *
from tkinter import ttk

import sql

TABLES = ["Vehicles", "Customer", "Sales Representatives", "Sales", "RI Toyota"]




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.attributes('-fullscreen', True)
root.title("Toyota Database")

frame = ctk.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


RED_MAIN = "#CE2029"
RED_HOVER = "#560319"

def main(connect, oldwindow):
    oldwindow.destroy()


    
    label = ctk.CTkLabel(master = frame, text = "Toytota Database")
    label.pack(pady = 12, padx = 10)

    leftFrame = ctk.CTkFrame(master = root)
    leftFrame.pack(pady=20, padx=60, fill="both", side = tk.LEFT, expand=True)
    table = Table(["VIN","Year","Make","Model","Color"])

    current = []

    combobox = ctk.CTkComboBox(master=leftFrame,
                                     values=TABLES,
                                     command =table_check,
                                     variable = current,
                                     width = 200, button_color = RED_MAIN, button_hover_color = RED_HOVER)
    
    combobox.pack(padx=20, pady=10)
    combobox.set("Select Table")


    #Left Panel
    L1 = ctk.CTkFrame(master = leftFrame)
    R1 = ctk.CTkFrame(master = leftFrame)
    
    L1.pack(fill="both", side = tk.LEFT, expand=True)
    R1.pack(fill="both", side = tk.RIGHT, expand=True)

    # - Left Side Buttons

    selectbtn = ctk.CTkButton(master = L1, text = "Select", command = select(current), fg_color = RED_MAIN, hover_color = RED_HOVER)
    selectbtn.pack(pady = 12, padx = 10)
   
    insertbtn = ctk.CTkButton(master = L1, text = "Insert", command = "", fg_color = RED_MAIN, hover_color = RED_HOVER)
    insertbtn.pack(pady = 12, padx = 10)

    updatebtn = ctk.CTkButton(master = L1, text = "Update", command = "", fg_color = RED_MAIN, hover_color = RED_HOVER)
    updatebtn.pack(pady = 12, padx = 10)


    # - Right Side Buttons -

    viewbtn = ctk.CTkButton(master = R1, text = "View", command = "", fg_color = RED_MAIN, hover_color = RED_HOVER)
    viewbtn.pack(pady = 12, padx = 10)

    deletebtn = ctk.CTkButton(master = R1, text = "Delete", command = "", fg_color = RED_MAIN, hover_color = RED_HOVER)
    deletebtn.pack(pady = 12, padx = 10)


    root.mainloop()





def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


def select(table):
    if windows_open():
        pass
    else:
        pop_up = ctk.CTkToplevel()
        pop_up.geometry("400x200")



        
        attributes = ctk.CTkComboBox(master=pop_up,
                                     values= table_check(table),
                                     command=optionmenu_callback,
                                     width = 200, button_color = RED_MAIN, button_hover_color = RED_HOVER)
        attributes.pack(padx=20, pady=10)
        attributes.set("Select ")

        label = ctk.CTkLabel(pop_up, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)







def table_check(choice):
    VEHICLES = ["VIN", "Year", "Make", "Model", "Color"]
    CUSTOMER = ["ID", "Name", "Phone", "Insurance"]
    SALES_REP = ["ID", "Name", "Phone","Location"]
    SALES = ["ID", "Date", "Agent", "VIN", "CUSTOMER"]
    TOYOTA = ["Location", "City", "Phone"]
    
    if choice == "Vehicles":
        return VEHICLES
    elif choice == "Customer":
        return CUSTOMER
    elif choice == "Sales Representatives":
        return SALES_REP
    elif choice == "Sales":
        return SALES
    else:
        return TOYOTA















def windows_open():
    tops = []
    for widget in root.winfo_children(): # Loop through each widget in main window
        if isinstance(widget,Toplevel): # If widget is an instance of toplevel
            tops.append(widget) # Append to a list
    if len(tops) > 0:
        return True
    else:
        return False



class Table:
    def __init__(self, headers):
        self.headers = headers
        self.tv = ttk.Treeview(master = root, columns= ["1,2,3"], show="headings", height = "30")
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure("Treeview", background = "#1A1A1A", fieldbackground = "#212121")
        self.tv.pack(pady=20, padx = 10, fill = tk.BOTH, expand = True)
        self.setHeaders()



    def setHeaders(self):
        self.style.configure('Treeview.Heading', background= RED_MAIN, font = ('bold', 16), foreground = 'white')
        self.tv['columns'] = (self.headers)
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.heading('#0', text='', anchor=CENTER)
        for i in self.headers:
            self.tv.column(i, anchor=CENTER, width = (1000//len(self.headers)))
            self.tv.heading(i, text=i, anchor=CENTER)
