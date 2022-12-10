import customtkinter as ctk
import tkinter as tk
ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("1200x800")


#remove later
def test():
    print("test")



frame = ctk.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = ctk.CTkLabel(master = frame, text = "Login System")
label.pack(pady = 12, padx = 10)

entry1 = ctk.CTkEntry(master = frame, placeholder_text = "Username")
entry1.pack(pady = 12, padx = 10)

entry2 = ctk.CTkEntry(master = frame, placeholder_text = "Password", show = "*")
entry2.pack(pady = 12, padx = 10)

button = ctk.CTkButton(master = frame, text = "Login", command = test)
button.pack(pady = 12, padx = 10)

checkbox = ctk.CTkCheckBox(master = frame, text = "Remember Me")
checkbox.pack(pady = 12, padx = 10)

optionmenu_var = ctk.StringVar(value="help")
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = ctk.CTkComboBox(master=frame, values=["help", "option 2", "option3"], command=optionmenu_callback, variable=optionmenu_var, button_color = "#01579b")
combobox.pack(padx=350, pady=0, anchor = tk.W)
combobox.set("Options")



combobox2 = ctk.CTkComboBox(master=frame, values=["help", "option 2", "option3"], command=optionmenu_callback, variable=optionmenu_var, button_color = "#01579b")
combobox2.pack(padx=350, pady=0, anchor = tk.E)
combobox2.set("Options")




root.mainloop()