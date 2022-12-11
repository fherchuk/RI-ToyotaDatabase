import customtkinter as ctk
import tkinter as tk
import sql

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("1200x800")


RED_MAIN = "#CE2029"
RED_HOVER = "#560319"

#remove later
def test(user, psw):
    print(user)
    print(psw)

def connect():
    try:
        sql.SqlConnector(entry1.get(), entry2.get())
        print("connected")
        window = ctk.CTkToplevel()
        window.geometry("400x200")
        label = ctk.CTkLabel(window, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    
    except Exception:
        print("could not connect")



frame = ctk.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master = frame, text = "Toytota Database Login")
label.pack(pady = 12, padx = 10)

entry1 = ctk.CTkEntry(master = frame, placeholder_text = "Username")
entry1.pack(pady = 12, padx = 10)

entry2 = ctk.CTkEntry(master = frame, placeholder_text = "Password", show = "*")
entry2.pack(pady = 12, padx = 10)

button = ctk.CTkButton(master = frame, text = "Login", command = connect, fg_color = RED_MAIN, hover_color = RED_HOVER)
button.pack(pady = 12, padx = 10)

checkbox = ctk.CTkCheckBox(master = frame, text = "Remember Me")
checkbox.pack(pady = 12, padx = 10)

optionmenu_var = ctk.StringVar(value="help")
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = ctk.CTkComboBox(master=frame, values=["=","!",">=",">","<=","<"], command=optionmenu_callback, variable=optionmenu_var, button_color = RED_MAIN, button_hover_color = RED_HOVER)
combobox.pack(padx=400, pady=0, anchor = tk.W)
combobox.set("=")



combobox2 = ctk.CTkComboBox(master=frame, values=["help", "option 2", "option3"], command=optionmenu_callback, variable=optionmenu_var, button_color = RED_MAIN, button_hover_color = RED_HOVER)
combobox2.pack(padx=400, pady=0, anchor = tk.E)
combobox2.set("Options")



radio_var = tk.IntVar(0)
def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radiobutton_1 = ctk.CTkRadioButton(master=frame, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = ctk.CTkRadioButton(master=frame, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)

radiobutton_1.pack(padx=20, pady=10)
radiobutton_2.pack(padx=20, pady=10)


root.mainloop()