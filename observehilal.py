import tkinter as tk
from tkinter import *
from tkcalendar import *
from datetime import datetime
import compute
from pandastable import Table

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
cal_dari = Calendar(window, selectmode="day",
                    date_pattern='y/mm/d',
                    year=datetime.today().year,
                    month=datetime.today().month,
                    day=datetime.today().day)
cal_dari.grid(row=3, column=1)
def Grab_dari():
    var.dari = cal_dari.get_date()

button_dari = Button(window, text="Pilih", command=Grab_dari)
button_dari.grid(row=4, column=1)

# Datepicker Sampai
label_sampai = tk.Label(text='Sampai').grid(row=3, column=2)
cal_sampai = Calendar(window, selectmode="day",
                    date_pattern='y/mm/d',
                    year=datetime.today().year,
                    month=datetime.today().month+1,
                    day=datetime.today().day)
cal_sampai.grid(row=3, column=3)
def Grab_sampai():
    var.sampai = cal_sampai.get_date()

button_sampai = Button(window, text="Pilih", command=Grab_sampai)
button_sampai.grid(row=4, column=3)

f2 = Frame(window)

# Jalankan program
def Get_param():
    lat = val_lat.get()
    long = val_long.get()
    dari = var.dari.split('/')
    sampai = var.sampai.split('/')
    dari = [int(i) for i in dari]
    sampai = [int(i) for i in sampai]
    print("Parameter:")
    print(f"\tLatitude: {lat}")
    print(f"\tLongitude: {long}")
    print(f"\tDari: {dari}")
    print(f"\tSampai: {sampai}")
    compute.result(lat, long, dari, sampai)
    pt = Table(f2, dataframe=compute.var.df, showtoolbar=True, showstatusbar=True)
    pt.show()

button_hitung = Button(window, text="Hitung", command=Get_param)
button_hitung.grid(row=5, column=0)

window.mainloop()