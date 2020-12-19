from datetime import datetime as dt
from tkinter import *
from tkinter import filedialog

import pandas as pd
from pandastable import Table, TableModel
from tkcalendar import *

import compute


class var():
    dari = ""
    sampai = ""
    obs = ['7.83305556 S', '110.38305556 E']

window = Tk()
window.state('zoomed')

# Frame 1 berisi parameter
f1 = Frame(window)
f1.pack(anchor=NW, fill=BOTH, expand=0)

# Input Latitude
val_lat = StringVar(value=var.obs[0])
label_lat = Label(f1, text="Latitude", width=10, anchor="w")
label_lat.grid(sticky=W, row=0, column=0)
in_lat = Entry(f1, textvariable=val_lat, width=12, justify=RIGHT).grid(sticky = W, row=0, column=1)

# Input Longitude
val_long = StringVar(value=var.obs[1])
label_long = Label(f1, text="Longitude", width=10, anchor="w").grid(sticky=W, row=1, column=0)
in_long = Entry(f1, textvariable=val_long, width=12, justify=RIGHT).grid(sticky = W, row=1, column=1)

# Datepicker dari
label_dari = Label(f1, text='Dari', width=10, anchor="w").grid(sticky = W, row=2, column=0)
cal_dari = DateEntry(f1, width=9)
cal_dari.grid(sticky = W, row=2, column=1)

# Datepicker Sampai

t2 = dt.today().month+1
print(t2)
if(t2 > 12):
    t2=dt.today().month -11
    print(t2)
else:
    pass
label_sampai = Label(f1, text='Sampai', width=10, anchor="w").grid(sticky = W, row=4, column=0)
cal_sampai = DateEntry(f1, width=9, month=t2)
cal_sampai.grid(sticky = W, row=4, column=1)

f2 = Frame(window)
f2.pack(fill=BOTH, expand=1)
pt = Table(f2, model=TableModel(dataframe=compute.var.df))
pt.show()

# Jalankan program
def Get_param():
    lat = val_lat.get()
    long = val_long.get()
    dari = cal_dari.get_date()
    sampai = cal_sampai.get_date()
    print("Parameter:")
    print(f"\tLatitude: {lat}")
    print(f"\tLongitude: {long}")
    print(f"\tDari: {dari}")
    print(f"\tSampai: {sampai}")
    compute.result(lat, long, dari, sampai)
    pt = Table(f2, model=TableModel(dataframe=compute.var.df))
    pt.show()
    pt.redraw()

def Save_file():
    filetype = (("Excel Document", "*.xlsx"),)
    f = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=filetype)
    compute.var.df.to_excel(f)
    print("File Saved")

button_hitung = Button(f1, text="Hitung", command=Get_param)
button_hitung.grid(sticky = W, row=6, column=0)

save_button = Button(f2, text='Simpan', command=Save_file)
save_button.grid(row=2)

window.mainloop()
