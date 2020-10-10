import tkinter as tk
from tkinter import *
from tkcalendar import *
from datetime import datetime

class var():
    dari = ""
    sampai = ""
    obs = ['7.83305556 S', '110.38305556 E']

window = tk.Tk()

# Input Latitude
val_lat = tk.StringVar(value=var.obs[0])
label_lat = tk.Label(text="Latitude").grid(row=0, column=0)
in_lat = tk.Entry(textvariable=val_lat, width=20, justify=RIGHT)
in_lat.grid(row=0, column=1)

# Input Longitude
val_long = tk.StringVar(value=var.obs[1])
label_long = tk.Label(text="Longitude").grid(row=1, column=0)
in_long = tk.Entry(textvariable=val_long, width=20, justify=RIGHT)
in_long.grid(row=1, column=1)

# Datepicker dari
label_dari = tk.Label(text='Dari').grid(row=3, column=0)
cal_dari = Calendar(window, selectmode="day", year=datetime.today().year, month=datetime.today().month, day=datetime.today().day)
cal_dari.grid(row=3, column=1)
def Grab_dari():
    var.dari = cal_dari.get_date()

button_dari = Button(window, text="Pilih", command=Grab_dari)
button_dari.grid(row=4, column=1)

# Datepicker Sampai
label_sampai = tk.Label(text='Sampai').grid(row=3, column=2)
cal_sampai = Calendar(window, selectmode="day", year=datetime.today().year, month=datetime.today().month+1, day=datetime.today().day)
cal_sampai.grid(row=3, column=3)
def Grab_sampai():
    var.sampai = cal_sampai.get_date()

button_sampai = Button(window, text="Pilih", command=Grab_sampai)
button_sampai.grid(row=4, column=3)


# Jalankan program
def compute():
    print("Parameter:")
    print(f"\tLatitude: {val_lat.get()}")
    print(f"\tLongitude: {val_long.get()}")
    print(f"\tDari: {var.dari}")
    print(f"\tSampai: {var.sampai}")

button_hitung = Button(window, text="Hitung", command=compute)
button_hitung.grid(row=5, column=0)

window.mainloop()