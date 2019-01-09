from tkinter import *
from tkinter import messagebox


def MessageBox(title, message):

    window = Tk()
    window.geometry("90x200")
    window.wm_withdraw()    # pravi prozor u pozadini
    result = messagebox.askyesno(title, message)

    window.destroy()
    return result
