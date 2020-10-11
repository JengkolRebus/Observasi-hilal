from datetime import datetime as d
from tkinter import *
from pandastable import Table

date = d.today().year

print(date)

window = Tk()
f1 = Frame(window)
f2 = Frame(window)

pt = Table(f1)
pt.show()

window.mainloop()