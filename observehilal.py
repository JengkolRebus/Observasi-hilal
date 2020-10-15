from datetime import datetime as dt
from tkinter import *
from tkinter import filedialog

import pandas as pd
from pandastable import Table
from tkcalendar import *

import compute


class var():
    dari = ""
    sampai = ""
    obs = ['7.83305556 S', '110.38305556 E']

window = Tk()
window.state('zoomed')

# Frame 1 berisi parameter
f1 = Frame(window, bg='red')
f1.pack(anchor=NW, fill=BOTH, expand=0)

# Input Latitude
val_lat = StringVar(value=var.obs[0])
label_lat = Label(f1, text="Latitude", width=10, anchor="w", bg='yellow')
label_lat.grid(sticky=W, row=0, column=0)
in_lat = Entry(f1, textvariable=val_lat, width=12, justify=RIGHT).grid(sticky = W, row=0, column=1)

# Input Longitude
val_long = StringVar(value=var.obs[1])
label_long = Label(f1, text="Longitude", width=10, anchor="w", bg='yellow').grid(sticky=W, row=1, column=0)
in_long = Entry(f1, textvariable=val_long, width=12, justify=RIGHT).grid(sticky = W, row=1, column=1)

# Datepicker dari
label_dari = Label(f1, text='Dari', width=10, anchor="w", bg='yellow').grid(sticky = W, row=2, column=0)
cal_dari = DateEntry(f1, width=9)
cal_dari.grid(sticky = W, row=2, column=1)

# Datepicker Sampai
label_sampai = Label(f1, text='Sampai', width=10, anchor="w", bg='yellow').grid(sticky = W, row=4, column=0)
cal_sampai = DateEntry(f1, width=9, month=dt.today().month +1)
cal_sampai.grid(sticky = W, row=4, column=1)

f2 = Frame(window)
f2.pack(fill=BOTH, expand=1)


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
    df = compute.var.df
    out_tabel = Table(f2, dataframe=df)
    out_tabel.show()

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
            f.pack(fill=BOTH,expand=1)
            df = compute.var.df
            # df = pd.read_csv('test/newfile.csv')
            self.table = pt = Table(f, dataframe=df,
                                    showtoolbar=False, showstatusbar=False)
            pt.show()

            
            def Save_file():
                filetype = (("Excel Document", "*.xlsx"),)
                f = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=filetype)
                compute.var.df.to_excel(f)
                print("File Saved")
            
            f2 = Frame(self.main)
            f2.pack(side=LEFT)
            save_button = Button(f2, text='Simpan', command=Save_file)
            save_button.pack(side=LEFT)

            return
    TabelHilal()

button_hitung = Button(f1, text="Hitung", command=Get_param)
button_hitung.grid(sticky = W, row=6, column=0)


save_button = Button(f2, text='Simpan')
save_button.grid(row=2)

window.mainloop()
