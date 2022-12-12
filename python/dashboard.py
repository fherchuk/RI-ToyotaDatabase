import customtkinter as ctk
import tkinter as tk

from tkinter import *
from tkinter import ttk

import sql

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("1200x800")

frame = ctk.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

RED_MAIN = "#CE2029"
RED_HOVER = "#560319"

def main(connect, oldwindow):
    oldwindow.destroy()
    
    label = ctk.CTkLabel(master = frame, text = "Toytota Database Login")
    label.pack(pady = 12, padx = 10)

    table = Table()


    root.mainloop()

class Table:
    def __init__(self):
        self.tv = ttk.Treeview(master = root, columns= ["1,2,3"], show="headings", height = "30")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.tv.pack(pady=12, padx = 10)

