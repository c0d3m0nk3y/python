import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x400")

def login():
    print('foo')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text='Doot')
label.pack()

button = customtkinter.CTkButton(master=frame, text='Click', command=login)
button.pack()

root.mainloop()
