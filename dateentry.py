from datetime import datetime as dt
from tkinter import *

from tkcalendar import *

window = Tk()

f1 = Frame(window)
f1.pack(fill=BOTH, expand=1)
dinput1 = DateEntry(f1, width=12, year=dt.today().year)
dinput2 = DateEntry(f1, width=12, year=dt.today().year)
dinput1.grid(row=1)
dinput2.grid(row=2)

def get_Date():
    date_val = dinput1.get_date()
    print(date_val)

tombol = Button(f1, text="Ini Tombol", command=get_Date)
tombol.grid(row=4)
tombol.grid_anchor('w')

window.mainloop()
