from turtle import width
import customtkinter as ctk
import tkinter as tk
import sql
import dashboard

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x500")


RED_MAIN = "#CE2029"
RED_HOVER = "#560319"

def connect():
    try:
        connection = sql.SqlConnector(entry1.get(), entry2.get())
        print("connected")
        dashboard.main(connection, root)
    
    except Exception:
        errorlabel.configure(text = "Invalid Login")



frame = ctk.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master = frame, text = "Toytota Database Login", font=ctk.CTkFont(family="arial", size=36))
label.pack(pady = 12, padx = 10)

entry1 = ctk.CTkEntry(master = frame, placeholder_text = "Username", width = 200, height = 35 )
entry1.pack(pady = 12, padx = 10)

entry2 = ctk.CTkEntry(master = frame, placeholder_text = "Password", show = "*", width = 200, height = 35)
entry2.pack(pady = 12, padx = 10)

button = ctk.CTkButton(master = frame, text = "Connect", command = connect, fg_color = RED_MAIN, hover_color = RED_HOVER)
button.pack(pady = 12, padx = 10)

errorlabel = ctk.CTkLabel(master = frame, text = "", text_color = ('red'), font=ctk.CTkFont(family="arial", size=20))
errorlabel.pack(pady = 12, padx = 10)

root.mainloop()