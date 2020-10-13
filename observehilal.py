import tkinter as tk
from tkinter import *
from tkcalendar import *
from datetime import datetime
import compute
from pandastable import Table
import pandas as pd

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
    openNewWindow()

def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(window) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("New Window")
  
    class TabelHilal(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = newWindow
            self.main.geometry('600x400+200+100')
            self.main.title('Hilal')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=0)
            df = compute.var.df
            # df = pd.read_csv('test/newfile.csv')
            self.table = pt = Table(f, dataframe=df,
                                    showtoolbar=False, showstatusbar=False)
            pt.show()

            f2 = Frame(self.main)
            f2.pack(side=LEFT)
            save_button = Button(f2, text='Simpan')
            save_button.pack(side=LEFT)

            return
    TabelHilal()

button_hitung = Button(window, text="Hitung", command=Get_param)
button_hitung.grid(row=5, column=0)

window.mainloop()