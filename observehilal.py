import tkinter as tk
from tkinter import *

window = tk.Tk()

# Input Latitude
val_lat = tk.StringVar(value='Latitude')
label_lat = tk.Label(text="Latitude").grid(row=0, column=0)
in_lat = tk.Entry(textvariable=val_lat, width=20, justify=RIGHT).grid(row=0, column=1)

# Input Longitude
val_long = tk.StringVar(value='Longitude')
label_long = tk.Label(text="Longitude").grid(row=1, column=0)
in_long = tk.Entry(textvariable=val_long, width=20, justify=RIGHT).grid(row=1, column=1)


window.mainloop()