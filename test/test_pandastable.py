import tkinter
from tkinter import *
import pandas as pd
import pandastable
from pandastable import *

data_table = pd.DataFrame(list(zip('a', 'b', 'c', 'd', 'e')),
                            columns=['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5'])

window = Tk()

f1 = Frame(window)
f1.pack(fill=BOTH, expand=1)


def show_df():
    df = pd.read_csv('test/newfile.csv')
    tabel = Table(f1, model=TableModel(dataframe=df))
    tabel.show()

button = Button(f1, text='Pencet', command=show_df)
button.grid(row=2)

window.mainloop()