import tkinter
from tkinter import *
from tkinter import filedialog

text_val = "Ini adalah text yang disimpan."

window = Tk()
window.geometry("500x200")

f1 = Frame(window)
f1.pack(fill=BOTH, expand=1)
out_text = Label(f1, text='Ini Output')
label1 = Label(f1, text='Tes Simpan Data')
label1.pack()

def get_dir():
    # f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    f = filedialog.asksaveasfilename(filetypes = (("Text Files", "*.txt"),), defaultextension='.txt')
    with open(f, 'w') as f:
        f.write(text_val)


button1 = Button(f1, text='Ini Tombol', command=get_dir)
button1.pack()


out_text.pack()

window.mainloop()