import customtkinter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x400")

def plot_csv():
    air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
    print(air_quality.head())
    air_quality.plot()
    plt.show()

def plot_quad():
    x = np.linspace(-10, 10, 1000)
    y = x**2 + 2*x + 2
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text='Doot')
label.pack()

btn_csv = customtkinter.CTkButton(master=frame, text='CSV', command=plot_csv)
btn_csv.pack()

btn_quad = customtkinter.CTkButton(master=frame, text='Quadratic', command=plot_quad)
btn_quad.pack()

root.mainloop()
